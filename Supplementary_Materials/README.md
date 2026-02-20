# SCAFFOLD Framework: Supplementary Materials

**Paper Title:** Scaffolding Student-AI Dialogue: A Layered Steering Framework for Safe Educational Interactions

**Authors:** Olga Muss, Luca Leisten, Charles Edouard Bardyn

------------------------------------------------------------------------

## Document Structure

This supplementary material is organized into five technical documents:

### S1: Framework Architecture and Specification

**File**: [S1_Framework_Architecture.md](S1_Framework_Architecture.md)\
**Content**: System architecture, 6-step pipeline, frame abstraction, state management, technology stack\
**Audience**: Developers, technical researchers

### S2: Frame Implementations and Validation

**File**: [S2_Frame_Implementations.md](S2_Frame_Implementations.md)\
**Content**: Detailed specifications for all 5 frames, validation checks (Tables 1 & 2), implementation details\
**Audience**: Developers implementing or extending frames

### S3: Testing 

**File**: [S3_Testing.md](S3_Testing.md)\
**Content**: Three-tier testing strategy (manual, unit tests, simulations)\
**Audience**: Developers, QA engineers

### S4: Classroom Pilot Study - Methods and Materials

**File**: [S4_Classroom_Pilot_Methods.md](S4_Classroom_Pilot_Methods.md)\
**Content**: Study design, participants, procedure, measures, materials (Marty robot, web interface)\
**Audience**: Researchers, paper reviewers, replication studies

### S5: Classroom Pilot Study - Statistical Analysis

**File**: [S5_Pilot_Statistical_Analysis.ipynb](S5_Pilot_Statistical_Analysis.ipynb)\
**Content**: Complete statistical analysis (Python + R), mixed-effects models, visualizations for all 8 findings\
**Audience**: Researchers, statisticians, replication studies\
**Note**: Requires Python 3.9+, R 4.0+, and rpy2 for full execution

------------------------------------------------------------------------

## Quick Navigation

**Understanding the framework** → Start with S1

**Implementing frames** → Read S1, then S2

**Testing** → Read S3

**Replicating the classroom study** → Read S4 (methods) and S5 (statistical analysis)

**Running statistical analyses** → Execute S5 notebook (requires Python + R)

**Running the code** → See repository README for installation and setup

------------------------------------------------------------------------

## Repository

**GitHub**: <https://github.com/OlgaMuss/BuildBot>

**Frame Engine Code**: `LLM_Frames_Design/frame_engine_v1.1.2/code/`

**Directory Structure**:

```         
frame_engine_v1.1.2/
├── code/
│   ├── src/backend/
│   │   ├── frame_engine/      # Core engine
│   │   └── frames/             # Frame implementations
│   ├── tests/                  # Unit tests
│   ├── simulations/            # Synthetic scenarios
│   ├── sessions/               # Logged sessions
│   └── scripts/                # Interactive interface
├── context/                    # Learning material
└── variables.md                # Configuration
```

------------------------------------------------------------------------

## Contact

-   **Luca Leisten**: [luca.leisten\@gess.ethz.ch](mailto:luca.leisten@gess.ethz.ch)
-   **Olga Muss**: [olga.muss\@unine.ch](mailto:olga.muss@unine.ch)