# import library streamlit
import streamlit as st

# BAGIAN 1 - TEXT ELEMENT
# st.header("Praktikum 1 Text Element")  # header
# st.subheader("Ini SubHeader")  # subheader
# st.text("ini text biasa tanpa format")  # text biasa
# st.markdown("**ini bold** & *ini italic*") # untuk format text bold dan italic, ini untuk 1 baris
# st.markdown("""
    # - ini baris 
    # - ini menggunakan markdown multibaris
    # 1. ini baris 2
    # 2. ini menggunakan markdown multibaris
    # * ini baris 3 
    # * ini menggunakan markdown multibaris
# """)
# st.caption("ini caption") # buat bikin text kecil dibawah elemen
# st.title("ini judul")

# Latihan
st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 Text Element")
st.markdown("""
    1. Nama: Dean Pramona
    2. Nim: 0110122163
""")

# BAGIAN 2 - MENAMPILKAN RUMUS ATAU LATEX
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binominal

# BAGIAN 3 - MENAMPILKAN KODE PROGRAM
st.header("Displaying Code")
st.subheader("Python Code")

# cara 1
# simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!)
'''
# st.code() untuk menampilan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

# cara 2 langsung panggil st.code dan masukin kode 
st.subheader('Java Code')
st.code('''
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello World!);
        }
    }
''', language='java')

# Fugngsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti java, javascript, C++,HTML, DLL
st.header('JavaScript Java')
st.code('''
    <script>
    <p id="demo"><p>
    try {
        addalert("Welcome guest!); //kesalahan ketik (addalert)
        sengaja dibuat untuk menimbulkan eror
        }
    catch(err){
        document.getElementById("demo").innerHTML = err.message; //
        menampilkan pesan error di elemen HTML dengan id 'demo'
        }
    <script>
''', language='javascript')
# kode ini menunjukan contoh bagaimana menangani error (Exception) di Javascript
# hasilnya tidak dijalankan di streamlit, tapi ditampilkan sebagai contoh code