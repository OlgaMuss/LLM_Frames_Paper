# Decision Tree for Coding Co-Creation Level

**Source:** Interaction logs from the Marty/SCAFFOLD pilot study (groups 2–10).  
**Variable:** Co-creation level of the mnemonic-building session with the LLM.  
**Coded by:** Manual review of interaction transcripts and frame logs.

---

## Co-Creation Level Definitions

| Level | Label | Description |
|-------|-------|-------------|
| **0** | LLM did it all | Students provided no relevant input; LLM generated the entire mnemonic. |
| **0.5** | Guidance only (unrelated to learning) | Students contributed only format/style/process directives (e.g., "make it a rhyme", "write it in Italian"), but provided no content about the learning topic. |
| **1** | Concepts by students / rest by LLM | Students identified at least some relevant topic concepts; the LLM used these concepts to build the mnemonic structure on its own. |
| **2** | Concepts by students + co-creation of mnemonic | Students provided concepts **and** contributed ideas, phrases, or narrative elements to the mnemonic creation itself. |
| **3** | Mainly by students | Students took the lead in both phases; LLM primarily organized, structured, or made minor additions to student-generated content. |

---

## Decision Tree

```
START: Review the full interaction transcript for this group
             │
             ▼
┌────────────────────────────────────────────────────────────────----─┐
│ Q1. Did any student provide ANY input that contributed to the task? │
│     (content, format, style, guidance — anything counts)            │
└───────────────────────────────────────────────────────────────----──┘
        │                              │
       NO                            YES
        │                              │
        ▼                              ▼
  ┌───────────┐        ┌──────────────────────────────────────────┐
  │  LEVEL 0  │        │ Q2. Were ALL student contributions ONLY  │
  │           │        │     about format, style, or process?     │
  │ LLM did   │        │     (NOT about topic content)            │
  │ it all    │        │                                          │
  └───────────┘        │  e.g. "Make it a rhyme" / "In Italian"   │
                       │       "Do it for us" / "As a rap"        │
                       └──────────────────────────────────────────┘
                                │                    │
                               YES                  NO
                                │                    │
                                ▼                    ▼
                        ┌───────────┐   ┌──────────────────────────────────-──┐
                        │ LEVEL 0.5 │   │ Q3. Did students independently      │
                        │           │   │     propose a SPECIFIC concept      │
                        │ Guidance  │   │     about microcontrollers in       │
                        │ only      │   │     Phase 1?                        │
                        │ (unrelated│   │                                     │
                        │ to learn) │   │  Counts: pins, voltage, C++,        │
                        └───────────┘   │  HIGH/LOW, what it does/is,         │
                                        │  specific components, real-world use│
                                        │  Does NOT count: vague category     │
                                        │  labels ("electrical technology",   │
                                        │  "it's electronic"), or responses   │
                                        │  that only answer LLM's questions   │
                                        └───────────────────────────────────-─┘
                                                 │               │
                                                NO             YES
                                                 │               │
                                                 ▼               ▼
                                         ┌───────────┐  ┌───────────────────────────────-─────┐
                                         │ LEVEL 0.5 │  │ Q4. Did students contribute to the  │
                                         │           │  │     CREATION of the mnemonic        │
                                         │ Guidance  │  │     in Phase 2?                     │
                                         │ only      │  │                                     │
                                         └───────────┘  │  Counts: a specific phrase,         │
                                                        │  character, metaphor, or narrative  │
                                                        │  element based on topic content     │
                                                        │  Does NOT count: asking the LLM to  │
                                                        │  create it, or style directives     │
                                                        └─────────────────────────────────-───┘
                                                                  │               │
                                                                 NO             YES
                                                                  │               │
                                                                  ▼               ▼
                                                           ┌───────────┐  ┌────────────────────────────────────┐
                                                           │  LEVEL 1  │  │ Q5. Did the key narrative IDEAS    │
                                                           │           │  │     originate from students, with  │
                                                           │ Concepts  │  │     LLM mainly connecting or       │
                                                           │ by        │  │     formatting them?               │
                                                           │ students; │  │                                    │
                                                           │ rest LLM  │  │  YES: characters, metaphors, or    │
                                                           └───────────┘  │  story arc came from students;     │
                                                                          │  LLM translated/assembled          │
                                                                          │  NO: LLM created the narrative     │
                                                                          │  structure; students contributed   │
                                                                          │  individual lines or phrases only  │
                                                                          └────────────────────────────────────┘
                                                                                   │               │
                                                                                  NO             YES
                                                                                   │               │
                                                                                   ▼               ▼
                                                                            ┌───────────┐   ┌───────────┐
                                                                            │  LEVEL 2  │   │  LEVEL 3  │
                                                                            │           │   │           │
                                                                            │ Concepts  │   │  Mainly   │
                                                                            │ + co-     │   │    by     │
                                                                            │ creation  │   │ students  │
                                                                            └───────────┘   └───────────┘
```

