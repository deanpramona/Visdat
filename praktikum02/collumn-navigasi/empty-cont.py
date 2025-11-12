import streamlit as st
import time

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Empty Container")
st.markdown("""
    Kelompok 14:
    1. Fatih Mubasyir (0110222186)
    2. Hisyam Wildan Alfath (0110222206) 
    3. Dean Pramona (0110222163)
""")

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ Times up!")