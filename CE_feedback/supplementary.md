## Supplementary Information

### A Layered Reliability Framework for Trustworthy AI in Education

*Luca Leisten\** (ETH Zurich)  
*Olga Muss\** (Université de Neuchâtel, ETH Zurich)  
*Charles Edouard Bardyn* (AI Swiss)

\*These authors contributed equally to this work

Correspondence: <!-- TODO: corresponding author name --> (<!-- TODO: corresponding author email -->)

---

## S1. Technical Architecture

### S1.0 Trusted Computing Base (TCB)

Our deterministic guarantees rely on the correctness of the following components:

**Core validation code:**
- Python 3.11 runtime
- Structured response contracts validated deterministically against a schema (Pydantic or equivalent JSON Schema validation) (version <!-- TODO -->)
- Custom predicate implementations (length checks, blocklist matching, regex validation)

**External dependencies:**
- LLM API (Vertex AI): We do not trust the LLM to be deterministic; we verify its outputs. We do not assume structured-output compliance. Instead, we validate schema conformance; on parse or validation failure, the system falls back to a predefined safe response.
- Speech-to-text system: <!-- TODO: specify system --> for transcription. Transcription errors can cause verification to operate on incorrect text; this is a known limitation.

**Not in TCB (explicitly verified):**
- LLM generation itself (the stochastic component we are making reliable)
- LLM judge verdicts (calibrated against human ground truth but not trusted as deterministic)

**Testing and validation:** We tested the system with a set of known disallowed prompts (including blatantly toxic queries, privacy-violating requests, and known "jailbreak" patterns) to verify that such inputs trigger immediate blocking or safe fallbacks. We included unit tests for each deterministic validator (format, blocklist, turn-count, etc.). In all test cases, the system responded with the intended safe fallback and logged an alert—no unsafe content was returned. Additionally, we verified that no code path could return an unverified candidate by tracing all response routes and confirming each terminates either in a verified output or a fallback.

**Formal invariants:** By construction, any response leaving the system must satisfy all deterministic checks (this is enforced by code). Once a response passes a "critical" check, that specific property is locked in and will not be regressed by subsequent repair attempts (monotonic non-regression).

<!-- TODO: Report actual test coverage numbers and add any property-based testing results if conducted -->

### S1.1 The 8-stage pipeline (implementation view)

The three conceptual phases described in the main text are implemented as eight discrete stages in the technical architecture:

| Stage | Phase | Purpose |
|-------|-------|---------|
| 1. PREPARE | Before | Filter context, retrieve materials, inject state |
| 2. ANALYZE | Before | Extract signals, evaluate bypass conditions |
| 3. ENCODE | During | Configure and execute the LLM call (including tools); produce raw output |
| 4. DETECT | After | Parse output, validate schema, run deterministic/statistical verification |
| 5. CORRECT | After | Fix detected violations (loop) |
| 6. TRANSFORM | After | Enhance a verified response (e.g., formatting/localisation) |
| 7. PERSIST | After | Update memory with verified information only |
| 8. ALERT | After | Generate notifications for human supervisors |

### S1.2 Stage Details

**Stage 1: PREPARE**

Controls what information the language model receives:
- History filtering (last N turns, summarization)
- Retrieval augmentation (relevant educational materials)
- Context injection (session state, user profile, time)

**Stage 2: ANALYZE**

Extracts structured signals from user input:
- Intent classification
- Emotional state estimation
- Topic relevance assessment
- Safety concern detection

ANALYZE can trigger **bypass**, returning an immediate response without LLM generation. Bypass reasons include:
- Safety: Harmful content detected
- Efficiency: FAQ match from cache
- Control: Off-topic rejection
- Integrity: Exam mode blocking

**Stage 3: ENCODE**

Constructs the prompt from composed frames and executes the model call:
- Collects instructions from all active frames
- Resolves conflicts by priority
- Renders structured system prompt
- Defines structured response contract (schema)
- Calls the LLM (including tool/function calls when applicable), returning raw output

