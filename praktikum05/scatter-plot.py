import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# dataset
suhu = [20, 24, 25, 26, 30, 33, 37, 39, 40]
penjualan = [50, 60, 70, 80, 90, 100, 110, 120, 130]

# dataset tambahan (data penjualan)
sale_weekdays = [50, 60,70, 80,90,100,105,110, 120]
sale_weekends = [60, 70, 85, 90, 100, 110, 120, 130, 140]

# data untuk analisis
data = {
    'Suhu': [20, 24, 25, 26, 30, 33, 37, 39, 40],
    'Sale_Coklat': [40,45,50,55,60,65,70,75,80],
    'Sale_Vanila':[82,80,84,88,90,95,97, 98, 99],
    'Sale_Strawberry': [55, 50,55, 60,65,60,65,70,72],
    'kelembapan' : [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# konversi ke dataframe
df = pd.DataFrame(data)

# layout utama
# Menampilkan Identitas Kelompok
st.title("Praktikum 5 Visualisasi Data - Scatter Plot")

# menu di sidebar
st.title('Visualisasi Penjualan Produk')
st.sidebar.header('Pengaturan Visualisasi')
option = st.sidebar.selectbox('Pilih Contoh Scatter Plot', ('Basic Scatter Plot', "Kustomisasi Scatter Plot", "Multiple Scatter Plot", "Analisis Scatter Plot"))

# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

# 1 BASIC SCATTER PLOT
def basic_scatter():
    st.subheader('1. Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2 KUSTOMISASI SCATTER PLOT
def custom_scatter():
    st.subheader('2. Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black',  alpha=0.7)
    ax.set_title('Hubungan penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3 MULTIPLE SCATTER PLOT
def multiple_scatter():
    st.subheader('3. Multiple Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, sale_weekdays, color='green', s=80, label='Weekdays')
    ax.scatter(suhu, sale_weekends, color='purple', s=80, label='Weekends')
    ax.set_title('Hubungan penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 4 ANALISIS SCATTER PLOT
def scatter_3_variable():
    st.subheader('4. Analisis Scatter Plot')

    # opsi jenis es krim
    jenis_eskrim = st.selectbox('Pilih Jenis Eskrim', ['Coklat', 'Vanila', 'Strawberry'])

    # logika untuk opsi jenis es krim berdasarkan pilihan
    if jenis_eskrim == 'Coklat':
        penjualan = df['Sale_Coklat']
    elif jenis_eskrim == 'Vanila':
        penjualan = df['Sale_Vanila']
    else:
        penjualan = df['Sale_Strawberry']

    st.subheader('Data Penjualan dan Suhu')
    st.dataframe(df)

    # SCATTER PLOT
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # styling
    ax.set_title('Hubungan Penjualan, Suhu, dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # ringkasan hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik Menunjukan antara Suhu, Kelembapan, dan Penjualan Es Krim ** {jenis_eskrim} **')


# routing berdasarkan menu
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == 'Kustomisasi Scatter Plot':
    custom_scatter()
elif option == 'Multiple Scatter Plot':
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variable()