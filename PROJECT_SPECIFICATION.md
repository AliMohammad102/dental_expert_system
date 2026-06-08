PROJECT TITLE:
Dental Expert System (Rule-Based Expert System)

==================================================================
GOAL
====

Build a simple academic expert system for diagnosing common dental problems.

The project must demonstrate the following expert system concepts:

* Knowledge Base
* Inference Engine
* Working Memory
* User Interface
* Explanation System

The implementation must remain simple, educational, and easy for a university student to understand and explain during a project discussion.

==================================================================
TECHNOLOGY
==========

Use:

* Python
* Streamlit

Do NOT use:

* CLIPS
* Database
* API
* Machine Learning
* Deep Learning
* Backend/Frontend separation
* Authentication/Login
* Configuration files
* Complex OOP architecture
* Design patterns
* External services
* Unnecessary frameworks

==================================================================
PROJECT STRUCTURE
=================

project/
│
├── app.py
├── ui.py
├── knowledge_base.py
└── inference_engine.py

No additional files unless absolutely necessary.

==================================================================
FILE RESPONSIBILITIES
=====================

1. knowledge_base.py

Contains:

* Diseases
* Symptoms
* Rules

---

2. inference_engine.py

Contains:

* Fact generation
* Rule evaluation
* Rule firing
* Diagnosis selection
* Confidence calculation
* Explanation generation

---

3. ui.py

Contains:

* Streamlit user interface

---

4. app.py

Acts as the coordinator:

* Collect user answers
* Build Working Memory
* Call Inference Engine
* Display results

==================================================================
WORKING MEMORY
==============

Working Memory must be implemented as a simple Python dictionary stored in memory during execution.

Example:

{
"tooth_pain": True,
"cold_sensitivity": True,
"visible_cavity": True
}

No database.

No file storage.

No persistence.

---

The Working Memory is internally stored as a Python dictionary.

During the inference process, the system converts positive user answers into explicit Facts for rule evaluation.

Example:

FACT: tooth_pain

FACT: cold_sensitivity

FACT: visible_cavity

These Facts are generated from the Working Memory and are used by the Inference Engine during reasoning.

==================================================================
DISEASES
========

1. Dental Caries

2. Tooth Sensitivity

3. Pulpitis

4. Gingivitis

5. Dental Abscess

6. Bruxism

7. Gum Recession

==================================================================
SYMPTOMS
========

1. Tooth Pain

2. Severe or Throbbing Pain

3. Cold Sensitivity

4. Hot Sensitivity

5. Visible Cavity

6. Gum Bleeding

7. Gum Redness

8. Gum or Face Swelling

9. Persistent Bad Breath

10. Pus or Bad Taste

11. Pain While Chewing

12. Teeth Grinding During Sleep

13. Jaw Pain or Fatigue in the Morning

14. Exposed Tooth Root / Receding Gums

15. Pain Continues After Removing the Stimulus

16. Night Pain or Waking Up Because of Pain

==================================================================
USER QUESTIONS
==============

1. Do you feel pain in one of your teeth?

2. Is the pain severe or throbbing?

3. Do you feel pain or discomfort when drinking cold beverages?

4. Do you feel pain or discomfort when drinking hot beverages?

5. Do you notice a visible cavity or hole in the tooth?

6. Do your gums bleed while brushing or spontaneously?

7. Do your gums appear red or inflamed?

8. Is there swelling in your gums or face?

9. Do you suffer from persistent bad breath?

10. Do you notice pus or a bad taste coming from the gum or tooth?

11. Do you feel pain while chewing?

12. Has anyone told you that you grind your teeth while sleeping?

13. Do you wake up with jaw pain or fatigue?

14. Do you notice gum recession or exposed tooth roots?

15. Does the pain continue after removing the trigger such as cold or hot drinks?

16. Does the pain become worse at night or wake you up from sleep?

==================================================================
KNOWLEDGE BASE RULES
====================

---

## DENTAL CARIES

Rule 1

IF:

* Tooth Pain
* Cold Sensitivity
* Visible Cavity

THEN:
possible_caries

---

Rule 2

IF:

* Visible Cavity
* Cold Sensitivity

THEN:
possible_caries

---

Rule 3

IF:

* Pain While Chewing
* Visible Cavity

THEN:
possible_caries

==================================================

DENTAL SENSITIVITY

==================================================

Rule 1

IF:

* Cold Sensitivity
* No Severe or Throbbing Pain
* No Visible Cavity

THEN:
possible_sensitivity

---

Rule 2

IF:

* Cold Sensitivity
* Hot Sensitivity
* No Visible Cavity

THEN:
possible_sensitivity

