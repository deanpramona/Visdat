import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Menampilkan Identitas Kelompok
st.title("Praktikum 3 Visualisasi Data")
st.caption("Bagian 1 - Matplotlib")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

# data
data = {
    'jurusan': ['Ilmu Komputer', 'Teknik Informatika', 'Sistem Informasi', 'Data Science'],
    'jumlah mahasiswa': [120,150,100,80]
}

df = pd.DataFrame(data)

# streamlit barchart
st.title('Basic Bar Chart - Jumlah Mahasiswa Per Jurusan')
st.bar_chart(df.set_index('jurusan'))

# matplotlib bar chart
st.title('Basic Bar Chart Menggunakan Matplotlib')
fig, ax = plt.subplots()
ax.bar(data['jurusan'], data['jumlah mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticklabels(data['jurusan'], rotation=20)
st.pyplot(fig)

# kustomisasi matplotlib bar chart 
st.title("Kustomisasi Bar Chart")
fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'red']
bars = ax.bar(data['jurusan'], data['jumlah mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            str(bar.get_height()), ha='center')
st.pyplot(fig)

# bultiple bar chart
st.title('Multiple Bar Chart')

# data tambahan
data_2023 = [120,150,100,80]
data_2024 = [140,160, 110, 90]

x = range(len(data['jurusan']))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='green')

ax.set_title('Jumlah Mahasiswa Per Jurusan (2023 vc 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width/2 for p in x])
ax.set_xticklabels(data['jurusan'])
ax.legend()
st.pyplot(fig)