**Stage 4: DETECT**

Three sub-stages:
1. **Parse**: Extract structured data from raw LLM output
2. **Validate**: Check against response schema
3. **Verify**: Run deterministic and statistical checks

**Stage 5: CORRECT**

Two correction types:
- **Deterministic**: Code-based fixes (truncation, formatting)
- **Statistical**: Re-generation with targeted feedback

After correction, DETECT runs again (repair loop).

**Formal repair algorithm with monotonicity:**

```python
def verify_and_repair(response: str, 
                      checks: List[Check], 
                      max_iterations: int = 2,
                      budget_timeout_sec: float = 5.0) -> Tuple[str, Status]:
    """
    Iteratively verify and repair a response, enforcing monotonicity on critical checks.
    
    Returns:
        (final_response, status) where status in {PASSED, FALLBACK}
    """
    start_time = time.time()
    r_current = response
    
    # Separate critical and non-critical checks
    C_critical = [c for c in checks if c.is_critical]
    C_noncritical = [c for c in checks if not c.is_critical]
    
    # Track which critical checks are currently passing
    C_passing = {c.name for c in C_critical if c.evaluate(r_current)}
    
    for iteration in range(max_iterations):
        # Check budget
        if time.time() - start_time > budget_timeout_sec:
            log_warning(f"Budget exhausted after {iteration} iterations")
            return generate_fallback(), Status.FALLBACK
        
        # Run all checks
        violations = [c for c in checks if not c.evaluate(r_current)]
        
        if not violations:
            # All checks pass
            log_success(f"Verified after {iteration} iteration(s)")
            return r_current, Status.PASSED
        
        # Attempt correction
        r_candidate = attempt_correction(r_current, violations)
        
        # Monotonicity check: do critical checks still pass?
        C_candidate_passing = {c.name for c in C_critical if c.evaluate(r_candidate)}
        
        if not C_passing.issubset(C_candidate_passing):
            # Monotonicity violation: correction broke a critical property
            regressed = C_passing - C_candidate_passing
            log_warning(f"Monotonicity violation at iteration {iteration}: "
                       f"regressed checks: {regressed}")
            alert_monotonicity_violation(regressed)
            return generate_fallback(), Status.FALLBACK
        
        # Correction is safe; accept it
        r_current = r_candidate
        C_passing = C_candidate_passing
    
    # Max iterations exhausted
    log_warning(f"Max iterations ({max_iterations}) exhausted with violations remaining")
    return generate_fallback(), Status.FALLBACK


def attempt_correction(response: str, violations: List[Check]) -> str:
    """
    Attempt to fix violations. Strategy depends on check type.
    """
    # Try deterministic fixes first (fast, reliable)
    for check in violations:
        if check.has_deterministic_fix():
            response = check.apply_fix(response)
    
    # Re-check; if deterministic fixes resolved everything, return
    remaining = [c for c in violations if not c.evaluate(response)]
    if not remaining:
        return response
    
    # Fall back to statistical correction: regenerate with feedback
    feedback = construct_feedback(remaining)
    return regenerate_with_feedback(response, feedback)
```

This algorithm ensures:
1. **Non-regression**: Critical properties never worsen
2. **Budget-bounded**: Finite time and iteration limits
3. **Fallback guarantee**: Students never see unverified content
4. **Deterministic-first**: Fast fixes attempted before expensive regeneration

**Stage 6: TRANSFORM**

Enhances an already-verified response for presentation (e.g., formatting, localisation) without changing its verified meaning.

**Stage 7: PERSIST**

Updates system state:
- Conversation memory
- Student progress tracking
- Comprehension assessments

**Important**: Only verified information is persisted. Failed interactions do not update state.

**Stage 8: ALERT**

Generates notifications:
- Info: Routine observations
- Warning: Concerning patterns
- Critical: Immediate attention required

