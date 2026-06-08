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
            /* Button styling: larger, centered, subtle hover */
            .stButton {
                display: flex;
                justify-content: center;
            }
            .stButton>button {
                background-color: #0d6efd;
                color: #ffffff;
                border-radius: 10px;
                border: none;
                padding: 0.95rem 1.3rem;
                font-weight: 700;
                font-size: 1.05rem;
                transition: transform 0.12s ease, box-shadow 0.12s ease;
            }
            .stButton>button:hover {
                background-color: #0b5ed7;
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(13,59,102,0.12);
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

            /* Result card styling */
            .result-card {
                background: #ffffff;
                border-radius: 16px;
                border: 1px solid #e2e2e2;
                box-shadow: 0 8px 20px rgba(11,77,135,0.06);
                padding: 22px;
                margin-top: 1.25rem;
                width: 100%;
                box-sizing: border-box;
            }
            .result-card h2, .result-card h3 { color: #0d3b66; margin-top:0 }
            .result-card ul { margin-top:0.45rem; margin-bottom:0.25rem; padding-left:1.1rem }

            /* Slightly increase gap between expanders */
            .stExpander {
                margin-bottom: 0.9rem;
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


def _render_card_start():
    """Return a Streamlit container to be used as a card wrapper.

    Usage: `with _render_card_start():` then render card contents inside the block.
    """
    return st.container()


def _render_card_end() -> None:
    # kept for backward compatibility; no longer needed with container approach
    return None


def _format_symptom(symptom: str) -> str:
    return symptom.replace('_', ' ').capitalize()


def render_result(result):
    st.subheader("Diagnosis Results")
    with _render_card_start():
        # Build HTML for the entire card so all content is inside the styled box.
        html_lines = ["<div class='result-card'>"]

        if result.get("diagnosis"):
            diagnosis = result.get("diagnosis")
            confidence = result.get("confidence") or result.get("match_type") or "Unknown"
            html_lines.append(f"<h3 style='margin-bottom:0.1rem;'>Diagnosis</h3>")
            html_lines.append(f"<p style='margin-top:0.1rem; margin-bottom:0.35rem; font-weight:700;'>{diagnosis}</p>")
            html_lines.append(f"<p style='margin:0 0 0.6rem 0;'><strong>Confidence Level:</strong> {confidence}</p>")

            fired_rules = result.get("fired_rules") or ([] if result.get("diagnosis") else [])
            if fired_rules:
                html_lines.append("<p style='margin:0.25rem 0 0.25rem 0;'><strong>Fired Rules:</strong></p>")
                html_lines.append("<ul>")
                for rule_id in fired_rules:
                    html_lines.append(f"<li>{rule_id}</li>")
                html_lines.append("</ul>")

            matched_symptoms = result.get("matched_symptoms") or []
            if matched_symptoms:
                html_lines.append("<p style='margin:0.35rem 0 0.2rem 0;'><strong>Matched Symptoms:</strong></p>")
                html_lines.append("<ul>")
                for symptom in matched_symptoms:
                    html_lines.append(f"<li>{_format_symptom(symptom)}</li>")
                html_lines.append("</ul>")
        else:
            html_lines.append("<p><strong>Unable to determine a reliable diagnosis.</strong></p>")

        html_lines.append("</div>")
        st.markdown("\n".join(html_lines), unsafe_allow_html=True)
