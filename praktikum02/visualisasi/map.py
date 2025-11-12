import streamlit as st
import pandas as pd
import numpy as np

st.title("Visualisasi")
st.write("kelompok 14")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] +[15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.subheader("Random Map")
st.map(df)