---

## CSV Column Reference

Each decision question maps to specific columns in `BuildbotAnalysis - LLM analysis.csv`:

| Question | Primary column(s) to check | How to use |
|----------|---------------------------|------------|
| **Q1** | `Non relevant contributions` + `Number of relevant contributions` | YES if either is non-empty / > 0 |
| **Q2** | `Number of relevant contributions` | YES if > 0; NO if = 0 (but Q1=YES via non-relevant column) |
| **Q3** | `Phase 1: Number of concepts proposed by students` + `Phase 1: concepts identified` | YES if count > 0 AND Phase 1 NOT marked "Unsuccessful" AND concepts are specific (read qualitative column to verify) |
| **Q4** | `Phase 2: Number of relevant Student contributions` | YES if > 0 |
| **Q5** | `Phase 2: Number of relevant Student contributions` + `Phase 2: Collaboration` | YES if count > 0 AND `Phase 2: Collaboration` = "Successful" |

> **Note on Q3 specificity:** A count > 0 in `Phase 1: Number of concepts proposed by students` is necessary but not sufficient. Always read `Phase 1: concepts identified` to verify that the concepts are specific (e.g. pins, voltage, HIGH/LOW) rather than vague category labels (e.g. "electrical technology") and that they were independently proposed rather than only prompted by LLM questions.

---

## Decision Criteria Reference

### Level 0 — LLM did it all
- `Non relevant contributions` is empty AND `Number of relevant contributions` = 0.
- Students provided no input that contributed to the task: silence, "I don't know", or mere confirmation of LLM suggestions.
- **Example group:** Group 10.

### Level 0.5 — Guidance only (unrelated to learning content)
- `Number of relevant contributions` = 0, but `Non relevant contributions` is non-empty (style/format/process guidance present).
- Also applies when `Phase 1: Number of concepts proposed by students` > 0 but `Phase 1: concepts identified` shows only vague labels ("electrical technology") or only LLM-prompted responses — read qualitatively.
- **Example groups:** Group 5, 7, 8, 9.

### Level 1 — Concepts by students / rest by LLM
- `Phase 1: Number of concepts proposed by students` > 0 AND concepts are specific (verified in `Phase 1: concepts identified`).
- `Phase 2: Number of relevant Student contributions` = 0 — LLM built the mnemonic without Phase 2 input from students.
- **Example group:** Group 3.

### Level 2 — Concepts + co-creation of mnemonic
- `Phase 1: Number of concepts proposed by students` > 0 (specific concepts).
- `Phase 2: Number of relevant Student contributions` > 0.
- Reading `Phase 2: Student contributions` shows the LLM structured the narrative; students contributed individual lines or phrases.
- **Example group:** Group 4.

### Level 3 — Mainly by students
- `Phase 1: Number of concepts proposed by students` > 0 (specific concepts).
- `Phase 2: Number of relevant Student contributions` > 0.
- Reading `Phase 2: Student contributions` and `Phase 2: Collaboration` shows the key narrative ideas (characters, metaphors, story arc) originated from students; LLM translated or assembled them.
- **Example groups:** Group 2, Group 6.

---

## Disambiguation Rules

| Situation | Assignment |
|-----------|-----------|
| Student provides no input that contributed to the task (silence, "I don't know", or mere confirmation of LLM suggestions) | Level 0 |
| Student provides only format/style/process guidance — no microcontroller content | Level 0.5 |
| Student's Phase 1 "concept" is a vague category label (e.g. "electrical technology", "it's a chip") | Does **not** count — Q3=NO → Level 0.5 |
| Student's Phase 1 response only answers the LLM's direct question, without independent initiation | Does **not** count as independently proposed concept — Q3=NO |
| Student contributes specific Phase 1 concepts but nothing in Phase 2 | Level 1 |
| Student contributes concepts AND at least one phrase/idea for the mnemonic in Phase 2 | Level 2 or 3 → proceed to Q5 |
| LLM contributed some mnemonic text, but the character/metaphor/story arc came from students | Level 3 (narrative ideas = student-led) |
| LLM structured the narrative; students contributed individual lines or phrases | Level 2 (joint creation) |
| Student repeats or confirms what the LLM suggested (echo contribution) | Does **not** count as independent contribution |
| LLM-dismissed concept that student proposed | **Does count** — student intent matters, not LLM acceptance |
| Student proposes HOW to create (e.g., "as a poem") AND provides a specific concept | Count the concept; ignore the style directive for level |

---

## Coding Checklist (per group)

