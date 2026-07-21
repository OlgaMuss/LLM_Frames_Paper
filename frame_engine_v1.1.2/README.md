# Frame Engine v1.1.2 — Mnemonic Co-Creator (Pilot Implementation)

This directory contains the complete SCAFFOLD implementation used in the classroom pilot study reported in the paper. It includes the runnable Python code, the learning material provided to the LLM and students, the interaction parametrization, and the development context.

## Directory Overview

```
frame_engine_v1.1.2/
├── code/                   # Runnable Python implementation (see code/README.md)
│   ├── src/backend/
│   │   ├── frame_engine/   # Core engine (orchestrator, base classes, LLM client)
│   │   └── frames/         # Five frame definitions used in the pilot
│   ├── simulations/        # Simulation test scripts and output sessions
│   ├── tests/              # Automated test suite (pytest)
│   └── sessions/           # Pre-deployment test session logs
├── context/                # Development context (not needed to run the code)
│   ├── coding_standards/   # Coding conventions used during development
│   └── frame_prototype/    # Early prototype design notes
├── microcontrollers.md     # Learning material provided to students and the LLM
└── variables.md            # Pre-registration variable definitions and session schema
```

---



## Key Files



### `microcontrollers.md`

The learning material on microcontrollers covered in class prior to the pilot. This document was provided verbatim to the LLM as context (to ground responses in curriculum content) and distributed to students as a reference summary.
→ [microcontrollers.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/microcontrollers.md)

### `variables.md`

Defines all variables extracted from SCAFFOLD session logs for the pre-registered analysis, including session metadata, turn-taking metrics, comprehension tracking, and mnemonic progress indicators. Useful for understanding the `.yaml` session log schema.
→ [variables.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/variables.md)

### `code/`

The full Python implementation. See [code/README.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/README.md) for setup and usage instructions.

**Frame definitions** (pilot-specific):


| Frame                 | File                                                                                                                                                    | Role                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Mnemonic CoCreator    | [marty.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/marty.py)                                 | Main pedagogical frame — phases, contributions, prompt shaping |
| Language Checker      | [language_checker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/language_checker.py)           | Age-appropriate language                                       |
| Balanced Turns        | [balanced_turns.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/balanced_turns.py)               | Fair participation across students                             |
| Comprehension Tracker | [comprehension_tracker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/comprehension_tracker.py) | Per-student, per-concept understanding                         |
| Phase Checker         | [phases_checker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/phases_checker.py)               | Phase alignment and pedagogical goals                          |


**Simulation test scripts** (used for pre-deployment testing, S3):


| Item                                                                                                                               | Description                               |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [run_simulation.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/simulations/run_simulation.py) | Main simulation runner                    |
| [simulations/personas/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/simulations/personas)      | Three student personas (Blue, Green, Red) |
| [simulations/sessions/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/simulations/sessions)      | Logs from 13 simulation runs              |




### `context/` *(development only)*

Internal development documents used during implementation. Not required to run or understand the framework.
→ [context/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/context)

---



## Relation to Supplementary Materials


| Supplementary               | Content covered here                                                                                                                                                                                                                                     |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S1 — Framework Architecture | Pipeline implemented in [code/src/backend/frame_engine/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/src/backend/frame_engine)                                                                                       |
| S2 — Frame Implementations  | All five frames in [code/src/backend/frames/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/src/backend/frames)                                                                                                        |
| S3 — Testing                | Simulation scripts in [code/simulations/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/simulations) and tests in [code/tests/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/tests) |
| S6 — Learning Material      | [microcontrollers.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/microcontrollers.md)                                                                                                                                    |


