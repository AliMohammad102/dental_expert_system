"""Streamlit user interface for the dental expert system."""

import streamlit as st


def render_header() -> None:
    st.set_page_config(page_title="Dental Expert System", page_icon="🦷", layout="centered")
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #eeeeee;
                color: #0d3b66;
            }
            .stButton>button {
                background-color: #0d6efd;
                color: #ffffff;
                border-radius: 6px;
                border: none;
                padding: 0.75rem 1rem;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #0b5ed7;
            }
            .block-container {
                padding: 2rem;
                max-width: 900px;
            }
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
    st.markdown("<div style='font-size:3rem; margin-bottom:0.25rem;'>🦷</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-bottom:0.25rem;'>Dental Expert System</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:18px; max-width:760px; margin-top:0;'>This expert system collects simple dental symptoms and suggests the most likely diagnosis based on rule matching.</p>",
        unsafe_allow_html=True,
    )


def render_questions(symptom_questions):
    answers = {}
    for key, question in symptom_questions:
        answer = st.radio(question, ["No", "Yes"], index=0, key=key)
        answers[key] = answer == "Yes"
    return answers


def render_result(result):
    st.subheader("Diagnosis Results")
    if result["diagnosis"]:
        st.markdown(f"**Diagnosis:** {result['diagnosis']}")
        st.markdown(f"**Match Type:** {result['match_type']}")
        st.markdown(f"**Matching Score:** {result['score']:.0%}")
        st.markdown(f"**Matched Rule:** {result['matched_rule']}")
        if result["matched_symptoms"]:
            st.markdown("**Matched Symptoms:**")
            for symptom in result["matched_symptoms"]:
                st.markdown(f"- {symptom.replace('_', ' ').capitalize()}")
    else:
        st.markdown("Unable to determine a reliable diagnosis.")
        st.markdown(f"**Highest Score:** {result['score']:.0%}")
        if result["matched_rule"]:
            st.markdown(f"**Best Matching Rule:** {result['matched_rule']}")
