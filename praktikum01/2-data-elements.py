# import library streamlit
import streamlit as st
import pandas as pd
import numpy as np
import altair as slt

# Menampilkan Identitas Kelompok
st.title("Praktikum 1 Visualisasi Data")
st.caption("Bagian 1 - Data Elements")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

# DataFrame : Struktur data berbentuk tabel (baris dan kolom) yang disediakn oleh library pandas
st.subheader("DataFrame")
# buat dataframe
df = pd.DataFrame(
    np.random.randn(30,10),
    columns = ('col_no %d' % i for i in range (10))
)
# menampilkan dataframe
st.dataframe(df)

# highlight nilai minimum dari dataframe tdi
st.subheader("Highliht Minimun Value In Dataframe")
# axis=0 bekerja per kolom
# axis=1 bekerja per baris
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
# menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
# metrics tunggal (nilai utama+nilai kenaikan)
st.metric(label="Temperature", value="31 c", delta="1.2 c") # kenaikan 1.2 c

# Metrics sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubuahan:
# 1. "normal" (default): naik itu hijau turun itu merah
# 2. "invers": kebalikanya (naik = merah, turun=hijau)
# 3. "off": tidak menampilkan warna perubahan

# definisikan variable metrics
col1, col2, col3 = st.columns(3)

# menampilan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik dan buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") #netral

# menampilkan metric tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan