import streamlit as st

from frontend.ui import run_app

st.set_page_config(
    page_title="Smart Hospital AI Assistant",
    page_icon="🏥",
    layout="wide"
)

run_app()