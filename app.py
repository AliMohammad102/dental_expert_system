"""Coordinator for the dental expert system application."""

import streamlit as st

import inference_engine
import knowledge_base
import ui


def main() -> None:
    ui.render_header()

    st.header("Patient Symptoms")
    working_memory = ui.render_questions(knowledge_base.SYMPTOM_QUESTIONS)

    if st.button("Diagnose"):
        result = inference_engine.diagnose(working_memory)
        ui.render_result(result)


if __name__ == "__main__":
    main()
