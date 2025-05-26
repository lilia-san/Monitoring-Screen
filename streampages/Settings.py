import streamlit as st
from datetime import datetime

def settings_session():
    st.header("Settings")
    volume = st.sidebar.slider("Adjust Sound Level", 0, 100, 50)
    st.write(f"Current Sound Level: {volume}")

#settings_session()
