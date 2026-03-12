# Supplementary Material S2: Frame Implementations and Validation

**Paper Title:** Scaffolding Student-AI Dialogue: A Framework for Safe Educational Interactions

**Authors:** Olga Muss, Luca Leisten, Charles Edouard Bardyn

------------------------------------------------------------------------

## Table of Contents

1.  [Frame Overview](#1-frame-overview)
2.  [Validation Checks Summary](#2-validation-checks-summary)
3.  [MnemonicCoCreatorFrame](#3-mnemoniccocreatorframe)
4.  [BalancedTurnsFrame](#4-balancedturnsframe)
5.  [ComprehensionTrackerFrame](#5-comprehensiontrackerframe)
6.  [LanguageCheckerFrame](#6-languagecheckerframe)
7.  [PhasesCheckerFrame](#7-phasescheckerframe)

------------------------------------------------------------------------

## 1. Frame Overview

The Marty mnemonic co-creator deployment uses five frames:

| Frame | Responsibility | Implementation |
|------------------|---------------------------|---------------------------|
| **MnemonicCoCreatorFrame** | Primary orchestrator, manages phases and mnemonic state | [`src/backend/frames/marty.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/marty.py) |
| **BalancedTurnsFrame** | Ensures fair participation across students | [`src/backend/frames/balanced_turns.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/balanced_turns.py) |
| **ComprehensionTrackerFrame** | Tracks per-student, per-concept understanding | [`src/backend/frames/comprehension_tracker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/comprehension_tracker.py) |
| **LanguageCheckerFrame** | Validates age-appropriate language | [`src/backend/frames/language_checker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/language_checker.py) |
| **PhasesCheckerFrame** | Enforces phase-specific pedagogical goals | [`src/backend/frames/phases_checker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/phases_checker.py) |


| **Frame** | **Responsibility** | **Key Checks** |
|----------------|---------------|-----------------------|
| **Mnemonic Co-Creator Frame** | Primary orchestrator | Phase tracking, contribution analysis, mnemonic state |
| **Balanced Turns Frame** | Fair participation | Turn-taking order, question limit, monopolization |
| **Comprehension Tracker Frame** | Understanding tracking | Per-student, per-concept comprehension levels |
| **Language Checker Frame** | Age-appropriateness | Vocabulary, sentence length, tone, no emojis |
| **Phases Checker Frame** | Phase adherence | Phase-specific pedagogical goals |
------------------------------------------------------------------------

## 2. Validation Checks Summary

### Legend

-   **D** = Deterministic check (rule-based)
-   **S** = Statistical check (LLM-based)
-   **P1** = Phase 1 (Knowledge Building, 0-3 min)
-   **P2** = Phase 2 (Mnemonic Co-Creation, 3-7 min)
-   **P3** = Phase 3 (Memorization & Practice, 7+ min)
-   **Closure** = Session wrap-up (10+ min)

### Table S2.1: Checks and Actions for Steps 2 (Analyze Input) and 3 (Shape & Generate)

| Frame | Step 2: Analyze Input |   | Step 3: Shape & Generate |   |
|---------------|---------------|:--------------|---------------|:--------------|
|  | **Checks/Actions** | Description | **Checks/Actions** | Description |
| **Balanced Turns Frame** | **Participation Tracking (D)** | Tracks contribution_count, total_speaking_time_seconds (word count ÷ 150 words/min × 60), last_contribution_time per student | **Turn-Taking Guidance** | Instructs AI to acknowledge previous speaker by name, invite suggested next speaker, ask only ONE question. Adds monopolization warning if detected. |
|  | **Monopolization Detection (D)** | Detects if same student speaks 2+ times consecutively by analyzing recent_speakers list |  |  |
|  | **Next Speaker Suggestion (D)** | Suggests next speaker: (1) Find students not in last 3 turns, (2) Sort by lowest contribution count then speaking time, (3) Select first candidate |  |  |
| **Comprehension Tracker Frame** | **Concept Initialization (P1)** | Waits for student-selected concepts from P1 (stored in mnemonic_state), does NOT extract from learning material | **Comprehension Scaffolding** | Provides two lists: (1) Concepts to clarify (confusion/misconceptions with justifications), (2) Concepts already understood (avoid repeating). Instructs AI to gently clarify confused concepts when they arise. |
|  | **Cumulative Comprehension Analysis (S, after P1)** | Assesses student understanding per concept: UNDERSTOOD (correctly explains/applies), CONFUSED (uncertain/questions), MISCONCEPTION (factually incorrect) |  |  |
|  | **Per-Turn Comprehension Analysis (S, after P1)** | Identifies which specific concepts student understood or was confused about in single message, for turn-by-turn logging |  |  |
|  | **Per-Student Tracking (after P1)** | Maintains per-student, per-concept tracking with level, justification, and turn number |  |  |
| **Mnemonic CoCreator Frame (Marty)** | **Speaker & Message Parsing (D)** | Extracts student name and message from raw input using regex pattern matching | **Persona Section** | Defines Marty's role as friendly robot facilitator, lists students with ages, specifies language, prohibits emojis |
|  | **Language Detection (S, Turn 1 only)** | Detects language of first message via LLM, defaults to English if detection fails | **Learning Material Section** | Injects full microcontrollers reference text (4,932 characters) for validating student contributions |
|  | **Time & Phase Tracking (D)** | Determines current phase based on elapsed time: P1 (0-3 min), P2 (3-7 min), P3 (7+ min), Closure (10+ min) | **Phase 1 Instructions (P1)** | Instructs AI to ask open-ended questions, let students propose concepts, never suggest concepts itself. **Critical rule: DO NOT PROPOSE ANY CONCEPTS YOURSELF** |
|  | **Contribution Analysis (S)** | Classifies message type (mnemonic_suggestion, knowledge_statement, question, builds_on_idea, off_topic, recall_attempt, recall_question) | **Phase 2 Instructions (P2)** | Instructs AI to help students BUILD mnemonic using selected concepts, ask students by name, narrate story progress every 1-3 contributions |
|  | **Mnemonic State Management (S, P1-P2)** | Extracts selected concepts from P1 conversation; updates mnemonic_text during P2 | **Phase 3 Instructions (P3)** | Recall-only mode: recite full story if asked, redirect questions/additions, ask students to recite from memory, provide hints only if all students stuck |

### Table S2.2: Checks and Actions for Steps 4 (Verify) and 5 (Repair)

| Frame | Step 4: Verify |   | Step 5: Repair |   |
|---------------|---------------|:--------------|---------------|:--------------|
|  | **Checks/Actions** | Description | **Checks/Actions** | Description |
| **Language Checker Frame** | **Age-Appropriateness Check (S)** | Validates vocabulary, sentence length (1-5 clauses), tone (friendly, encouraging), no emojis, no condescending language. Includes lesson context and selected concepts as acceptable technical terms. Action if fails: REVISE | **Correction of language** | Returns feedback to engine for LLM regeneration: "The language was not appropriate for a {target_age}-year-old. Please simplify your wording, reduce complexity, and use a more encouraging, less complex tone." |
| **Balanced Turns Frame** | **Turn-Taking Validation (D)** | Checks: (1) Previous speaker mentioned, (2) Suggested next speaker mentioned, (3) Correct order (previous before next), (4) No other students mentioned. Action if fails: REVISE | **Correction of the previous and/or next speaker** | Returns detailed feedback to engine for LLM regeneration (e.g., "TURN-TAKING ERROR: You mentioned {wrong_student}, but should only interact with {previous_speaker} and {suggested_next}") |
|  | **Question Limit Check (D)** | Counts '?' characters in draft, requires exactly 1 question per response per student to avoid overwhelming students. **Action if fails:** REVISE |  |  |
| **Phases Checker Frame** | **Phase 1 Adherence (S, P1)** | P1: Validates AI asks open questions, encourages discussion. Fails if: Suggests specific concepts, starts creating mnemonic prematurely. Action if fails: REVISE | **Correction for phase instructions** | Returns phase-specific feedback to the frame engine for LLM regeneration (e.g., "The response did not adhere to the Phase Goal. {required_adjustment}"). For Closure: provides detailed instructions to thank all students, mention time is up, celebrate accomplishment, and NOT invite another student. |
|  | **Phase 2 Adherence (S, P2)** | P2: Validates AI encourages building on ideas, asks for creative additions, narrates story progress. Allows longer summaries if they end with invitation. Fails if: Provides complete mnemonic phrases, tests recall prematurely. **Action if fails:** REVISE |  |  |
|  | **Phase 3 Adherence (S, P3)** | P3: Validates AI asks students to recite from memory, provides hints when stuck. Fails if: Continues adding to mnemonic instead of practicing. **Action if fails:** REVISE |  |  |
|  | **Closure Validation (S, Closure)** | Closure: Validates: (1) Thanks ALL students by name, (2) Mentions session time is up, (3) Celebrates accomplishment, (4) Encourages practice, (5) Friendly goodbye, (6) Does NOT invite another student to speak. **Action if fails:** REVISE |  |  |

------------------------------------------------------------------------

## 3. MnemonicCoCreatorFrame

**Class**: `MnemonicCoCreatorFrame`\
**Identifier**: `'mnemonic_co_creator_marty'`\
**Location**: [`src/backend/frames/marty.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/marty.py)

### Configuration

``` python
MnemonicCoCreatorFrame(
    students=['Alice', 'Bob', 'Charlie'],
    topic='microcontrollers',
    mnemonic_type='Story',
    learning_material=microcontrollers_text,  # 4,932 characters
    session_duration_minutes=10,
    phase_durations_minutes=[3, 7, 10],
    target_language='English'
)
```

### Slot 1: Analyze Input

**Speaker & Message Parsing** \[Deterministic\]: - Regex: `r'(?:\[\d{2}:\d{2}:\d{2}\]\s*)?([A-Za-z]+):\s*(.+)'` - Output: `shared_context['_speaker']`, `shared_context['_cleaned_message']`

**Language Detection** \[Statistical, Turn 1 only\]: - LLM prompt: "What language is this text written in? Respond with ONLY the name..." - Fallback: 'English'

**Time & Phase Tracking** \[Deterministic\]: - Phase 1: 0–3 min, Phase 2: 3–7 min, Phase 3: 7–10 min, Closure: 10+ min - Output: `shared_context['_session_phase']`

**Contribution Analysis** \[Statistical\]: - Types: mnemonic_suggestion, knowledge_statement, question, builds_on_idea, off_topic, recall_attempt, recall_question

**Mnemonic State Management** \[Statistical\]: - Extracts `selected_concepts` from Phase 1 conversation (NOT from learning material) - Updates `mnemonic_text` during Phase 2

### Slot 2: Shape Prompt

**Persona Section**: Defines Marty's role, lists students with ages, specifies language, prohibits emojis

**Learning Material Section**: Injects full microcontrollers reference text (4,932 characters)

**Phase-Specific Instructions**: - **Phase 1**: Ask open questions, let students propose concepts, **DO NOT PROPOSE ANY CONCEPTS YOURSELF** - **Phase 2**: Help students BUILD mnemonic, ask by name, narrate progress every 1-3 contributions - **Phase 3**: Recall-only mode, recite if asked, redirect additions, provide hints if all stuck

### Slot 3: Validate Output

Delegates all validation to specialized frames (returns PASS).

### Slot 4: Repair Output

No programmatic repair (returns `None`).

------------------------------------------------------------------------

## 4. BalancedTurnsFrame

**Class**: `BalancedTurnsFrame`\
**Identifier**: `'balanced_turns_validator'`\
**Location**: [`src/backend/frames/balanced_turns.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/balanced_turns.py)

### Slot 1: Analyze Input

**Participation Tracking** \[Deterministic\]: - Metrics: `contribution_count`, `total_speaking_time_seconds` (word count ÷ 150 × 60), `last_contribution_time` - Tracks `recent_speakers` (last 5)

**Monopolization Detection** \[Deterministic\]: - Trigger: Same student speaks 2+ times consecutively - Output: `shared_context['_consecutive_same_speaker']`

**Next Speaker Suggestion** \[Deterministic\]: - Algorithm: (1) Find students not in last 3 turns, (2) Sort by contribution count then speaking time, (3) Select first - Output: `shared_context['_suggested_next_speaker']`

### Slot 2: Shape Prompt

Adds turn-taking guidance: Acknowledge previous speaker, invite suggested next speaker, ask only ONE question. Adds monopolization warning if detected.

### Slot 3: Validate Output

**Turn-Taking Validation** \[Deterministic\]: - Checks: (1) Previous speaker mentioned, (2) Suggested next mentioned, (3) Correct order, (4) No other students - Action if fails: REVISE with detailed feedback

**Question Limit Check** \[Deterministic\]: - Counts '?' characters, requires exactly 1 - Action if fails: REVISE

### Slot 4: Repair Output

No programmatic repair (returns `None`).

------------------------------------------------------------------------

## 5. ComprehensionTrackerFrame

**Class**: `ComprehensionTrackerFrame`\
**Identifier**: `'comprehension_tracker_frame'`\
**Location**: [`src/backend/frames/comprehension_tracker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/comprehension_tracker.py)

### Initialization

**Concept Source**: Waits for student-selected concepts from Phase 1 (`mnemonic_state`), does NOT extract from learning material.

**Tracking Structure**:

``` python
{
    'concepts': selected_concepts,
    'by_student': {
        student: {
            concept: {'level': 'not_seen', 'justification': None, 'turn': None}
        }
    }
}
```

### Slot 1: Analyze Input

**Dual Comprehension Analysis** \[Statistical, concurrent\]:

**Analysis 1 - Cumulative** (session-long tracking): - Levels: UNDERSTOOD, CONFUSED, MISCONCEPTION - Updates per-student, per-concept profiles

**Analysis 2 - Per-Turn** (logging): - Identifies concepts understood/confused in single message

### Slot 2: Shape Prompt

**Comprehension Scaffolding**: - List 1: Concepts to clarify (with justifications) - List 2: Concepts already understood (avoid repeating)

### Slot 3: Validate Output

No validation checks (returns PASS).

### Slot 4: Repair Output

No repair logic (returns `None`).

------------------------------------------------------------------------

## 6. LanguageCheckerFrame

**Class**: `LanguageCheckerFrame`\
**Identifier**: `'language_checker_frame'`\
**Location**: [`src/backend/frames/language_checker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/language_checker.py)

### Configuration

``` python
LanguageCheckerFrame(
    target_age=14,
    lesson_context=microcontrollers_text,
    selected_concepts=['GPIO pins', 'PWM', 'I2C']
)
```

### Slot 3: Validate Output

**Age-Appropriateness Check** \[Statistical\]:

**Validation Prompt** (abbreviated):

```         
Check whether the RESPONSE is suitable for a {target_age}-year-old:
keep sentences short (1-5 clauses), friendly, encouraging, and free of emojis.

CONTEXT ABOUT TODAY'S LESSON (acceptable technical terms):
{lesson_context}

Currently selected lesson concepts (always allowed):
{selected_concepts}

Return ONLY JSON: {"complies": <bool>, "rationale": "..."}
```

**Criteria**: - Vocabulary for 13-14 year olds - Sentences: 1-5 clauses - Tone: Friendly, encouraging - No emojis, no condescension

**Action if fails**: REVISE with feedback: "The language was not appropriate for a {target_age}-year-old. Please simplify your wording, reduce complexity, and use a more encouraging, less complex tone."

### Slot 4: Repair Output

No programmatic repair (returns `None`).

------------------------------------------------------------------------

## 7. PhasesCheckerFrame

**Class**: `PhasesCheckerFrame`\
**Identifier**: `'phases_checker_frame'`\
**Location**: [`src/backend/frames/phases_checker.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frames/phases_checker.py)

### Configuration

``` python
PhasesCheckerFrame(
    phase_goals={
        1: "Help students select 3-5 key concepts. DO NOT suggest concepts yourself.",
        2: "Help students BUILD the mnemonic. Facilitate their creativity.",
        3: "Test recall. NO new content, only practice reciting.",
        'closure': "Thank all students, celebrate, say goodbye. Do NOT invite next speaker."
    }
)
```

### Slot 3: Validate Output

**Phase Adherence Check** \[Statistical\]:

**Validation Prompt** (abbreviated):

```         
Evaluate the RESPONSE against the PHASE INSTRUCTIONS and decide if it complies.

--- PHASE INSTRUCTIONS ---
{phase_instructions}

--- RESPONSE ---
{response}

Summaries/narrations are acceptable if they end by inviting the next student.

Return ONLY JSON: {"complies": <bool>, "rationale": "...", "required_adjustment": "..."}
```

**Phase-Specific Validation**: - **Phase 1**: Asks open questions, does NOT suggest concepts - **Phase 2**: Facilitates creation, does NOT provide complete phrases - **Phase 3**: Tests recall, does NOT add new content - **Closure**: Thanks all students, does NOT invite next speaker

**Action if fails**: REVISE with phase-specific feedback

### Slot 4: Repair Output

No programmatic repair (returns `None`).

------------------------------------------------------------------------

## References

**Complete source code**: <https://github.com/OlgaMuss/BuildBot/tree/main/LLM_Frames_Design/frame_engine_v1.1.2>

**Contact**: - Luca Leisten: [luca.leisten\@gess.ethz.ch](mailto:luca.leisten@gess.ethz.ch) - Olga Muss: [olga.muss\@unine.ch](mailto:olga.muss@unine.ch)