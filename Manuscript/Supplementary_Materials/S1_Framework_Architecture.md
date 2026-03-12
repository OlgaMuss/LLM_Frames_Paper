# Supplementary Material S1: Framework Architecture and Specification

**Paper Title:** Scaffolding Student-AI Dialogue: A Framework for Safe Educational Interactions

**Authors:** Olga Muss, Luca Leisten, Charles Edouard Bardyn

------------------------------------------------------------------------

## Table of Contents

1.  [Introduction](#1-introduction)
2.  [Terminology: SCAFFOLD vs. Rodin Frame Engine](#2-terminology-scaffold-vs-rodin-frame-engine)
3.  [System Architecture](#3-system-architecture)
4.  [Six-Step Processing Pipeline](#4-six-step-processing-pipeline)
5.  [Frame Abstraction](#5-frame-abstraction)
6.  [State Management](#6-state-management)
7.  [Technology Stack](#7-technology-stack)

------------------------------------------------------------------------

## 1. Introduction

This document provides technical specifications for the SCAFFOLD (Steered Contextual AI Framework for Orchestrating Learning Dialogue) framework implementation. The system processes each student interaction through a six-step pipeline with multiple validation and repair stages.

**Repository**: <https://github.com/OlgaMuss/BuildBot>

**Implementation Location**: `LLM_Frames_Design/frame_engine_v1.1.2/code/`

------------------------------------------------------------------------

## 2. Terminology: SCAFFOLD vs. Rodin Frame Engine

### Conceptual Model (Paper)

The paper describes **SCAFFOLD** using a **6-step conceptual model** for clarity:

1.  **Collect Data**: Assemble all information
2.  **Analyze Input**: Deep analysis of student message
3.  **Shape & Generate**: Construct prompt and generate response
4.  **Verify**: Validate draft against requirements
5.  **Repair**: Fix validation failures
6.  **Deliver**: Release response and update memory

### Implementation (Code)

The codebase implements this as the **Rodin Frame Engine** with a **4-slot pipeline**:

**Table S1.1**: Mapping between conceptual paper steps and implementation slots

| Paper Step | Implementation Slot | Frame Method | Purpose |
|------------------|--------------------|------------------|------------------|
| Step 1: Collect Data | \[Implicit\] | Engine initialization | Assembles user input, conversation history, frame memory |
| Step 2: Analyze Input | **Slot 1** | `analyze_input()` | Deep analysis before prompt construction |
| Step 3: Shape & Generate | **Slot 2** | `get_prompt_sections()` + `shape_prompt()` | Construct prompt and generate LLM response |
| Step 4: Verify | **Slot 3** | `validate_output()` | Validate LLM draft against requirements |
| Step 5: Repair | **Slot 4** | `repair_output()` | Fix validation failures or regenerate with feedback |
| Step 6: Deliver | \[Implicit\] | Final response delivery | Release validated response and update memory |

**Rationale**: Steps 1 and 6 are always the same (initialization and cleanup), so they're built into the engine rather than requiring frame implementations.

------------------------------------------------------------------------

## 3. System Architecture

### Core Components

```         
┌─────────────────────────────────────────────────────────────┐
│                      FrameEngine                            │
│  - Orchestrates pipeline execution                          │
│  - Manages FrameContext state                               │
│  - Invokes LLM provider                                     │
│  - Coordinates validation and repair                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                      FrameContext                           │
│  - user_input, conversation_history                         │
│  - frame_memory (persistent), shared_context (ephemeral)    │
│  - prompt_sections, system_prompt                           │
│  - llm_draft_response, validation_results                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    Frame (Abstract)                         │
│  - analyze_input(context) → Optional[dict]                  │
│  - get_prompt_sections(context) → list[tuple]               │
│  - shape_prompt(context, prompt) → str                      │
│  - validate_output(context) → ValidationResult              │
│  - repair_output(context) → Optional[str]                   │
└─────────────────────────────────────────────────────────────┘
                          ↑
        ┌─────────────────┴─────────────────┐
        │ Concrete Frame Implementations    │
        │ (Marty, BalancedTurns, etc.)      │
        └───────────────────────────────────┘
```

### Key Classes

**`FrameEngine`** ([`src/backend/frame_engine/engine.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frame_engine/engine.py)): - Orchestrates pipeline execution - Manages `FrameContext` state - Invokes LLM provider - Coordinates validation and repair loops

**`Frame`** ([`src/backend/frame_engine/frame.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frame_engine/frame.py)): - Abstract base class defining 4-slot interface - Provides default no-op implementations - Frames override only needed slots

**`FrameContext`** ([`src/backend/frame_engine/context.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frame_engine/context.py)): - TypedDict defining complete pipeline state - Contains input data, memory, prompt, response, validation results

------------------------------------------------------------------------

## 4. Six-Step Processing Pipeline

### Step 1: Collect Data \[Engine Initialization\]

**Implementation**: Implicit in `FrameEngine.ainvoke()` method.

**Data Assembled**:

``` python
initial_state = FrameContext(
    user_input=user_input,              # Raw input string
    conversation_history=history_copy,   # List of previous turns
    frame_memory=frame_memory,           # Persistent state
    shared_context={},                   # Ephemeral data
    prompt_sections=[],                  # Accumulator
    system_prompt='',                    # Final prompt
    llm_draft_response='',               # LLM output
    validation_results={},               # Validation outcomes
    repair_attempts=0                    # Repair counter
)
```

------------------------------------------------------------------------

### Step 2: Analyze Input \[Slot 1: `analyze_input()`\]

**Purpose**: Perform deep analysis of user message to inform subsequent steps.

**Execution**: Engine calls each frame's `analyze_input()` sequentially, updating `shared_context`.

**Example Analyses**: - Speaker identification (deterministic) - Contribution type classification (statistical) - Comprehension assessment (statistical) - Next speaker suggestion (deterministic)

------------------------------------------------------------------------

### Step 3: Shape and Generate \[Slot 2: Prompt Construction + LLM Call\]

**Three Phases**:

**Phase 3a - Accumulation** (`get_prompt_sections()`): - Frames contribute labeled sections - Engine accumulates into `prompt_sections`

**Phase 3b - Shaping** (`shape_prompt()`): - Frames can modify assembled prompt - Applied sequentially

**Phase 3c - LLM Generation**: - Engine invokes LLM with final prompt - Stores draft in `llm_draft_response`

------------------------------------------------------------------------

### Step 4: Verify \[Slot 3: `validate_output()`\]

**Purpose**: Validate LLM draft against all requirements.

**Execution**: All frames' `validate_output()` run **concurrently** for speed.

**Validation Actions**: - **PASS**: All checks passed → proceed to Step 6 - **REVISE**: Some checks failed → proceed to Step 5 with feedback - **FAIL**: Critical failure → use safe fallback

------------------------------------------------------------------------

### Step 5: Repair \[Slot 4: `repair_output()` + Repair Loop\]

**Strategy**: 1. Collect feedback from all failed validations 2. Apply programmatic fixes if available (`repair_output()`) 3. If no programmatic fix, regenerate with feedback (REVISE) 4. Re-verify new draft (return to Step 4) 5. Maximum **2 repair attempts** (`MAX_REPAIR_ATTEMPTS = 2`) 6. If repair budget exhausted, proceed with last draft

**Fallback Response Behavior**: The system uses a fallback message for catastrophic failures (ValidationAction.FAIL): "I'm having trouble generating a helpful response right now. Let's pause and try again in a moment." However, when repair attempts are exhausted without catastrophic failure, the system proceeds with the last generated draft rather than the fallback message.

------------------------------------------------------------------------

### Step 6: Deliver \[Final Response Delivery\]

**Implementation**: Implicit in `FrameEngine.ainvoke()` return.

**Activities**: - Send final response to user - Update conversation history - Save persistent frame memory to YAML - Log session data (markdown, YAML, JSON) - Clear ephemeral shared context

------------------------------------------------------------------------

## 5. Frame Abstraction

The frame abstraction defines a common interface that all frames must implement, enabling modular composition of steering behaviors. Each frame can independently contribute to any slot in the pipeline (analyze input, shape prompt, validate output, repair output) without needing to know about other frames. This design allows the Frame Engine to process frames uniformly—regardless of whether a frame enforces turn-taking, tracks comprehension, or validates language appropriateness. New frames can be added to the system simply by implementing this interface, making the architecture extensible without modifying the core engine logic.

### Abstract Frame Interface

**Location**: [`src/backend/frame_engine/frame.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/frame_engine/frame.py)

**Required Property**: - `name` → `str`: Unique identifier for memory namespacing

**Slot Methods** (all optional, default to no-op):

**Slot 1**: `analyze_input(context: FrameContext) → Optional[dict]` - Returns dict to merge into `shared_context`

**Slot 2a**: `get_prompt_sections(context: FrameContext) → list[tuple[str, str]]` - Returns list of (label, content) tuples

**Slot 2b**: `shape_prompt(context: FrameContext, prompt: str) → str` - Returns modified prompt

**Slot 3**: `validate_output(context: FrameContext) → ValidationResult` - Returns `{'action': ValidationAction, 'feedback': Optional[str]}`

**Slot 4**: `repair_output(context: FrameContext) → Optional[str]` - Returns programmatically repaired response or `None`

### Frame Composition

**Marty Deployment** uses 5 frames: 1. `MnemonicCoCreatorFrame` - Primary orchestrator 2. `BalancedTurnsFrame` - Turn-taking management 3. `ComprehensionTrackerFrame` - Understanding tracking 4. `LanguageCheckerFrame` - Age-appropriateness validation 5. `PhasesCheckerFrame` - Phase adherence validation

**Communication**: Frames communicate via: - **Shared Context**: Ephemeral dict for current turn - **Frame Memory**: Persistent dict for session state - **Standard Keys**: Constants avoid hardcoded dependencies

------------------------------------------------------------------------

## 6. State Management

State management controls how information flows through the frame pipeline and persists across conversation turns. The system uses a two-tier memory architecture to separate ephemeral data needed only within a single turn from persistent data that must be maintained throughout the entire session.

### Two-Tier Memory System

#### 6.1 Frame Memory (Persistent)

**Storage**: `FrameContext['frame_memory']`\
**Structure**: `frame_memory[frame_name][key] = value`\
**Lifecycle**: Persists across turns, saved to YAML after each turn\
**Purpose**: Session-long state

**Example**:

``` python
frame_memory = {
    'balanced_turns_validator': {
        'participation': {
            'Alice': {'contribution_count': 5, 'total_speaking_time_seconds': 87.3},
            'Bob': {'contribution_count': 4, 'total_speaking_time_seconds': 62.1}
        },
        'recent_speakers': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob']
    },
    'comprehension_tracker': {
        'concepts': ['GPIO pins', 'PWM', 'I2C'],
        'by_student': {
            'Alice': {
                'GPIO pins': {'level': 'understood', 'justification': '...', 'turn': 3}
            }
        }
    }
}
```

#### 6.2 Shared Context (Ephemeral)

**Storage**: `FrameContext['shared_context']`\
**Structure**: `shared_context[key] = value`\
**Lifecycle**: Cleared after each turn\
**Purpose**: Pass analysis results between frames

**Standard Keys**:

``` python
# From marty.py
SPEAKER_KEY = '_speaker'
CLEANED_MESSAGE_KEY = '_cleaned_message'
SESSION_PHASE_KEY = '_session_phase'

# From balanced_turns.py
SUGGESTED_NEXT_SPEAKER_KEY = '_suggested_next_speaker'
CONSECUTIVE_SAME_SPEAKER_KEY = '_consecutive_same_speaker'

# From comprehension_tracker.py
CONCEPT_ASSESSMENTS_KEY = '_concept_assessments'
```

------------------------------------------------------------------------

## 7. Technology Stack

### Core Framework

-   **Language**: Python 3.11+
-   **Async Orchestration**: LangGraph (state machine for pipeline)
-   **Dependency Management**: Poetry
-   **Type Safety**: TypedDict, Protocol, Enum

### LLM Providers

**Location**: [`src/backend/llm/client.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/llm/client.py)

**Supported**: - Google (Gemini 2.0 Flash, Gemini 2.5 Pro) via `langchain-google-genai` - OpenAI (GPT-4o, GPT-4o-mini) via `langchain-openai` - Azure OpenAI (used in classroom deployment) via `langchain-openai` - Anthropic (Claude Sonnet 4) via `langchain-anthropic`

**Configuration**: Environment variables + YAML config


### Logging

**Three-tier system**: 1. **Markdown** (`.md`): Human-readable transcript 2. **YAML** (`.yaml`): Machine-readable state snapshots 3. **JSON** (`.json`): Full prompts for reproducibility

**Location**: [`src/backend/logging/session_logger.py`](https://github.com/OlgaMuss/BuildBot/blob/main/LLM_Frames_Design/frame_engine_v1.1.2/code/src/backend/logging/session_logger.py)

------------------------------------------------------------------------

## References

**Complete source code**: <https://github.com/OlgaMuss/BuildBot/tree/main/LLM_Frames_Design/frame_engine_v1.1.2>

**Contact**: - Luca Leisten: [luca.leisten\@gess.ethz.ch](mailto:luca.leisten@gess.ethz.ch) - Olga Muss: [olga.muss\@unine.ch](mailto:olga.muss@unine.ch)