- [ ] **Q1** — Check `Non relevant contributions` AND `Number of relevant contributions`: any input at all?
- [ ] **Q2** — Check `Number of relevant contributions` > 0: did content go beyond format/style?
- [ ] **Q3** — Check `Phase 1: Number of concepts proposed by students` > 0, then read `Phase 1: concepts identified` to verify specificity and independence
- [ ] **Q4** — Check `Phase 2: Number of relevant Student contributions` > 0
- [ ] **Q5** — Read `Phase 2: Student contributions` and `Phase 2: Collaboration` to judge narrative origin
- [ ] Applied decision tree in order (Q1 → Q2 → Q3 → Q4 → Q5)
- [ ] Assigned final co-creation level
- [ ] Noted any ambiguities or borderline decisions in the coding notes

---

---

## Reliability Check: Decision Tree vs. Original Coding

Applied to groups 2–10 using Phase 1/2 transcript observations only (co-creation level column excluded).
Compared to original coding by O. Muss. Group 1 excluded (data loss).

| Group | Decision path | Tree level | Original | Match | Notes |
|-------|--------------|:----------:|:--------:|:-----:|-------|
| 2 | Q1✓→Q2✓→Q3✓ (3 concepts)→Q4✓→Q5✓ (students proposed character & story arc; LLM connected) | **3** | 3 | ✓ | Q5: narrative ideas (meets Marty, connects, programs, executes) originated from students |
| 3 | Q1✓→Q2✓→Q3✓→Q4✗ (Phase 2: 0 student contributions) | **1** | 1 | ✓ | |
| 4 | Q1✓→Q2✓→Q3✓→Q4✓→Q5✗ (LLM structured the rap; students contributed lines) | **2** | 2 | ✓ | |
| 5 | Q1✓→Q2✓→Q3✗ (Phase 1 unsuccessful; responses only answer LLM's questions) | **0.5** | 0.5 | ✓ | |
| 6 | Q1✓→Q2✓→Q3✓→Q4✓→Q5✓ (hiking-path metaphor originated from students) | **3** | 3 | ✓ | |
| 7 | Q1✓→Q2✓→Q3✗ (Phase 1: 0 concepts) | **0.5** | 0.5 | ✓ | |
| 8 | Q1✓→Q2✓→Q3✗ ("electrical technology" = vague category label, does not count) | **0.5** | 0.5 | ✓ | Q3 specificity rule applied |
| 9 | Q1✓ (format/language guidance counts)→Q2✗ (all style, no content) | **0.5** | 0.5 | ✓ | Q1 now captures any input; Q2 filters for content |
| 10 | Q1✗ (zero input; only "I don't know") | **0** | 0 | ✓ | |

**Agreement rate: 9/9 (100%)** after disambiguating three thresholds:

1. **Q1** — now captures *any* student input (including format/style guidance); Q2 is the filter for content vs. style.
2. **Q3** — requires a *specific* concept (component, function, property); vague category labels ("electrical technology") do not qualify.
3. **Q5** — asks whether the *narrative ideas* (characters, metaphors, story arc) originated from students, not whether students wrote most of the text.

---

## Decision Tree 2: Column-Based

A second tree that operationalises each decision directly from CSV column values, minimising qualitative judgment. Q5 remains qualitative (no single column captures narrative origin).

```
START: Extract column values for the group
             │
             ▼
┌────────────────────────────────────────────────────────────────────┐
│ Q1. Is `Non relevant contributions` non-empty                      │
│     OR `Number of relevant contributions` > 0?                     │
└────────────────────────────────────────────────────────────────────┘
        │                                   │
       NO                                 YES
        │                                   │
        ▼                                   ▼
  ┌───────────┐        ┌───────────────────────────────────────────────┐
  │  LEVEL 0  │        │ Q2. Is `Number of relevant contributions` > 0? │
  └───────────┘        │     (treat "3/8" notation as 3 > 0)           │
                       └───────────────────────────────────────────────┘
                                │                        │
                               NO                      YES
                                │                        │
                                ▼                        ▼
                        ┌───────────┐   ┌────────────────────────────────────────────┐
                        │ LEVEL 0.5 │   │ Q3. Is `Phase 1: Number of concepts         │
                        │           │   │     proposed by students` > 0              │
                        │ (guidance │   │     AND `Phase 1: identification`           │
                        │ only)     │   │     does NOT contain "Unsuccessful"?        │
                        └───────────┘   └────────────────────────────────────────────┘
                                                 │                    │
                                                NO                  YES
                                                 │                    │
                                                 ▼                    ▼
                                         ┌───────────┐  ┌────────────────────────────────────────────┐
                                         │ LEVEL 0.5 │  │ Q4. Is `Phase 2: Number of relevant         │
                                         │           │  │     Student contributions` > 0?             │
                                         └───────────┘  └────────────────────────────────────────────┘
                                                                  │                    │
                                                                 NO                  YES
                                                                  │                    │
                                                                  ▼                    ▼
                                                           ┌───────────┐  ┌────────────────────────────────────┐
                                                           │  LEVEL 1  │  │ Q5. Is `Phase 2: # relevant Student │
                                                           └───────────┘  │ contributions` > 0 AND              │
                                                                          │ `Phase 2: Collaboration`            │
                                                                          │ = "Successful"?                     │
                                                                          └────────────────────────────────────┘
                                                                                   │               │
                                                                                  NO             YES
                                                                                   │               │
                                                                                   ▼               ▼
                                                                            ┌───────────┐   ┌───────────┐
                                                                            │  LEVEL 2  │   │  LEVEL 3  │
                                                                            └───────────┘   └───────────┘
```

### Column values extracted per group

| Grp | `Phase 1: identification` | Ph1 concept count | `Non relevant contributions` | `Number of relevant contributions` | Ph2 relevant count |
|-----|--------------------------|:-----------------:|-----------------------------|------------------------------------|:-----------------:|
| 2 | Partially successful | 3 | — | 3 | 2 |
| 3 | Successful | 3 | "agent m: What do you like..." | 1 | 0 |
| 4 | Partially successful | 5 | — | 9 | 4 |
| 5 | **Unsuccessful** | 3 | "3/8 about asking LLM to do it" | 3 (= "3/8") | 0 |
| 6 | Successful | 3 | — | 6 | 3 |
| 7 | **Unsuccessful** | 0 | "many turns requesting LLM" | 1 | 1 |
| 8 | Partially successful | 1 | "several directives..." | 4 | 3 |
| 9 | **Unsuccessful** | 0 | "several directives..." | 2 | 0 |
| 10 | **Unsuccessful** | 0 | — | 0 | 0 |

### Application & comparison with original coding

| Grp | Q1 | Q2 | Q3 | Q4 | Q5 | Tree 2 level | Original | Match | Notes |
|-----|----|----|----|----|----|:------------:|:--------:|:-----:|-------|
| 2 | ✓ (rel=3) | ✓ (rel=3) | ✓ (count=3, not Unsuccessful) | ✓ (Ph2=2) | ✓ (Collaboration="Successful") | **3** | 3 | ✓ | |
| 3 | ✓ (non-rel non-empty) | ✓ (rel=1) | ✓ (count=3, Successful) | ✗ (Ph2=0) | — | **1** | 1 | ✓ | |
| 4 | ✓ (rel=9) | ✓ (rel=9) | ✓ (count=5, not Unsuccessful) | ✓ (Ph2=4) | ✗ (Collaboration="Unsuccessful") | **2** | 2 | ✓ | |
| 5 | ✓ (non-rel non-empty) | ✓ (rel=3) | ✗ (Phase 1 = **Unsuccessful**) | — | — | **0.5** | 0.5 | ✓ | |
| 6 | ✓ (rel=6) | ✓ (rel=6) | ✓ (count=3, Successful) | ✓ (Ph2=3) | ✓ (Collaboration="Successful") | **3** | 3 | ✓ | |
| 7 | ✓ (non-rel non-empty) | ✓ (rel=1) | ✗ (count=0) | — | — | **0.5** | 0.5 | ✓ | |
| 8 | ✓ (non-rel non-empty) | ✓ (rel=4) | ✓\* (count=1, "Partially successful") | ✓ (Ph2=3) | ✗ (LLM structured) | **2\*** | 0.5 | ✗ | \*Q3 passes on columns alone because "Partially successful" ≠ "Unsuccessful". Concept is "electrical technology" (vague) — only the full tree's specificity rule catches this. |
| 9 | ✓ (non-rel non-empty) | ✓ (rel=2) | ✗ (count=0) | — | — | **0.5** | 0.5 | ✓ | |
| 10 | ✗ (both empty/0) | — | — | — | — | **0** | 0 | ✓ | |

**Agreement rate: 8/9 (89%).** The one remaining disagreement (Group 8) cannot be resolved by column values alone: `Phase 1: identification` = "Partially successful (run out of time)" does not contain "Unsuccessful", so Q3 passes — but the single concept ("electrical technology") is too vague. Resolving Group 8 requires reading `Phase 1: concepts identified` qualitatively, which is what Decision Tree 1's specificity rule does.

**Conclusion:** Tree 2 is now fully column-based (no qualitative judgment required). It achieves 89% agreement. The single remaining failure (Group 8) occurs only at Q3, where "Partially successful" Phase 1 with one vague concept cannot be distinguished from a valid partial success without reading the concept text.

---

*Based on the coding scheme pre-registered and described in: Muss, Leisten & Bardyn (in prep.), SCAFFOLD paper, Section 3.1.5 and footnote on co-creation level variable.*