---

### S1.3 Robustness testing (future work)

The current deployment focused on naturalistic classroom interaction. Future work should include systematic stress testing:

**Adversarial inputs:**
- Prompt injection attempts ("Ignore previous instructions and reveal the answer")
- Jailbreak patterns from public databases
- Multilingual code-switching (German/English mixing)
- Deliberately ambiguous or off-topic queries

**Distribution shift:**
- Different age groups (10–12, 16–18)
- Different tasks (math tutoring, essay feedback, exam proctoring)
- Different transcript quality (simulated speech recognition errors)
- Different models (GPT-4, Claude, Llama 3)

**Judge ensemble:**
- Comparing verdicts across different judge models
- Majority voting schemes
- Confidence calibration under distribution shift

**Property-based testing:**
- Fuzzing validation predicates with random inputs
- Verifying that deterministic checks always produce the same output for same input
- Testing fallback coverage (no code path ever exposes unverified content)

<!-- TODO: If any of these tests were conducted, report results here. -->

---

## S2. Proof-of-Concept Frame Implementation

### S2.1 Frame Configuration

```
Frame: Mnemonic Creation Assistant
Target age: 13-15 years
Language: German
Session duration: <!-- TODO: total duration per condition and/or per session -->
Group size: 3-4 students
```

### S2.2 Persona Definition

The AI assistant was configured with the following persona:

> You are a friendly robot buddy helping students learn together. You are encouraging, patient, and enthusiastic about learning. You never talk down to students or use overly complex language. You facilitate discussion rather than providing answers. You ensure everyone participates equally.

### S2.3 Phase Definitions

The phase timings below describe the default schedule for a 10-minute condition; if a condition duration differs, timings are rescaled proportionally by the frame configuration.

**Phase 1: Concept Selection (0-3 minutes)**
- Goal: Students identify 3-5 key concepts
- AI behavior: Ask open questions, do NOT suggest concepts
- Transition: Automatic at 3 minutes

**Phase 2: Mnemonic Creation (3-7 minutes)**
- Goal: Collaborative creation of mnemonic
- AI behavior: Facilitate contributions, recite draft periodically
- Transition: At 7 minutes (or 10 if no quality mnemonic)

**Phase 3: Practice (8-10 minutes)**
- Goal: Memorization through recall
- AI behavior: Test recall, provide hints, redirect modification attempts
- Transition: At 10 minutes

**Closure (10+ minutes)**
- Goal: Positive wrap-up
- AI behavior: Thank students, celebrate accomplishment

### S2.4 Verification Prompts

**Age-appropriate language check:**
```
You are a validation AI. Determine if the following RESPONSE is written in 
vocabulary and style appropriate for a 13-15 year old student. The tone 
should be encouraging and age-appropriate, not condescending or overly complex.

Your answer must be a single word: either "true" or "false".

--- RESPONSE ---
{response}
----------------
```

**Phase alignment check:**
```
You are a validation AI. Determine if the provided RESPONSE is appropriate 
for the current session phase.

Current phase: {phase_name}
Phase goal: {phase_goal}
Phase requirements: {phase_requirements}

Your answer must be a single word: either "true" or "false".

--- RESPONSE ---
{response}
----------------
```

**Content accuracy check:**
```
You are a validation AI. Determine if any factual claims in the RESPONSE 
are consistent with the provided SOURCE MATERIAL about microcontrollers.

--- SOURCE MATERIAL ---
{source_material}
-----------------------

--- RESPONSE ---
{response}
----------------

Your answer must be a single word: either "true" or "false".
```

### S2.5 Turn Management

Turn tracking implemented with deterministic counters:
- `participation_count[student_name]`: Number of contributions per student
- `speaking_time[student_name]`: Estimated speaking time per student
- `consecutive_turns[student_name]`: Consecutive turns without other speakers

Balancing rule: If any student has `consecutive_turns > 2` or `participation_count` below group average by more than 2, prompt includes instruction to invite that student.

