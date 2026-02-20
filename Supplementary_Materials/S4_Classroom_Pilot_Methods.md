# S4: Classroom Pilot Study - Methods and Materials

**SCAFFOLD Framework Supplementary Materials**

------------------------------------------------------------------------

## Table of Contents

1. [Participants](#1-participants)
2. [Procedure](#2-procedure)
3. [Measures](#3-measures)
4. [Materials and Technology](#4-materials-and-technology)

------------------------------------------------------------------------

## 1. Participants

### 1.1 Sample Characteristics

**N**: 27 participants

**Age**: M = 13.46 years (SD = 0.81)

**Gender**: 4 female, 21 male (77.8%), 2 other/not specified

**Grade Level**: 

**School Type**: 

**Prior Experience**: No formal introduction to AI literacy, social robots, programming, microcontrollers or sensors prior to the training

### 1.2 Grouping

**Group Size**: 3-4 students per group

**Number of Groups**: 10 groups (lost data for 1 group)

**Group Assignment**: random

### 1.3 Inclusion/Exclusion Criteria

**Inclusion**:

**Exclusion**:

### 1.4 Ethical Considerations

**Consent**: 

**Data Protection**: 

**Approval**: 

------------------------------------------------------------------------

## 2. Procedure

### 2.1 Session Structure

**Phase 1 (0-3 minutes)**: Knowledge Building
- Students introduce themselves to Marty
- Initial exploration of microcontroller concepts
- Identification of key concepts to include in mnemonic

**Phase 2 (3-9 minutes)**: Mnemonic Co-Creation
- Collaborative creation of mnemonic device (story, poem, or jokes)
- Iterative refinement based on student contributions
- Integration of technical concepts

**Phase 3 (9-10 minutes)**: Practice and Recall
- Students practice reciting the mnemonic
- Recall testing and reinforcement

### 2.2 Interaction Examples

#### 2.2.1 Baseline Condition (Prompt-Only)

XXX. Add example interaction without SCAFFOLD framing

**Characteristics**:
- No explicit turn-taking management
- No age-appropriate language validation
- No phase-specific scaffolding
- No comprehension tracking

#### 2.2.2 Full Framework Condition (SCAFFOLD)

XXX. Add example interaction with complete SCAFFOLD framing

**Characteristics**:
- Balanced turn-taking enforced
- Age-appropriate language validated
- Phase-appropriate scaffolding
- Real-time comprehension tracking
- Targeted support for misconceptions

### 2.3 Data Collection Timeline

**T1 (Pre-session)**:
- Demographic questionnaire
- Pre-test knowledge assessment (2 items)

**T2-T6 (During session)**:
- Real-time conversation logging
- Frame memory snapshots
- Validation and repair logs
- Participation tracking

**T7 (Post-session)**:
- Post-test knowledge assessment (10 items: 2 repeated + 8 new)
- User experience questionnaire
- Qualitative feedback

------------------------------------------------------------------------

## 3. Measures

### 3.1 Knowledge Assessment

**Instrument**: Multiple-choice questionnaire developped by the researchers

**Administration**: 
- T1 (pre-session): 2 items
- T7 (post-session): 10 items (2 repeated from T1 + 8 new)

**Scoring**: Correct/incorrect (1/0 per item)

#### 3.1.1 Repeated Items (T1 and T7)

**Item 1**: What is the main function of this component on the Arduino Nano ESP32?

a) It is the main processor ("brain") that executes the program and gives the board Wi-Fi and Bluetooth capabilities. ✓ (correct)

b) It is the chip that converts the 5V voltage from the USB port for the board.

c) It is a sensor that measures the board's ambient temperature.

d) It is the translator chip that is exclusively responsible for USB communication.

**Item 2**: What is the main role of a microcontroller (like an Arduino) in a robot?

a) To run a specific, relatively simple program, such as controlling motors or reading sensors. ✓ (correct)

