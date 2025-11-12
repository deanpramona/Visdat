import streamlit as st
from PIL import Image

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Padding")
st.markdown("""
    Kelompok 14:
    1. Fatih Mubasyir (0110222186)
    2. Hisyam Wildan Alfath (0110222206) 
    3. Dean Pramona (0110222163)
""")


img = Image.open("../../assets/bowi2.jpg")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)