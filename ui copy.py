"""Streamlit user interface for the dental expert system."""

import streamlit as st


def render_header() -> None:
    st.set_page_config(page_title="Dental Expert System", page_icon="🦷", layout="centered")
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #ffffff;
                color: #0d3b66;
            }
            .stButton>button {
                background-color: #0d6efd;
                color: #ffffff;
                border-radius: 8px;
                border: none;
                padding: 0.85rem 1.1rem;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #0b5ed7;
            }
            .block-container {
                padding: 2rem;
                max-width: 1000px;
            }
            .stCheckbox label,
            .stCheckbox span,
            .stRadio label,
            .stRadio span {
                color: #0d3b66;
            }
            h1, h3 {
                color: #0d3b66;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 style='margin-bottom:0.25rem;'>🦷 Dental Expert System</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:18px; max-width:760px; margin-top:0; margin-bottom:1.5rem;'>Select the symptoms you are experiencing and click Analyze Symptoms.</p>",
        unsafe_allow_html=True,
    )


def render_questions(symptom_questions):
    question_map = {key: question for key, question in symptom_questions}

    symptom_groups = [
        (
            "Pain Symptoms",
            [
                "tooth_pain",
                "severe_throbbing_pain",
                "cold_sensitivity",
                "hot_sensitivity",
                "pain_while_chewing",
                "pain_after_stimulus",
                "night_pain",
            ],
        ),
        (
            "Gum Symptoms",
            [
                "gum_bleeding",
                "gum_redness",
                "gum_face_swelling",
                "receding_gums",
            ],
        ),
        (
            "Infection Symptoms",
            [
                "bad_breath",
                "pus_bad_taste",
            ],
        ),
        (
            "Bruxism Symptoms",
            [
                "grinding_sleep",
                "jaw_pain_fatigue",
            ],
        ),
        (
            "Other Symptoms",
            [
                "visible_cavity",
            ],
        ),
    ]

    answers = {}

    for group_title, keys in symptom_groups:
        with st.expander(group_title, expanded=True):
            col1, col2 = st.columns(2)
            for index, key in enumerate(keys):
                question = question_map.get(key, key.replace('_', ' ').capitalize())
                column = col1 if index % 2 == 0 else col2
                answers[key] = column.checkbox(question, key=key)

    return answers


def _render_card_start() -> None:
    st.markdown(
        """
        <div style='background:#ffffff; border:1px solid #e2e2e2; border-radius:16px; padding:22px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-top:1.25rem;'>
        """,
        unsafe_allow_html=True,
    )


def _render_card_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def _format_symptom(symptom: str) -> str:
    return symptom.replace('_', ' ').capitalize()


def render_result(result):
    st.subheader("Diagnosis Results")
    _render_card_start()

    if result.get("diagnosis"):
        st.markdown(f"**Diagnosis:** {result['diagnosis']}")
        confidence = result.get("confidence") or result.get("match_type") or "Unknown"
        st.markdown(f"**Confidence Level:** {confidence}")

        fired_rules = result.get("fired_rules") or ([] if result.get("diagnosis") else [])
        if fired_rules:
            st.markdown("**Fired Rules:**")
            for rule_id in fired_rules:
                st.markdown(f"- {rule_id}")

        matched_symptoms = result.get("matched_symptoms") or []
        if matched_symptoms:
            st.markdown("**Matched Symptoms:**")
            for symptom in matched_symptoms:
                st.markdown(f"- {_format_symptom(symptom)}")
    else:
        st.markdown("**Unable to determine a reliable diagnosis.**")

    _render_card_end()
