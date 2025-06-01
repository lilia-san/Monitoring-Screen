import streamlit as st
import importlib
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Traffic Monitoring System", layout="wide")

# --- AUTHENTICATION ---
st.login("auth0")  # Initiates Auth0 login flow
user = st.user

if not user:
    st.error("You need to log in to use this app.")
    st.stop()

# Safely display user info
user_display = getattr(user, "email", "Guest")
st.sidebar.markdown(f"👤 {user_display}")

# Main menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Dashboard", "Data Analysis", "Prediction", "About"],
        icons=["speedometer", "bar-chart", "graph-up-arrow", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# --- DYNAMIC MODULE IMPORT ---
if selected == "Dashboard":
    dashboard_module = importlib.import_module("streampages.Dashboard")
    dashboard_module.app()
elif selected == "Data Analysis":
    analysis_module = importlib.import_module("streampages.Analysis")
    analysis_module.app()
elif selected == "Prediction":
    pred_module = importlib.import_module("streampages.Prediction")
    pred_module.app()
elif selected == "About":
    about_module = importlib.import_module("streampages.About")
    about_module.app()



