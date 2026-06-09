import streamlit as st

def render_header():
    st.set_page_config(
        page_title="Dental Expert System",
        page_icon="🦷",
        layout="centered",
    )
    st.title("Dental Expert System")
    st.write("A rule-based expert system for dental diagnosis")
    st.divider()

def render_questions(symptom_questions):
    question_map = {key: question for key, question in symptom_questions}
    groups = [
        ("Pain and Sensitivity", [
            "tooth_pain", "severe_throbbing_pain", "cold_sensitivity",
            "hot_sensitivity", "sweet_sensitivity", "pain_while_chewing",
            "lingering_pain", "night_pain", "pain_on_tapping",
        ]),
        ("Gum and Periodontal", [
            "gum_bleeding", "gum_redness", "gum_tenderness",
            "receding_gums", "gum_pockets", "loose_teeth", "plaque_tartar",
        ]),
        ("Infection and Swelling", [
            "gum_face_swelling", "bad_breath", "pus_bad_taste",
            "fever", "difficulty_opening_mouth", "swollen_lymph_nodes",
        ]),
        ("Bruxism and Jaw", [
            "grinding_sleep", "jaw_pain_fatigue", "morning_headache",
            "earache", "worn_teeth",
        ]),
        ("Other Signs", ["visible_cavity"]),
    ]

    st.subheader("Step 1: Enter Symptoms")
    st.write("Check all symptoms that apply to you:")
    answers = {}

    for group_name, keys in groups:
        with st.expander(group_name):
            col1, col2 = st.columns(2)
            for i, key in enumerate(keys):
                question = question_map.get(key, key.replace("_", " ").capitalize())
                col = col1 if i % 2 == 0 else col2
                answers[key] = col.checkbox(question, key=key)
    return answers

def render_review(answers, rules):
    st.subheader("Step 2: Review Your Answers")
    selected = [k for k, v in answers.items() if v]
    if not selected:
        st.warning("No symptoms selected. Please go back and select at least one.")
        if st.button("Back to Questions"):
            return False
        return None

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Selected Symptoms:**")
        for symptom in selected:
            st.write(f"- {symptom.replace('_', ' ').capitalize()}")

    with col2:
        st.write("**Summary:**")
        st.write(f"Total symptoms selected: {len(selected)}")
        st.write(f"Out of {len(answers)} possible symptoms")

    st.divider()

    st.write("**Conditions that will be evaluated:**")
    possible_diseases = set()
    for rule in rules:
        rule_symptoms = set(rule["conditions"].keys())
        if rule_symptoms & set(selected):
            possible_diseases.add(rule["disease"])

    if possible_diseases:
        for disease in sorted(possible_diseases):
            st.write(f"- {disease}")
    else:
        st.write("No conditions match the selected symptoms.")

    st.divider()

    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("Edit Symptoms", use_container_width=True):
            return False
    with col_next:
        if st.button("Run Diagnosis", type="primary", use_container_width=True):
            return True
    return None

def render_result(result, rules):
    st.subheader("Step 3: Diagnosis Result")
    st.divider()
    if not result.get("diagnosis"):
        st.error("No reliable diagnosis could be determined.")
        st.write("Please try again with different or more specific symptoms.")
        if st.button("Start Over"):
            st.session_state.clear()
            st.rerun()
        return

    diagnosis = result["diagnosis"]
    confidence = result.get("confidence", "Unknown")
    score = result.get("score", 0)
    fired_rules = result.get("fired_rules", [])
    matched_symptoms = result.get("matched_symptoms", [])
    st.write(f"**Diagnosis:** {diagnosis}")
    st.write(f"**Confidence:** {confidence}")
    st.write(f"**Match Score:** {score * 100:.0f}%")
    st.progress(int(score * 100))
    st.divider()
    if matched_symptoms:
        st.write("**Symptoms that matched this diagnosis:**")
        for symptom in matched_symptoms:
            st.write(f"- {symptom.replace('_', ' ').capitalize()}")
    st.divider()

    if fired_rules:
        st.write("**Rules that were triggered:**")
        for rule_id in fired_rules:
            for rule in rules:
                if rule["id"] == rule_id:
                    with st.expander(rule_id):
                        st.write(f"Condition: {rule['disease']}")
                        st.write("Required symptoms:")
                        for symptom, required in rule["conditions"].items():
                            status = "Must be present" if required else "Must be absent"
                            st.write(f"  - {symptom.replace('_', ' ').capitalize()}: {status}")
                    break
    st.divider()
    if confidence == "High":
        st.success("The symptoms strongly match the diagnostic patterns for this condition.")
    elif confidence == "Medium":
        st.info("The symptoms partially match. Further examination may be needed.")
    else:
        st.warning("The match is weak. Please consult a dentist for proper evaluation.")
    st.write("---")
    st.caption("Note: This system is for educational purposes only and does not replace professional medical advice.")
    if st.button("Start New Diagnosis", use_container_width=True):
        st.session_state.clear()
        st.rerun()
