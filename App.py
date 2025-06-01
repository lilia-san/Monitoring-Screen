import streamlit as st
import importlib
from datetime import datetime

# Set Streamlit page config
st.set_page_config(page_title="Monitoring Screen", layout="centered")

# --- AUTH0 LOGIN ---
if not st.experimental_user.is_logged_in:
    st.image("image1.jpg", use_container_width = True)
    st.title("Welcome to the Traffic Monitoring Dashboard 🚦")
    st.title("🔐 Login Required or Authentification")
    st.markdown("Please log in to access the traffic monitoring dashboard.")
    if st.button("Login with Auth0 or Google"):
        st.login("auth0")
    
    st.stop()

# --- LOGOUT HANDLER ---
if st.sidebar.button("🚪 Logout"):
    st.logout()
    st.stop()

# --- HEADER SECTION ---
date = datetime.today().strftime('%Y-%m-%d')
st.title("Welcome to the Traffic Monitoring Dashboard 🚦")
st.title(f"**Date** :red[{date}]")

# --- SIDEBAR INFO ---
st.sidebar.title("Navigation")
st.sidebar.markdown(f"👤 {st.experimental_user.name}")
st.sidebar.markdown(f"📧 {st.experimental_user.email}")

page = st.sidebar.radio("Go to", [
    "🚗 **Dashboard Home**", 
    "🎥 **Camera Display**", 
    "🚨 **Plate tracking**",
    "📈 **Traffic Prediction**", 
    "⚙️ **Settings**"
])

# --- PAGE ROUTING ---
if page == "🚗 **Dashboard Home**":
    chart_module = importlib.import_module("streampages.Chart")
    chart_module.traffic_chart()

elif page == "🎥 **Camera Display**":
    camera_module = importlib.import_module("streampages.Camera")
    camera_module.main_camera()

elif page == "🚨 **Plate tracking**":
    plate_module = importlib.import_module("streampages.Plate")
    plate_module.tracking()

elif page == "📈 **Traffic Prediction**":
    pred_module = importlib.import_module("streampages.Prediction")
    pred_module.prediction()

elif page == "⚙️ **Settings**":
    settings_module = importlib.import_module("streampages.Settings")
    settings_module.settings_session()




