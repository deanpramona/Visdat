import streamlit as st

st.title("Columns")
st.write("kelompok 14")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

col1, col2 = st.columns(2)
col1.write("ini adalah kolom pertama")
col1.image("D:/Praktikum Visdat/assets/bowi2.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("D:/Praktikum Visdat/assets/bowi.jpg")