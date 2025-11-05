# import library streamlit
import streamlit as st
import altair as slt

# Menampilkan Identitas Kelompok
st.title("Praktikum 1 Visualisasi Data")
st.write("Bagian 3 - Data dan Media Elements")
# Menampilkan Identitas Kelompok
st.markdown("""
    1. Dean Pramona - 0110122163
    2. Fatih Mubasyir - 0110222186
    3. Hisyam Wildan Alfatih - 0110222206
""")

# DISPLAYING IMAGE 
# Menampilkan 1 Gambar 
st.write('Displaying an Images')
# Menampilkan gambar dari lokal
st.image('D:/Praktikum Visdat/assets/bowi2.jpg')
#Image Courtesy by National Wildlife Federation
st.caption("Image Courtesy: National Animal Yang Aku Suka")

# Menampilkan banyak gambar
st.write("Diplaying Multiple Images")
# Untuk menampilkan banyak gambar buat dulu variable
animal_images = [
    'D:/Praktikum Visdat/assets/bowi.jpg',
    'D:/Praktikum Visdat/assets/bowi2.jpg',
    'D:/Praktikum Visdat/assets/cat.jpeg',
    'D:/Praktikum Visdat/assets/hyena.jpg',
    'D:/Praktikum Visdat/assets/tiger.jpeg',
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.caption("Image Courtesy: National Animal Yang Aku Suka")

# BACKGROUND IMAGE
import base64

# Function untuk membuat Image menjadi Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())

    st.markdown(
    f""" 
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
   unsafe_allow_html=True
    )

st.write("Background Image: Pokonya ini foto BG")
# Panggil Image dalam function
add_local_background_image('D:/Praktikum Visdat/assets/bg.jpg')

# RESIZING AN IMAGE (Mengubah Ukuran Gambar)
from PIL import Image

# Menampilkan gambar asli
original_image = Image.open("D:/Praktikum Visdat/assets/fox.jpeg")
# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((300, 300))

# Menampilkan Resized Image
st.title("Resized Image")
st.image(resized_image)