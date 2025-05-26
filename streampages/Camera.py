import streamlit as st
from datetime import datetime

def Region_Filter():
    st.sidebar.title("Diplay cameras per Area")
    Departement = st.sidebar.selectbox(
    "Select the department",
    ('Atlantique', 'Littoral', 'Attacora', 'Donga','Borgou', 'Allibori', 
     'Mono', 'Couffo','Zou', 'Collines', 'Oueme', 'Platteau'), index=None, 
      placeholder="Choose an option",
    )
    City = st.sidebar.selectbox(
    "Select the City",
    ('Cotonou', 'Porto-Novo', 'Abomey-Calavi', 'Bobpa','Possotome', 'Natitingou',
      'Ouidah', 'Parakou','Sèmè', 'Kandi', 'Djougou', 'Grand-Popo'), index=None, 
      placeholder="Choose an option",
    )
    Area = st.sidebar.selectbox(
    "Select the Area",
    ('Saint Michel', 'Sikekodji', 'Quartier Jaq', 'Haie Vive', 'Marina', 'Zongo', 
     'Arconville', 'Ganhi', 'PK6', 'Cadjèhoun', 'Fidjrossè', 'Kouhounou'), index=None, 
      placeholder="Choose an option",
    )
    st.header("Live Traffic Feeds",divider="gray")
    st.markdown(f"**Cameras display for** <span style='color:red'>{Departement}</span> **Department,** "
            f"<span style='color:red'>{City}</span>  **City, and** "
            f"<span style='color:red'>{Area}</span> **Area.**", unsafe_allow_html=True)

def traffic_camera():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Camera 1")
        video_url1 = "https://youtu.be/nnXjWVC6SW4"
        st.video(video_url1, autoplay=True)

        st.subheader("Camera 2")
        VIDEO2_URL = "https://youtu.be/6d2N7Cdh6JA"
        st.video(VIDEO2_URL,autoplay=True)

    with col2:
        st.subheader("Camera 3")
        VIDEO3_URL = "https://youtu.be/LtartHuSj6U"
        st.video(VIDEO3_URL,autoplay=True)

        st.subheader("Camera 4")
        VIDEO4_URL = "https://youtu.be/Cf02sgFFJhw"
        st.video(VIDEO4_URL,autoplay=True)


def main_camera():
  Region_Filter()
  traffic_camera()