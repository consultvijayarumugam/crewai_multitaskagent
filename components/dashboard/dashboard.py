import streamlit as st

from components.cards.stat_card import render_stat_card


def render_dashboard():

    if "questions" not in st.session_state:
        st.session_state.questions = 0

    if "research_calls" not in st.session_state:
        st.session_state.research_calls = 0

    if "memory_updates" not in st.session_state:
        st.session_state.memory_updates = 0

    if "avg_time" not in st.session_state:
        st.session_state.avg_time = 0.0

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_stat_card(
            "Questions",
            st.session_state.questions,
            "💬"
        )

    with c2:
        render_stat_card(
            "Research",
            st.session_state.research_calls,
            "🌐"
        )

    with c3:
        render_stat_card(
            "Memory",
            st.session_state.memory_updates,
            "🧠"
        )

    with c4:
        render_stat_card(
            "Avg Time",
            f"{st.session_state.avg_time:.2f}s",
            "⚡"
        )

    st.divider()