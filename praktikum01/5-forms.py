# import library yang dibutuhkan
import streamlit as st
import datetime
import pandas as pd

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 5: Forms")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# Text Box
st.title("Text Box")
# Creating Text box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

# Text Area
# Creating Text Area
input_text = st.text_area("Enter your Text")
# Printing Text Area
st.write("""You entered: \n""", input_text)

# Number Input
st.number_input("Enter a number")

# Creating Number Input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default value is 5, \n Step Size value is 2")
st.write("Total value after adding Numer entered with step value is:", num)

# Time
st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

# Date
st.title("Date")
# Defining Date Function
st.date_input("Select Date")

st.title("Date Time")
# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 2),
max_value=datetime.date(2005, 12, 1))

# Color Picker
st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

# Date Upload
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {"file_name": data_file.name, "file_type": data_file.type,
                        "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# Submit Button
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)