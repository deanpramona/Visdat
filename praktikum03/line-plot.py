import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', ' Apr', 'Mei', 'Juni', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']
product_a_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_b_sales  = [2,10,8,17,2,6,7,50,30,20,15,17]

# layout streamlit
st.title('Visualisasi Penjualan Produk')
st.sidebar.header('Pengaturan Grafik')
option = st.sidebar.selectbox('Pilih Tipe Visualisasi', ('Single Line Plot', "Multiple & Customization", "Jenis Garis Untuk Menunjukan Tren", "Subplot"))

# Menampilkan Identitas Kelompok
st.title("Praktikum 3 Visualisasi Data")
st.caption("Bagian 1 - Matplotlib")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months,product_a_sales, label='Product A')

    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)


# multiple line
def customize_plot():
    fig, ax = plt.subplots()
    ax.plot(months,product_a_sales, label='Product A', linestyle="--", marker='o', color='blue')
    ax.plot(months,product_b_sales, label='Product B', linestyle="-", marker='x', color='red')
    
    ax.set_title('Penjualan Produk per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid('True')
    st.pyplot(fig)

# Dataset C dan D
product_c_sales= [12,3,45,3,26,67,48,59,34,24,78,56]
product_d_sales = [4,6,7,23,67,24,15,26,18,19,50,47]

# tren line
def tren_line():
    fig, axs = plt.subplots()
    axs.plot(months,product_c_sales, label='Product C', linestyle=":",  color='green')
    axs.plot(months,product_d_sales, label='Product D', linestyle="-.",  color='purple')

    axs.set_title('Penjualan Produk per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid('True')
    st.pyplot(fig)

# subplot
def subplot():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # plot pertama untuk produk c
    axs[0].plot(months, product_c_sales, label="Product C", color='green', marker='d')
    axs[0].set_title('Penjualan Produk C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid('True')

    # plot pertama untuk produk d
    axs[1].plot(months, product_d_sales, label="Product D", color='purple', marker='s')
    axs[1].set_title('Penjualan Produk D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid('True')

    plt.tight_layout()
    st.pyplot(fig)

    

# logika untuk menampikan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customization":
    customize_plot()
elif option == "Jenis Garis Untuk Menunjukan Tren":
    tren_line()
elif option == "Subplot":
    subplot()