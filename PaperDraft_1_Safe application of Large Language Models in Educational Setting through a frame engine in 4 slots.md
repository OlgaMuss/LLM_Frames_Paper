# Safe application of Large Language Models in Educational Setting through Rodin's Four-Slot Frame Engine

*Luca Leisten\** (ETH Zurich)  
*Olga Muss\** (Université de Neuchâtel, ETH Zurich)  
*Charles Edouard Bardyn* (....)

\*These authors contributed equally to this work

# Abstract

….

# 1 Introduction

Generative Artificial Intelligence (AI) in the form of Large Language Models (LLMs) used in AI chatbots has been transformative in the last few years with a rapid adoption of AI chatbots by the general public and particularly young users. According to the 2025 WIP-CH report, teenagers  are the main users of this technology with 84% of swiss 14-19-year-olds regularly using generative AI, compared to only t 60% of 30-49 year olds, and less than 40% of 50-69 year olds [(*WIP-CH*, 2025\)](https://www.zotero.org/google-docs/?FQq5cG). Amongst younger children, 53% of 9-11-year-olds regularly use AI chatbots in the UK in April and May 2025 [(Internet Matters, 2025\)](https://www.zotero.org/google-docs/?4Zyr7R). This is no surprise, since AI chatbots are now present in most apps that childrenyoung people use, such as snapchat, whatsapp, tiktok, or instagram (ref).  
The risks of using LLMs are numerous, from data privacy concerns and unsafe responses to attachment, cognitive atrophy and over-trust ([Neugnot & Muss, 2024, pre-print; Kurian, 2023; 2024; UNESCO, 2021; Viola de Azevedo Cunha, 2017](https://www.zotero.org/google-docs/?Tbs5zS), [Yu et al., 2025, pre-print](https://www.zotero.org/google-docs/?C1FCp5), [Chandra et al., 2025\)](https://www.zotero.org/google-docs/?Cbq2by). While society as a whole needs to address these issues, the educational sector faces specific challenges, as it simultaneously has to educate students about AI technologies and protect them from harm–a duty even more critical when considering that children’s brains are still developing and their skills and knowledge are limited (ref development; ref UNESCO children rights)(). To realize the potential benefits of generative AI tools for education and young people's lives (UNESCO, 2021), we need to ensure that these tools are safe and developmentally adapted to their users.  
There are several methods to achieve this goal and thereby protecting children from harmful AI interactions: (1) ban generative AI tools from schools and restrict their access to over 18 year olds, similarly to what Australia has been doing (ref); (2) allow the use, but regulate the design of these products, a strategy that Europe has been putting in place with the EU AI Act (ref); (3) educate young people about the risks and benefits of AI and teach them how to use it in a beneficial way, a strategy adopted by many grassroot initiatives (ref), or (4) build safer tools or develop mechanisms to adapt current ones. In this paper, we focus on the latter by developing and deploying a new method to control LLM behavior, to increase the safety and pedagogical value of current LLMs. First, we outline the development of this new method and describe the tool. Second, we report preliminary findings of a long-term study, in which we deployed the new method in a social robot in an educational context with 13-15 year olds. The contributions of this paper are:

* XXX  
* XXX  
* XXX  
* Therefore being able to control genAI models’ behaviour is a crucial step towards beneficial outcomes of this wide social transformation.  

# 2 Part 1: A framework for safe LLM interactions

There are several methods to steer language models behavior to comply with a set of requirements, also known as the alignment problem (ref). First, (1) foundational models can be trained in a way to respect a set of instructions by changing the underlying training data, for example through cleaning of the input data, adding new sets of data, and/or by reinforcement learning with human feedback (ref). This is a common approach that can yield very different results depending on how ethical the instructions to the model are (ref). Often these instructions are not transparent, with a few exceptions that focus on ethical AI such as the Swiss Apertus (ref), Olmo3 (ref) and Anthropic with Claude models(ref). Second,  open source models can be fine-tuned, which is usually done for specific narrow tasks (ref). This method is providing more flexibility, but also introduces more heterogeneity, since there are no standards or controls. Third, LLM behavior can be altered through prompt engineering where an instructional prompt is combined with the user’s prompt during the interaction (ref). These instructions are also called AI Constitutions (ref). Most literature about LLM safety explores what prompts would yield better results (ref).   
Importantly, neither of these methods resolve the problem of the intrinsic generative nature of language models, when hallucinations persist and instructions tend to be diluted with the amount of turns in a conversation, leading to less and less compliance of the models to the guidelines (ref). A fourth method, called (4) Post-Hoc Validation, tries to address this issue by implementing a separate program that checks if the output of a model broke any rules. This method is a step in the right direction since it can reject a “bad” draft. However, it cannot influence the initial prompt writing process, thus limiting  its suitability for safe and efficient dynamic interactions with users. We propose a new open-source method, which we call Rodin's Four-Slot Frame Engine, that assesses the user’s input, shapes and generates a draft response, checks its validity and regenerates a promptanswer with a repair if needed. By incorporating checks and repairs in prompt generation, we offer the first method that allows forto systematically solve safe and dynamic interactions with language models. In the following, we describes the concept and development of an LLM frame, followed by how we deployed a frame in an educational setting with children aged 13-15.

## 2.1  Rodin's Four-Slot Frame Engine

The idea of Rodin’s Frame Engine starts with accepting that a much finer control of LLM inputs and outputs is needed to increase reliability at a level necessary to allow for schools but also any other context focused on learning or beneficial interactions to introduce this technology and harvest its potential while managing the risks. It also recognises that a large community of interdisciplinary and international stakeholders is needed to improve the odds of having  beneficial AI that can be safely used in educational contexts. Rodin’s Frame Engine as a method has been pre-patented (see supplemental material), to preserve the right to publish the frames open-source, making them freely available to anyone, so a community can develop and build upon these ideas. 

The Rodin architecture provides a robust, modular, and efficient solution by breaking the process of text/speech generation into distinct, composable stages. It consists of adding a modular layer of coding that could work with different language models and in different contexts using external memory and a system of checks at different stages of the generation process. By defining the context, the related information and the process to follow, the interaction can be, for example, an AI assistant for brainstorming solutions in a stem project, a socratic seminar assistant in history, a math tutor for homework, a creative writing assistant in a second language class or an AI-student co-thinking exercise to learn to efficiently communicate with AI in civics class. The possibilities are many.

## 2.2 Description of the Rodin’s frame engine

The four-slots of Rodin’s frame engine are (1) input analysis, (2) prompt shaping, (3) draft generation, (4) response assessment, repair and validation. 

In v1.1.2, each slot is implemented by several specialized frames orchestrated by the frame engine using LangGraph for state management. The main pedagogical frame (`MnemonicCoCreatorFrame`, nicknamed "Marty") manages the learning flow, session phases, and mnemonic creation. Four supporting frames provide modular functionality:

1. **BalancedTurnsFrame**: Manages fair turn-taking across students, tracking participation count, speaking time, and consecutive turns
2. **ComprehensionTrackerFrame**: Maintains per-student, per-concept understanding profiles, tracking whether each student understands, is confused about, or has misconceptions regarding specific concepts
3. **LanguageCheckerFrame**: Validates age-appropriate language, tone, and complexity of responses
4. **PhasesCheckerFrame**: Ensures responses align with the current session phase goals and pedagogical requirements

These frames communicate via a `shared_context` dictionary for ephemeral data within a turn and a `frame_memory` dictionary for persistent state across turns. Each frame contributes labeled prompt sections using the `get_prompt_sections()` method, which the engine assembles into a single system prompt. Frames can also optionally transform the assembled prompt using the `shape_prompt()` method for final adjustments.

| Slot | Purpose | Advantage over Other Methods |
| :---- | :---- | :---- |
| **1\. Analyze Input** | React to the user's state before generation. | A static "Constitution" cannot dynamically adapt its rules based on whether the user is frustrated, confused, or excited. This slot allows the system to gather crucial metadata first. |
| **2\. Shape Prompt** | Build the instructions dynamically and modularly through two phases. | Phase 2a: Each frame contributes labeled `PromptSection` objects that are accumulated. Phase 2b: Frames can optionally transform the assembled prompt. This separation enables both additive contributions and final transformations, ideal for community contributions. |
| **3\. Generate** | Create the initial response from the tailored prompt. | The generation is more likely to be on-track from the start because the prompt was shaped with context-specific rules and user analysis. |
| **4\. Validate & Repair** | Provide targeted feedback in a loop. | This is far more powerful than simple rejection. The \`REVISE\` action tells the LLM \*what was wrong\* and asks for a targeted fix, which is much faster than a full restart. The \`FIX\` action allows for fast, programmatic repairs. |

##### Table 1\. Description of the four-slot

The process of creating a frame engine begins with defining the inputs to the first slot. This can be categorized as (1) user information (name or nickname, age, language, etc.), (2) parameters of the interaction, and (3) the user’s prompt.   
![][image1]

##### Figure 1\. Overview of the four-slot process for one turn

The definition of the interaction – parameters of the interaction, which we also call dialogue contract – can be approached in a nested and combinatory way and it can be defined by: 

- Setting of the interaction such as the type of school, or class or a type of a museum or another setting such as a camp or a home.   
- Location such as the country and region (to take into account cultural specificities) and preferred language  
- Goal of the interaction  
- Description of the interaction   
- Interlocutors, such as the students age group, or several age groups in the case of multi-user interactions with corresponding roles (or persona for the AI agent) (an interaction might not require AI to intervene, but just observe)  
- Desired output  
- What needs to be monitored (safeguards, turns, level of understanding, etc.)

![][image2]

##### Figure 2\. Potential elements of a parametrization of an interaction

The interaction can be defined in a generic way and be suitable in many situations or it can be very specific to a certain use-case. Most of these parameters can be defined either as a freely formatted prompt or the users can be guided through a set of choices. The exception is the monitoring that requires more background definition and testing, which, once developed (ideally by the open-source community), can be added to the toolbox of the frames in a modular way.   
The first slot, input analysis, is a crucial and game-changing aspect of the frame. It allows (1) to assess different levels of risks and trigger safety measures that are difficult to put in place otherwise: for example, sending an alert to a teacher when a student insists at misusing the tool or when a student is expressing dark thoughts, but also to trigger meta-responses when the user goes off topic. Another advantage of an input analysis is to (2) be able to manage interactions in a specifically designed way, such as to engage the user’s cognitive processes instead of performing them for the user. This is particularly relevant in educational settings when students focus on delivering outcomes, underestimating the learning process. Management of an interaction is crucial and essential in multi-user interaction, a common situation in education, which requires to track participants’ turns and contributions. Moreover, input analysis allows (3) to perform analysis that can be used to improve the interaction in real time or to analyse the interaction afterwards. Examples of analysis can be the user's understanding of the content, progress towards a goal, level of critical thinking, level of engagement or of fatigue. Some analysis can be quite simple and straightforward, such as the level of distraction from the topic, while others analysis could be much more complex and require expert validation such as in the case of detecting learning difficulties or mental health problems. In this last case, a committee of experts should contribute to the development of the analysis.    
 Input analysis can be done using a combination of methods: (1) a lighter or a specialized LLM can be used to assess alignment to an instruction, for example if the question is on the topic, (2) coding can be used in specific instances such as interaction time monitoring, or user’s turn counting.   
![][image3]   
![][image4]

##### Figure 3\. Potential elements of the slot 1 \- Input Analysis 

The second slot consists in shaping the prompt in a way to take into account (1) a constitution which integrates safeguards as prompts, (2) the context of the interaction – parametrisation –  with information from parametrization of the interaction and user information, (3) the results of the input analysis, and also (4) the feedback from the slot 4 if the drafted response haven’t passed all validations and needs repair.   
![][image5]

##### Figure 4\. Potential elements of the slot 2 \- Shape Prompt 

Third slot consists in the generation of a drafted response by a Large Language Model. When the model is used in real time interaction with AI speed might become a crucial factor in deciding which model to use, while for offline analysis or when the interaction is only monitored, a more heavy model might be more appropriate.  
The last slot is validation and repair, which starts with assessing the response and runs validation checks. If those are not passed the slot creates a repair procedure and initiates the slot 2 \- shape the prompt. The number of rounds of repair is a variable and when reached the system will generate a predefined error message.   
![][image6]

##### Figure 5\. Potential elements of response assessment in the slot 4 \- Validate and Repair  

### 2.2.1 Inter-Frame Communication via Shared Context

V1.1.2 uses well-defined keys for inter-frame communication in the `shared_context` dictionary. This avoids hardcoding frame names and enables frames to be reused across different dialogue configurations:

**Keys defined by MnemonicCoCreatorFrame:**
- `CLEANED_MESSAGE_KEY` (`'_cleaned_message'`): The parsed user message (speaker prefix removed)
- `SPEAKER_KEY` (`'_speaker'`): The identified speaker's name
- `SESSION_PHASE_KEY` (`'_session_phase'`): Current phase (1, 2, or 3)
- `PHASE_INSTRUCTIONS_KEY` (`'_phase_instructions'`): Current phase instructions for validators
- `MNEMONIC_STATE_KEY` (`'mnemonic_state'`): Mnemonic creation state (in frame_memory)

**Keys defined by BalancedTurnsFrame:**
- `SUGGESTED_NEXT_SPEAKER_KEY` (`'_suggested_next_speaker'`): Who should speak next for balance
- `CONSECUTIVE_SAME_SPEAKER_KEY` (`'_consecutive_same_speaker'`): Monopolization counter

**Keys defined by ComprehensionTrackerFrame:**
- `CONCEPT_ASSESSMENTS_KEY` (`'_concept_assessments'`): Cumulative per-student, per-concept profiles
- `PER_TURN_COMPREHENSION_KEY` (`'_per_turn_comprehension'`): What was understood/confused this turn

This key-based architecture allows frames to be composed flexibly. For example, the `BalancedTurnsFrame` could be reused in any multi-student dialogue system by having the main frame populate `SPEAKER_KEY` in the shared context.

## 2.2.2 Orchestration Architecture: LangGraph State Machine

V1.1.2 uses LangGraph to implement the four-slot pipeline as an asynchronous state machine. This provides:

**State Management:**
- The `FrameContext` TypedDict serves as the state object
- LangGraph ensures immutable state transitions
- Each node receives the current state and returns an updated version

**Graph Structure:**
```
analyze_input → shape_prompt → generate_response → validate_output
                                                          ↓
                                    (if validation fails) → repair_output
                                                          ↓
                                    (REVISE: regenerate) → generate_response
                                    (FIX: re-validate)   → validate_output
                                    (FAIL: abort)        → END
                                    (max attempts)       → END
```

**Conditional Edges:**
The engine uses conditional logic to determine the next step after validation:
- All validations PASS → END (success)
- Any validation FAIL → END (abort with fallback response)
- Any validation REVISE/FIX + attempts < 2 → repair_output
- Max repair attempts reached → END (accept current draft)

**Concurrency:**
- All frames' `analyze_input()` methods run sequentially (to preserve dependencies)
- All frames' `validate_output()` methods run concurrently via `asyncio.gather()` (for speed)
- Repair actions for FIX run concurrently if multiple frames request it

**Benefits:**
- Clear, debuggable execution flow
- Deterministic state transitions
- Easier to add/remove frames without breaking the pipeline
- Built-in support for loops (repair cycles)
- Async-first design for optimal performance with LLM calls

## 2.3 Memory Management and Session Logging

V1.1.2 implements a dual-memory architecture:

**1. Frame Memory (`frame_memory`):**
Persistent state that survives across turns within a session. Two patterns coexist:

- **Root-level memory**: The main `MnemonicCoCreatorFrame` writes directly to the root of `frame_memory` (e.g., `frame_memory['turn_count']`, `frame_memory['mnemonic_state']`). This design allows easy access to core session state.
  
- **Namespaced memory**: Supporting frames write to their own namespace (e.g., `frame_memory['balanced_turns_validator']`, `frame_memory['comprehension_tracker']`). This prevents naming collisions and enables clean modularization.

Critical state stored in frame memory includes:
- Turn count, session phase, elapsed time
- Mnemonic creation state (selected concepts, current draft, finalization status, quality validation)
- Participation tracking (per-student contribution counts, speaking times, recent speakers)
- Comprehension profiles (per-student, per-concept understanding levels)
- Recall tracking (per-student attempts, successful parts, stuck points)

**2. Shared Context (`shared_context`):**
Ephemeral state that only exists for a single turn. Frames use this for intra-turn communication:
- Cleaned message and speaker identification
- Current session phase
- Per-turn comprehension analysis
- Next speaker suggestions
- Phase instructions for validators

Shared context is reset at the start of each turn, while frame memory persists throughout the session.

**3. Session Logging:**
V1.1.2 includes a comprehensive `SessionLogger` that creates three output files per session:

- **YAML log** (`session_ID.yaml`): Complete event log with metadata, all frame outputs, and final frame memory
- **Markdown report** (`session_ID.md`): Human-readable summary including participation statistics, comprehension summary, selected concepts, created mnemonic, and full conversation log with per-turn comprehension analysis
- **Prompts JSON** (`session_ID_prompts.json`): Complete system prompts and LLM responses for debugging content filters

**Privacy and Transparency Considerations:**
The frame memory can optionally be cleared between sessions to ensure no persistent tracking across interactions. For educational deployments, monitoring can increase learning through improved teacher attention allocation [(Holstein et al., 2018)](https://www.zotero.org/google-docs/?ZaoWAE) and pro-social behavior, but may also increase anxiety [(Cañigueral & Hamilton, 2019)](https://www.zotero.org/google-docs/?sj7eF9). 

Implementations should:
- Clearly inform students about what data is being tracked
- Provide transparency about who can access the logs
- Allow students/teachers to opt out of persistent logging
- Limit monitoring to cases with clear educational benefits
- Make session logs available to students for self-reflection 

# 3\. Part 2: Application of the framing in a school setting

To test Rodin's Four-Slot Frame Engine, we designed and tested a minimal framing in the context of an experiment in social robotics in an educational setting which we call BuildBots. Buildbots' experimental condition is a 7 weeks, 3 hours per week intervention in 2 stem classrooms of 14 and 15 year olds in Germany. During this intervention, students, in groups of 3 or 4 build a social robot, in particular Marty robot from [Robotical.io](http://Robotical.io), learn about Artificial Intelligence, Large Language Models, social robots, programming, microcontrollers and sensors. As part of the AI literacy curriculum, students experiment with safeguards and design a learning interaction with Marty which has been equipped with a voice interaction module. During the last session, students work in groups of 3 or 4 to create a mnemonic (a poem, a story or a few jokes) about microcontrollers with the support of Marty's AI. They first try to do that without Rodin's framing – just with prompting, and then try with the framing. All code and testing sessions for v1.1.2 are available in the project repository (frame_engine_v1.1.2 directory). 

## 3.1 Description of Marty’s framing

The goal of the frame is to set up an interaction where 3 or 4 students of 14 or 15 years of age consolidate their knowledge about a topic covered in class. We settled on microcontrollers which is a major topic for the class’s curriculum, but the topic is a variable and can be easily changed. The AI model impersonates "Marty," a friendly and encouraging buddy robot who helps students learn together. The interaction is set to last about 10 minutes with the structure described below. 

#### SESSION STRUCTURE

V1.1.2 implements automatic time-based phase transitions:

**PHASE 1: MINUTES 0-3 - Concept Selection**  
- Marty asks open-ended questions to elicit student-selected concepts
- Students propose and discuss which concepts are most important to remember
- **Critical rule**: Marty MUST NOT propose concepts; only students suggest them
- Group collaboratively selects 3-5 key concepts for the mnemonic
- Phase automatically transitions at 3 minutes elapsed time

**PHASE 2: MINUTES 3-7 - Co-Create the Mnemonic (THE CORE)**  
- Students collaborate to build the chosen mnemonic type (Story, Poem, or Jokes - decided pre-session)
- Marty facilitates by asking students to contribute ideas
- **Regular narration**: Marty recites the mnemonic draft every 1-3 contributions to scaffold memory
- Incremental building: Each student contribution updates the mnemonic draft
- **Quality validation**: Once substantial, the draft is checked for length, structure, and concept coverage
- **Phase extension**: If 7 minutes pass without a quality mnemonic, Phase 2 extends until 10 minutes
- Phase automatically transitions at 7 minutes (or 10 minutes if extension needed)

**PHASE 3: MINUTES 7-10 - Recall Practice**  
- Only enters if a quality mnemonic exists
- **First turn**: Marty recites the complete mnemonic to students
- Students practice recalling the mnemonic from memory
- Marty provides hints if students get stuck
- Students help each other remember
- **Redirect off-topic**: If students try to modify the mnemonic, Marty redirects to recall practice
- Phase ends at 10 minutes elapsed time

**CLOSURE: MINUTE 10+ - Wrap-Up**  
- Automatic closure mode triggered at 10 minutes
- Marty thanks all students by name
- Celebrates what was accomplished (selected concepts, created mnemonic)
- Encourages continued practice
- Validation frames pass automatically during closure to allow wrap-up    
The minimum checks that we considered necessary were (1) managing turns, (2) managing speaking time, (3) checking understanding, (4) staying on topic. We also added a few other checks that seemed relevant and which are described below.

It is important to note that ideally the interaction would imply minimal input from Marty’s AI, where students work out the mnemonic as autonomously as possible. This would mean that several students might speak one after another, with no intervention from Marty. While this is very possible with Rodin's frame – we tested that in the prototype version – we were not able to implement it with the students for technical reasons at robotical.ai and the interaction was left as back and forth between a student and Marty.  

#### Frames

V1.1.2 implements five frames that work together in a modular architecture:

**Main Pedagogical Frame:**
1. **MnemonicCoCreatorFrame** (`marty.py`): Manages the complete learning session including:
   - Three distinct phases with time-based transitions (Phase 1: Concept Selection 0-3 min, Phase 2: Mnemonic Creation 3-7 min, Phase 3: Recall Practice 7-10 min)
   - LLM-powered analysis of student contributions to classify contribution type, assess relevance, and track mnemonic progress
   - Dynamic mnemonic building that incrementally updates the story/poem/jokes as students contribute
   - Mnemonic quality validation before transitioning to recall practice
   - Language detection to support multilingual sessions
   - Session closure management when time limit is reached

**Supporting Frames:**
2. **BalancedTurnsFrame** (`balanced_turns.py`): Ensures equitable participation by:
   - Tracking each student's contribution count, speaking time, and recent speaking history
   - Suggesting the next speaker to maintain balance
   - Validating that Marty follows turn-taking suggestions (acknowledgment before invitation)
   - Detecting and preventing conversation monopolization

3. **ComprehensionTrackerFrame** (`comprehension_tracker.py`): Monitors student understanding by:
   - Extracting key concepts from learning material (or using student-selected concepts)
   - Maintaining per-student, per-concept comprehension profiles (understood, confused, misconception, not_seen)
   - Performing dual analysis: cumulative assessment for long-term tracking and per-turn analysis for immediate feedback
   - Sharing comprehension insights with other frames via shared context

4. **LanguageCheckerFrame** (`language_checker.py`): Validates response appropriateness by:
   - Checking language complexity and simplicity for the target age (14 years)
   - Ensuring friendly, encouraging tone (not condescending)
   - Allowing technical terms from the learning material and student-selected concepts
   - Using LLM-based validation with concrete examples of acceptable language

5. **PhasesCheckerFrame** (`phases_checker.py`): Enforces phase-specific goals by:
   - Validating that responses align with the current phase's pedagogical objectives
   - Checking that Marty follows phase-specific instructions (e.g., not proposing concepts in Phase 1, narrating progress in Phase 2, focusing on recall in Phase 3)
   - Providing specific feedback for revision when responses drift from phase goals

All frames implement the abstract `Frame` base class with four core methods: `analyze_input()` (Slot 1), `get_prompt_sections()` and `shape_prompt()` (Slot 2), and `validate_output()` (Slot 4). The `FrameEngine` orchestrates these frames using LangGraph to create a state machine that executes the four-slot pipeline for each turn.

#### Parameters of the interaction

The parameters describe the interaction assigning the AI assistant a persona (see figure 6 for the details), the language of the interaction, the learning material which is provided through a file, the names and age of the interlocutors, the structure of the interaction and desired outputs.    
![][image7]

##### Figure 6: Marty’s interaction parameters

#### Slot 1 - Input Analysis

In v1.1.2, input analysis is distributed across frames, each contributing specialized assessments:

**MnemonicCoCreatorFrame analyzes:**
- **Turn count and session phase**: Time-based transitions (0-3min=Phase 1, 3-7min=Phase 2, 7-10min=Phase 3, 10min+=Closure)
- **Language detection**: First turn only, to support multilingual sessions (detects German, English, etc.)
- **Contribution type** via LLM analysis:
  - Phases 1-2: "mnemonic_suggestion", "knowledge_statement", "question", "builds_on_idea", "off_topic"
  - Phase 3: "recall_attempt", "recall_question", "off_topic"
- **Relevance assessment**: Tracks consecutive off-topic turns
- **Mnemonic progress**: Summarizes current state of co-creation
- **Incremental mnemonic building**: Updates draft as students contribute (Phase 2)
- **Mnemonic quality validation**: Checks length, structure, and concept coverage before Phase 3
- **Phase-specific state**: Tracks concept selection (Phase 1), mnemonic creation (Phase 2), recall attempts (Phase 3)

**BalancedTurnsFrame analyzes:**
- **Recent speaker history**: Last 5 speakers to detect patterns
- **Per-student participation**: Contribution count and estimated speaking time (based on message length)
- **Consecutive same-speaker detection**: Identifies monopolization
- **Next speaker suggestion**: Recommends who should speak next for balanced participation

**ComprehensionTrackerFrame analyzes:**
- **Cumulative per-student, per-concept profiles**: Tracks understanding levels (understood, confused, misconception, not_seen)
- **Per-turn comprehension**: Identifies what concepts were understood or confused in this specific message
- **Concept extraction**: Uses student-selected concepts once Phase 1 completes

The validation frames (LanguageChecker, PhasesChecker) do not perform input analysis—they only validate outputs in Slot 4.

The section below reports the actual LLM-based analysis instructions: 

\*\*ANALYSIS TASK:\*\*  
Analyze the student's message and provide the following in a JSON object:  
1\.  \`contribution\_type\`: Classify the message. Choose one: "mnemonic\_suggestion", "knowledge\_statement", "question", "builds\_on\_idea", "off\_topic".  
2\.  \`is\_relevant\`: A boolean (\`true\` or \`false\`) indicating if the message is relevant to the topic or task.  
3\.  \`mnemonic\_progress\`: A brief, one-sentence summary of the current state of the co-created mnemonic.  
4\.  \`summary\`: A one-sentence summary of the student's message.  

During slot 1, turns are updated and the next speaker is suggested based on a combination of recent speakers, number of contributions, and approximate speaking time: the frame keeps a short history of who spoke when and for how long (estimated from message length) and identifies under-participating students who have contributed significantly less or spoken less than their peers.   
![][image8]

##### Figure 7: Input analysis for Marty’s frame

#### Slot 2 - Shape Prompt

Slot 2 in v1.1.2 is implemented as a two-phase process:

**Phase 2a - Section Accumulation (`get_prompt_sections`):**
Each frame contributes labeled `PromptSection` objects that are accumulated by the engine:

1. **MnemonicCoCreatorFrame** contributes:
   - "Marty - Persona & Knowledge": Core role, language requirements, learning material, and age-appropriate guidance
   - "Marty - Phase X Instructions": Dynamic, phase-specific pedagogical guidance including:
     - Phase 1: Open-ended questions to elicit student-selected concepts (explicitly forbids Marty from proposing concepts)
     - Phase 2: Facilitation of collaborative mnemonic creation with regular narration of progress
     - Phase 3: Recall practice with hints and peer support
   - "Marty - Redirection": Off-topic redirection guidance (only when off_topic_duration >= 2)
   - Shares phase instructions via `PHASE_INSTRUCTIONS_KEY` in shared context for validator frames

2. **BalancedTurnsFrame** contributes:
   - "Balanced Turns Guidance": Explicit instructions to acknowledge the previous speaker by name and invite the suggested next speaker, with emphasis when consecutive turns by same speaker >= 2

3. **ComprehensionTrackerFrame** contributes:
   - "Comprehension Tracker - Concepts to Clarify": Lists concepts where students showed confusion or misconceptions, with student names and justifications
   - "Comprehension Tracker - Concepts Already Understood": Lists concepts to avoid over-explaining

**Phase 2b - Prompt Transformation (`shape_prompt`):**
After accumulation, each frame can optionally transform the assembled system prompt. In v1.1.2, most frames do not use this capability, relying instead on section contribution for clean, modular composition.

**Assembly Process:**
The `FrameEngine` assembles sections by concatenating them with double newlines. An optional `include_section_labels` flag adds `[Label]` markers for debugging, though this is disabled by default to save tokens.

**Repair Integration:**
When validation fails with a `REVISE` action in Slot 4, the engine appends repair feedback to the system prompt and regenerates the response. This creates a feedback loop: Shape Prompt → Generate → Validate → (if REVISE) → Update System Prompt → Generate again.       
![][image9]

##### Figure 8: Shape prompt elements of Marty’s frame

#### Slot 3 - Generate Response

In Slot 3, the `FrameEngine` constructs a message sequence and invokes the LLM:

1. **Message Construction:**
   - System message with the assembled prompt from Slot 2
   - Conversation history (previous user/assistant messages from `conversation_history`)
   - Current user message (using cleaned message from `shared_context[CLEANED_MESSAGE_KEY]` if available)

2. **LLM Invocation:**
   The engine calls `await llm_client.ainvoke(messages)` and stores the result in `llm_draft_response`.

3. **Response Parsing:**
   The engine handles various response formats (string, AIMessage, multimodal content) via the `_parse_llm_response()` helper.

4. **Prompt Logging:**
   For debugging content filter issues, the `SessionLogger` records each prompt/response pair to a JSON file (`session_ID_prompts.json`), including the full system prompt, conversation history, and LLM draft.

**Provider Configuration:**
V1.1.2 is provider-agnostic through the `get_llm_client()` factory in `llm.py`. Configuration is managed via `config.yaml`:

```yaml
llm:
  provider: "google"  # Options: "google", "openai", "anthropic"
  model_name: "gemini-2.5-flash-lite"
  temperature: 0.7  # Optional
```

**Supported Models:**
- **Google Gemini**: `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-2.5-pro`
- **OpenAI**: `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`
- **Anthropic**: `claude-sonnet-4-20250514`, `claude-3-5-haiku-20241022`

For our empirical study, we use Google's Gemini 2.5 flash-lite, which achieves sub-second response times in our testing environment.

#### Slot 4 - Validation and Repair

Slot 4 in v1.1.2 orchestrates validation across multiple frames and manages a sophisticated repair loop:

**Validation Phase (`_validate_output_node`):**
The engine runs validation concurrently for all frames using `asyncio.gather()` for efficiency. Each frame returns a `ValidationResult` with an action (`PASS`, `FIX`, `REVISE`, `FAIL`) and optional feedback.

**Frame-Specific Validation:**

1. **BalancedTurnsFrame** validates turn-taking:
   - Checks that Marty acknowledged the previous speaker by name
   - Verifies that Marty invited the suggested next speaker (when participation is unbalanced)
   - Validates speaker ordering (acknowledgment must come before invitation)
   - Detects incorrect student names being mentioned
   - Returns `REVISE` with specific feedback if turn-taking rules are violated
   - Passes validation during closure mode to allow final wrap-up messages

2. **ComprehensionTrackerFrame**:
   - Does not implement output validation (no checks in Slot 4)
   - Only contributes to Slot 1 (analysis) and Slot 2 (prompt guidance)

3. **LanguageCheckerFrame** validates age-appropriateness:
   - Uses LLM to check if language is suitable for target age (14 years)
   - Validates tone is friendly and encouraging (not condescending)
   - Allows technical terms from learning material and selected concepts
   - Provides lesson context to avoid false positives on domain-specific vocabulary
   - Returns `REVISE` if language is too complex or tone is inappropriate
   - Example validation check:
     ```
     Check whether the RESPONSE is suitable for a 14-year-old:
     keep sentences short (1-5 clauses), friendly, encouraging, and free of emojis.
     
     CONTEXT ABOUT TODAY'S LESSON (acceptable technical terms):
     {lesson_context}
     
     Currently selected lesson concepts (always allowed to mention):
     {selected_concepts}
     ```

4. **PhasesCheckerFrame** validates phase alignment:
   - Uses LLM to check if response follows phase-specific instructions
   - Validates tone, phase goal adherence, and complexity matching student understanding
   - Receives the exact phase instructions from shared context via `PHASE_INSTRUCTIONS_KEY`
   - Allows narrations and recaps that help scaffold learning
   - Returns `REVISE` with specific required adjustments if response drifts from phase goals
   - Passes validation during closure mode
   - Example validation checks:
     - Phase 1: Did Marty propose concepts instead of asking students?
     - Phase 2: Did Marty narrate progress? Did Marty facilitate rather than create?
     - Phase 3: Did Marty focus on recall testing? Did Marty redirect off-topic contributions?

5. **MnemonicCoCreatorFrame**:
   - Validation is deprecated (returns `PASS` by default)
   - Historical validation logic has been distributed to specialized frames
   - Relies on `REVISE` action from other frames rather than implementing programmatic fixes

**Validation Decision Logic:**
After all frames complete validation, the engine decides the next step:
- **All PASS**: Turn completes successfully
- **Any FAIL**: Abort turn immediately, use fallback response
- **Any REVISE or FIX** (and attempts < MAX_REPAIR_ATTEMPTS=2): Proceed to repair
- **Max attempts reached**: Accept current draft and finish

**Repair Phase (`_repair_output_node`):**
The engine handles two types of repairs:

1. **FIX Action** (Programmatic Repair):
   - Frame's `repair_output()` method directly modifies `llm_draft_response`
   - Used for deterministic, rule-based corrections
   - After repair, engine re-runs validation on the fixed draft
   - Not currently used by any frame in v1.1.2

2. **REVISE Action** (LLM Regeneration):
   - Engine collects feedback from all failing frames
   - Appends consolidated feedback to the system prompt
   - Regenerates a new response via Slot 3
   - Example feedback format:
     ```
     The previous response was not suitable. Please revise it based on the following feedback:
     - From frame 'balanced_turns_validator': You mentioned Green before Red. Structure: 1) First acknowledge Red. 2) Then ask Green a question.
     - From frame 'language_checker_frame': The language was not appropriate for a 14-year-old. Please simplify your wording.
     ```

**Closure Mode Handling:**
When `frame_memory['_closure_ready']` is True (elapsed time >= 10 minutes), validation frames pass automatically to allow Marty to deliver a final wrap-up message that may deviate from normal phase rules.

**Fallback Response:**
If validation fails catastrophically (`FAIL` action), the engine returns a safe, generic message:
```
"I'm having trouble generating a helpful response right now. Let's pause and try again in a moment."
```

#### ![][image10]

##### Figure 9: Output validation of Marty frame

#### Memory

V1.1.2 stores session data in three formats:
- **YAML log** (`session_ID.yaml`): Complete event log with all frame outputs and final frame memory
- **Markdown report** (`session_ID.md`): Human-readable summary with participation statistics, comprehension profiles, selected concepts, created mnemonic, and full conversation log
- **Prompts JSON** (`session_ID_prompts.json`): All system prompts and LLM responses for debugging

See Section 2.3 for detailed memory architecture (frame_memory and shared_context). 

#### Testing

V1.1.2 includes comprehensive testing infrastructure:

**Interactive Interface:**
A Streamlit-based web interface allows real-time testing with live LLM calls. The interface displays:
- Real-time conversation with Marty
- Session phase indicators
- Participation statistics
- Comprehension tracking status

**Automated Testing:**
- **Unit tests** (`tests/` directory): Validate individual frame behavior with real LLM calls (no mocking)
- **Simulation framework** (`simulations/` directory): AI-generated student personas (Red, Blue, Green) with distinct behavioral profiles enable automated testing of complete 10-minute sessions
- **Session analysis**: All simulation outputs are logged for analysis, including edge cases like monopolization, off-topic drift, and concept confusion

**Test Coverage:**
- Individual frame tests: `test_marty.py`, `test_balanced_turns.py`, `test_comprehension_tracker.py`, `test_language_checker.py`, `test_phases_checker.py`
- Engine orchestration: `test_engine.py`
- Provider configuration: `test_llm.py`

### 3.1 Implementation in the class

#### To be done 

# 4\. Conclusion

…  
Learning points  
Limitations   
Further work needed  
On going projects

# References

[Cañigueral, R., & Hamilton, A. F. de C. (2019). Being watched: Effects of an audience on eye gaze and prosocial behaviour. *Acta Psychologica*, *195*, 50–63. https://doi.org/10.1016/j.actpsy.2019.02.002](https://www.zotero.org/google-docs/?jJTdPT)   
[Chandra, M., Naik, S., Ford, D., Okoli, E., Choudhury, M. D., Ershadi, M., Ramos, G., Hernandez, J., Bhattacharjee, A., Warreth, S., & Suh, J. (2025). *From Lived Experience to Insight: Unpacking the Psychological Risks of Using AI Conversational Agents* (No. arXiv:2412.07951). arXiv. https://doi.org/10.48550/arXiv.2412.07951](https://www.zotero.org/google-docs/?jJTdPT)   
[*ECREA \- World Internet Project – Switzerland 2025 (WIP-CH): Reports*. (2025). https://ecrea.eu/page-18206/13561816](https://www.zotero.org/google-docs/?jJTdPT)   
[Holstein, K., McLaren, B. M., & Aleven, V. (2018). Student Learning Benefits of a Mixed-Reality Teacher Awareness Tool in AI-Enhanced Classrooms. In C. Penstein Rosé, R. Martínez-Maldonado, H. U. Hoppe, R. Luckin, M. Mavrikis, K. Porayska-Pomsta, B. McLaren, & B. du Boulay (Eds.), *Artificial Intelligence in Education* (pp. 154–168). Springer International Publishing. https://doi.org/10.1007/978-3-319-93843-1\_12](https://www.zotero.org/google-docs/?jJTdPT)   
[*Me, Myself and AI research Understanding and safeguarding children’s use of AI chatbots*. (2025). internetmatters.org. https://www.internetmatters.org/hub/research/me-myself-and-ai-chatbot-research/](https://www.zotero.org/google-docs/?jJTdPT)   
[Neugnot-Cerioli, M., & Muss Laurenty, O. (2024). *The Future of Child Development in the AI Era. Cross-Disciplinary Perspectives Between AI and Child Development Experts* (No. arXiv:2405.19275). arXiv. https://doi.org/10.48550/arXiv.2405.19275](https://www.zotero.org/google-docs/?jJTdPT)   
[Yu, Y., Liu, Y., Zhang, J., Huang, Y., & Wang, Y. (2025). *Understanding Generative AI Risks for Youth: A Taxonomy Based on Empirical Data* (No. arXiv:2502.16383). arXiv. https://doi.org/10.48550/arXiv.2502.16383](https://www.zotero.org/google-docs/?jJTdPT) 

# Annexes

### Patent with figures

### Specification: Live demo

### Link to github with the code

### Statement on GenAI use

- This paper has been written without the help of an AI. After writing, Gemini was used for proofreading.    
- We used Cursor with several models for fine-tuning and debugging the frame’s code  
- 

#### Authors contributions

*Olga Muss* (Education and cognitive sciences: specification of inputs and slots’ tasks, designing the interaction for the interaction, testing the frame prototype and the final frame, writing the paper)  
*Luca Leisten* (HCI and learning expertise: Designing and implementing the educational intervention at the school, reviewing the frame design, prototype and implementation, review of the paper)  
*Charles Edouard Bardyn* (Technical expertise: idea of the Rodin Four-Slot Frame Engine, development, patent, specifications, creation of a prototype, coding of the Frame, writing of the paper)
