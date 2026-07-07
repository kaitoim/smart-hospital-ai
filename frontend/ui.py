import streamlit as st

from backend.chatbot import Chatbot
from frontend.style import CUSTOM_CSS


def initialize_session():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "bot" not in st.session_state:
        st.session_state.bot = Chatbot()


def sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/hospital.png",
            width=80
        )

        st.title("Smart Hospital AI")

        st.markdown("---")

        st.write(
            """
            ### Fitur

            ✅ SIMRS

            ✅ Troubleshooting

            ✅ SOP Rumah Sakit

            ✅ AI Assistant
            """
        )

        if st.button("🗑 Clear Chat"):
            st.session_state.messages = []
            st.session_state.bot.clear()
            st.rerun()


def show_messages():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


def chat():

    question = st.chat_input(
        "Tulis pertanyaan Anda..."
    )

    if not question:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Sedang berpikir..."):

            answer = st.session_state.bot.ask(question)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


def run_app():

    initialize_session()

    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    sidebar()

    st.markdown(
        "<div class='main-title'>🏥 Smart Hospital IT Assistant</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Asisten AI untuk SIMRS dan Sistem Informasi Rumah Sakit</div>",
        unsafe_allow_html=True
    )

    show_messages()

    chat()