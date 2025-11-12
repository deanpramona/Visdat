import streamlit as st
import graphviz as graphviz

st.title("Visualisasi GraphViz")
st.write("kelompok 14")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

st.graphviz_chart("""
    digraph{
        "Training data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"        
    }
""")