b) To run complex Artificial Intelligence, like a Large Language Model (LLM).

c) To move the robot's legs and arms.

d) To provide a software library of pre-made functions for programming.

#### 3.1.2 Additional Items (T7 only)

**8 additional items assessing**:
- XXX. List topics/concepts covered

### 3.2 Co-Creation Level (Participation Balance)

**Metric**: Gini coefficient

**Definition**: Measure of inequality in contribution distribution (0 = perfect equality, 1 = maximum inequality)

**Calculation**: 

$$G = \frac{\sum_{i=1}^{n} \sum_{j=1}^{n} |x_i - x_j|}{2n^2\bar{x}}$$

Where:
- $n$ = number of students in group
- $x_i$ = contribution count for student $i$
- $\bar{x}$ = mean contribution count

**Data Source**: Automated participation tracking from conversation logs

**Operationalization**:
- Contribution count: Number of speaking turns per student
- Speaking time: Estimated from message length
- Balance score: Lower Gini = more balanced participation

### 3.3 User Experience

**Instrument**: Post-session questionnaire (Likert scale)

**Domains**:
- Perceived fairness of participation
- Language appropriateness
- Helpfulness of AI tutor
- Engagement and enjoyment
- Learning experience

**Items**: XXX items, X-point Likert scale

### 3.4 Qualitative Feedback

**Method**: Open-ended questions

**Topics**:
- What did you like about working with Marty?
- What could be improved?
- How did you feel about the turn-taking?
- Was the language easy to understand?

### 3.5 System Logs

**Automated Data Collection**:

1. **Conversation Transcripts** (`.md` files):
   - Complete dialogue with timestamps
   - Speaker identification
   - Turn numbers

2. **Frame Memory Snapshots** (`.yaml` files):
   - Participation tracking per turn
   - Comprehension state per student
   - Phase transitions
   - Session metadata

3. **Validation Logs** (`.json` files):
   - Validation results per check
   - Repair attempts and outcomes
   - Fallback triggers
   - Latency measurements

4. **Prompt Logs** (`.json` files):
   - Full prompts sent to LLM
   - Token counts
   - Model parameters

**Location**: [`sessions/`](https://github.com/OlgaMuss/BuildBot/tree/main/LLM_Frames_Design/frame_engine_v1.1.2/code/sessions)

------------------------------------------------------------------------

## 4. Materials and Technology

### 4.1 Marty the Robot

**Description**: XXX. Short description of Marty robot

**Technical Specifications**:
- Microcontroller: XXX
- Capabilities: XXX
- Sensors: XXX
- Actuators: XXX

**Role in Study**:
- Physical embodiment of AI tutor
- Demonstration platform for microcontroller concepts
- Engagement and motivation tool

### 4.2 Web Interface

**Platform**: XXX. Description of web interface

**Features**:
- XXX
- XXX
- XXX

**Access**: XXX

### 4.3 Learning Materials

**Topic**: Microcontrollers

**Content**: [`microcontrollers.md`](https://github.com/OlgaMuss/BuildBot/tree/main/LLM_Frames_Design/frame_engine_v1.1.2/microcontrollers.md)

**Key Concepts**:
- What is a microcontroller
- Components (CPU, memory, pins)
- Programming (Blockly, C++)
- Applications (robots, IoT devices)
- Examples (ESP32, Arduino Nano)

------------------------------------------------------------------------

## References

**Repository**: <https://github.com/OlgaMuss/BuildBot>

**Frame Engine**: `LLM_Frames_Design/frame_engine_v1.1.2/code/`

**Session Data**: `LLM_Frames_Design/frame_engine_v1.1.2/code/sessions/`

**Contact**: 
- Luca Leisten: [luca.leisten@gess.ethz.ch](mailto:luca.leisten@gess.ethz.ch)
- Olga Muss: [olga.muss@unine.ch](mailto:olga.muss@unine.ch)
