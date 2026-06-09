import streamlit as st
import inference_engine
import knowledge_base
import ui

def main():
    ui.render_header()
    if "page" not in st.session_state:
        st.session_state.page = "questions"
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "result" not in st.session_state:
        st.session_state.result = None

    if st.session_state.page == "questions":
        show_questions()
    elif st.session_state.page == "review":
        show_review()
    elif st.session_state.page == "results":
        show_results()

def show_questions():
    answers = ui.render_questions(knowledge_base.SYMPTOM_QUESTIONS)
    st.session_state.answers = answers
    if st.button("Review Answers", type="primary", use_container_width=True):
        st.session_state.page = "review"
        st.rerun()

def show_review():
    confirmed = ui.render_review(st.session_state.answers, knowledge_base.RULES)
    if confirmed is True:
        result = inference_engine.diagnose(st.session_state.answers)
        st.session_state.result = result
        st.session_state.page = "results"
        st.rerun()
    elif confirmed is False:
        st.session_state.page = "questions"
        st.rerun()

def show_results():
    """Display the diagnosis results page."""
    ui.render_result(st.session_state.result, knowledge_base.RULES)

if __name__ == "__main__":
    main()