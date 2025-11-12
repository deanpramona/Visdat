import streamlit as st

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Main Page")
st.markdown("""
    Kelompok 14:
    1. Fatih Mubasyir (0110222186)
    2. Hisyam Wildan Alfath (0110222206) 
    3. Dean Pramona (0110222163)
""") 

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are u A New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)
st.sidebar.selectbox("Pilih Visualisasi", ["Bar", "Line", "Area"])

# NOTFICATION ALERT
st.success("Successful")
st.warning("Warning")
st.info("INFO")
st.error("Errors")
st.exception("It is an exception")