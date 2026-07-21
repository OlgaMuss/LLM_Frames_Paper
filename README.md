# SCAFFOLD: Steered Contextual AI Framework for Orchestrating Learning Dialogue

This repository contains all materials accompanying the paper:

> **Scaffolding Students–AI Dialogue: A Framework for Safe Educational Interactions**
> Olga Muss, Luca M. Leisten, Charles Edouard Bardyn

**Preregistration:** [OSF — 10.17605/OSF.IO/K7UE2](https://doi.org/10.17605/OSF.IO/K7UE2)
**Interactive demo:** [Streamlit simulation app](https://buildbot-4tzkvoxzssupnzkb9e6va4.streamlit.app)
**Repository:** [github.com/OlgaMuss/LLM_Frames_Paper](https://github.com/OlgaMuss/LLM_Frames_Paper)

---

## Repository Structure

### 1. Frame Engine Code

The core pipeline that runs the six SCAFFOLD stages (collect, analyse, shape, verify, repair, deliver):

| Component | Description |
|---|---|
| [frame_engine_v1.1.2/code/src/backend/frame_engine/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/src/backend/frame_engine) | Core engine — abstract base classes, LangGraph orchestrator, LLM client |
| [engine.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frame_engine/engine.py) | Main async pipeline orchestrator |
| [core.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frame_engine/core.py) | Abstract base classes and data structures |
| [llm.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frame_engine/llm.py) | Provider-agnostic LLM client factory |
| [frontend.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/scripts/frontend.py) | Streamlit interactive web UI |
| [code/README.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/README.md) | Full setup and usage instructions |

---

### 2. Frame Definition Files

The five frames used in the pilot (detailed description in [S2](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S2_Frame_Implementations.md)):

| Frame | File | Role |
|---|---|---|
| Mnemonic CoCreator | [marty.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/marty.py) | Main pedagogical frame — session management, phases, contribution analysis |
| Language Checker | [language_checker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/language_checker.py) | Age-appropriate language validation |
| Balanced Turns | [balanced_turns.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/balanced_turns.py) | Fair turn-taking across students |
| Comprehension Tracker | [comprehension_tracker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/comprehension_tracker.py) | Per-student, per-concept understanding profiles |
| Phase Checker | [phases_checker.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/phases_checker.py) | Phase alignment and pedagogical requirements |

All frames: [frame_engine_v1.1.2/code/src/backend/frames/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/src/backend/frames)

---

### 3. System and Constitution Prompts Used in the Pilot

- **Embedded in frame code:** The persona, constitution, and phase-specific instructions are defined directly in [marty.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/src/backend/frames/marty.py) and the other frame files above.
- **Captured in session logs:** Each pilot session log includes a `*_prompts.json` file recording the full prompt sent to the LLM at each turn. Example: [Group 2 prompts](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Data_analysis/Data/LLM_interaction_Data/English/Group%202/session_875f17465356476a90d782013e4841ae_prompts.json)
- **Learning material** provided to both students and the LLM: [microcontrollers.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/microcontrollers.md)
- **Interaction parametrization:** [variables.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/variables.md)

---

### 4. Simulation Test Scripts (S3)

Used to test the framework prior to classroom deployment (described in [S3](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S3_Testing.md)):

| Item | Description |
|---|---|
| [run_simulation.py](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/frame_engine_v1.1.2/code/simulations/run_simulation.py) | Main simulation runner script |
| [simulations/personas/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/simulations/personas) | Three student personas (Blue, Green, Red) used to drive simulations |
| [simulations/sessions/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/simulations/sessions) | Output logs from all simulation runs (sim001–sim013) |
| [code/tests/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/frame_engine_v1.1.2/code/tests) | Automated unit and integration tests (pytest) |
| [S3 Testing Supplementary](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S3_Testing.md) | Description of the testing methodology |

---

### 5. Anonymised Interaction Logs

Student interaction logs from the classroom pilot, pseudonymised and translated to English. Organised by group:

| Folder | Contents |
|---|---|
| [LLM_interaction_Data/English/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/Data_analysis/Data/LLM_interaction_Data/English) | Per-group logs (Groups 1–10): transcripts (`.json`) and SCAFFOLD session logs (`.md`, `.yaml`, `_prompts.json`) |
| [LLM_interaction_Data/German/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/Data_analysis/Data/LLM_interaction_Data/German) | Original German session logs with pseudonyms |
| [S8_LLM Interaction notes.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S8_LLM%20Interaction%20notes.md) | Manual notes on each group's interaction |
| [S9_LLM analysis.csv](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S9_LLM%20analysis.csv) | Coded interaction data (on/off topic, concept proposals, constructive contributions) |

---

## Supplementary Materials

| Document | Link |
|---|---|
| S1 — Framework Architecture | [S1_Framework_Architecture.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S1_Framework_Architecture.md) |
| S2 — Frame Implementations | [S2_Frame_Implementations.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S2_Frame_Implementations.md) |
| S3 — Testing | [S3_Testing.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S3_Testing.md) |
| S4 — Classroom Pilot Methods | [S4_Classroom_Pilot_Methods.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S4_Classroom_Pilot_Methods.md) |
| S5 — Statistical Analysis (v1) | [S5_Pilot_Statistical_Analysis.ipynb](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S5_Pilot_Statistical_Analysis.ipynb) |
| S5 — Statistical Analysis (v2, current) | [S5_Pilot_Statistical_Analysis_v2.ipynb](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S5_Pilot_Statistical_Analysis_v2.ipynb) |
| S6 — Learning Material | [S6_Learning_material.md](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S6_Learning_material.md) |
| S7 — Qualtrics Codebook | [S7_Qualtrics_Codebook.xlsx](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Manuscript/Supplementary_Materials/S7_Qualtrics_Codebook.xlsx) |

## Data

| Dataset | Link |
|---|---|
| Student knowledge and engagement data (T1–T7) | [BuildBots_engagement_children_T1-T7.csv](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Data_analysis/Data/Qualtrics/BuildBots_engagement_children_T1-T7.csv) |
| Coded LLM interaction data | [BuildbotAnalysis - LLM analysis.csv](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Data_analysis/Data/BuildbotAnalysis%20-%20LLM%20analysis.csv) |
| Statistical analysis notebook (Python) | [S5_Pilot_Statistical_Analysis.ipynb](https://github.com/OlgaMuss/LLM_Frames_Paper/blob/main/Data_analysis/S5_Pilot_Statistical_Analysis.ipynb) |
| R analysis scripts (mixed-effects models) | [BuildBots_Rproj/](https://github.com/OlgaMuss/LLM_Frames_Paper/tree/main/Data_analysis/BuildBots_Rproj) |