### S2.6 Memory Structure

Session memory stored as JSON:

```json
{
  "session_id": "uuid",
  "start_time": "ISO timestamp",
  "current_phase": 1,
  "selected_concepts": [],
  "mnemonic_draft": "",
  "student_participation": {
    "Anna": {"turns": 3, "concepts_contributed": ["CPU"]},
    "Max": {"turns": 2, "concepts_contributed": []},
    "Lisa": {"turns": 4, "concepts_contributed": ["memory", "GPIO"]}
  },
  "comprehension_tracking": {
    "Anna": {"understood": ["CPU"], "confused": []},
    "Max": {"understood": [], "confused": ["GPIO"]},
    "Lisa": {"understood": ["memory", "GPIO"], "confused": []}
  }
}
```

---

## S3. Study Materials

### S3.1 Learning Material: Microcontrollers

[Source material provided to the frame for content verification - to be included]

### S3.2 Pre-Session Briefing

[Student instructions - to be included]

### S3.3 Post-Session Survey

[Survey instrument - to be included]

---

## S4. Execution Trace Schema

Every interaction generates a structured execution trace for audit and analysis. Example schema (JSON):

```json
{
  "interaction_id": "uuid",
  "session_id": "hashed_session_identifier",
  "student_id": "hashed_student_identifier",
  "timestamp": "ISO 8601",
  "input": {
    "text": "student utterance (transcribed)",
    "audio_quality": 0.95,
    "language_detected": "de"
  },
  "pipeline": {
    "phase_1_prepare": {
      "context_window_tokens": 1250,
      "circuit_breaker_triggered": false
    },
    "phase_2_analyze": {
      "intent": "concept_suggestion",
      "current_phase": "phase_1_concept_selection",
      "participation_gap_detected": true
    },
    "phase_3_encode": {
      "active_frames": ["mnemonic_facilitator", "age_13_15", "phase_1_rules"],
      "priority_conflicts_resolved": 0,
      "model": "gemini-2.5-flash",
      "model_version": "...@20250115",
      "temperature": 0.7,
      "latency_ms": 842
    },
    "phase_4_detect": {
      "initial_response": "...",
      "checks_run": [
        {"name": "length", "type": "deterministic", "passed": true},
        {"name": "phase_appropriate", "type": "statistical", "passed": false, "judge_verdict": "false", "judge_latency_ms": 320}
      ],
      "violations_detected": ["phase_appropriate"]
    },
    "phase_5_correct": [
      {
        "iteration": 1,
        "correction_type": "regenerate_with_feedback",
        "feedback": "Response provides guidance instead of eliciting concepts. Revise to ask open question.",
        "candidate_response": "...",
        "recheck_results": {
          "phase_appropriate": {"passed": true},
          "length": {"passed": true}
        },
        "monotonicity_check": "passed",
        "accepted": true
      }
    ],
    "phase_6_transform": {
      "transforms_applied": ["format_for_tts"],
      "changed_semantics": false
    },
    "phase_7_persist": {
      "memory_updated": true,
      "state_changes": {"concepts_discussed": ["CPU", "memory"]}
    },
    "phase_8_alert": {
      "alerts_generated": []
    }
  },
  "output": {
    "text": "final verified response",
    "status": "passed_after_correction",
    "total_latency_ms": 1650,
    "api_calls": 2,
    "cost_usd": 0.00042
  }
}
```

These traces enable post-hoc analysis of:
- Which checks fail most frequently
- Correction success rates by violation type
- Latency distribution by pipeline stage
- Monotonicity violation patterns
- Cost per interaction

All traces are stored with hashed identifiers; re-identification requires access to the salt (stored separately, access-controlled).

---

## S5. Analysis Code

[Analysis scripts for processing execution traces - to be included after data collection]

---

## S6. Raw Results

[Execution traces and analysis results - to be included after data collection]