==================================================

PULPITIS

==================================================

Rule 1

IF:

* Severe or Throbbing Pain
* Pain Continues After Removing the Stimulus
* Night Pain

THEN:
possible_pulpitis

---

Rule 2

IF:

* Severe or Throbbing Pain
* Cold Sensitivity
* Night Pain

THEN:
possible_pulpitis

---

Rule 3

IF:

* Severe or Throbbing Pain
* Hot Sensitivity
* Pain Continues After Removing the Stimulus

THEN:
possible_pulpitis

==================================================

GINGIVITIS

==================================================

Rule 1

IF:

* Gum Bleeding
* Gum Redness

THEN:
possible_gingivitis

---

Rule 2

IF:

* Gum Bleeding
* Gum Redness
* Persistent Bad Breath

THEN:
possible_gingivitis

---

Rule 3

IF:

* Gum Bleeding
* Gum Redness
* Gum or Face Swelling

THEN:
possible_gingivitis

==================================================

DENTAL ABSCESS

==================================================

Rule 1

IF:

* Gum or Face Swelling
* Severe or Throbbing Pain
* Pus or Bad Taste

THEN:
possible_abscess

---

Rule 2

IF:

* Gum or Face Swelling
* Severe or Throbbing Pain
* Pain While Chewing

THEN:
possible_abscess

---

Rule 3

IF:

* Gum or Face Swelling
* Persistent Bad Breath
* Pus or Bad Taste

THEN:
possible_abscess

==================================================

BRUXISM

==================================================

Rule 1

IF:

* Teeth Grinding During Sleep
* Jaw Pain or Fatigue in the Morning

THEN:
possible_bruxism

---

Rule 2

IF:

* Teeth Grinding During Sleep
* Tooth Pain
* Jaw Pain or Fatigue in the Morning

THEN:
possible_bruxism

==================================================

GUM RECESSION

==================================================

Rule 1

IF:

* Exposed Tooth Root / Receding Gums
* Cold Sensitivity

THEN:
possible_recession

---

Rule 2

IF:

* Exposed Tooth Root / Receding Gums
* Cold Sensitivity
* Hot Sensitivity

THEN:
possible_recession

---

Rule 3

IF:

* Exposed Tooth Root / Receding Gums
* Tooth Pain
* Cold Sensitivity

THEN:
possible_recession

==================================================================
INFERENCE ENGINE
================

STEP 1

Collect user answers.

---

STEP 2

Convert positive answers into Facts.

Example:

FACT: tooth_pain

FACT: cold_sensitivity

FACT: visible_cavity

---

STEP 3

Store Facts in Working Memory.

---

STEP 4

Evaluate all rules.

---

STEP 5

Whenever a rule is fully satisfied:

* Fire the rule.
* Create a diagnostic Fact.

Example:

Rule Fired:

Dental Caries Rule 1

Generated Fact:

possible_caries

---

STEP 6

Count how many rules fired for each disease.

Example:

possible_caries

Rule 1 -> Fired

Rule 2 -> Fired

Rule 3 -> Fired

---

STEP 7

Select the disease with the highest number of fired rules.

If multiple diseases have the same number of fired rules, select the disease with the highest total number of matched symptoms.

Only one final diagnosis should be returned.

Do NOT return multiple diagnoses.

==================================================================
CONFIDENCE LEVELS
=================

The system must use only:

* High
* Medium
* Low

No percentages.

No matching score.

---

HIGH

All rules of the selected disease fired.

Examples:

3 out of 3

or

2 out of 2

---

MEDIUM

More than one rule fired, but not all rules.

Example:

2 out of 3

---

LOW

Only one rule fired.

Examples:

1 out of 3

or

1 out of 2

==================================================================
SAFETY RULE
===========

If no rule fires:

Return:

"Unable to determine a reliable diagnosis."

Do not force a diagnosis.

==================================================================
EXPLANATION SYSTEM
==================

The system must display:

* Diagnosis Name
* Confidence Level
* Fired Rule IDs
* Matched Symptoms

Example:

Diagnosis:
Dental Caries

Confidence:
High

Fired Rules:

* Rule 1
* Rule 2
* Rule 3

Matched Symptoms:

* Tooth Pain
* Cold Sensitivity
* Visible Cavity

==================================================================
IMPORTANT IMPLEMENTATION CONSTRAINT
===================================

This project is an educational university project.

Keep the code:

* Simple
* Readable
* Easy to understand
* Easy to explain during project discussion

Avoid:

* Overengineering
* Excessive abstraction
* Complex class hierarchies
* Advanced software architecture
* Unnecessary files

The final project should be understandable by a student within one or two days of study.
