# import library yang dibutuhkan
import streamlit as st
import time

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 4: Buttons and Sliders")
st.markdown("""
    Kelompok 14:
    1. Fatih Mubasyir (0110222186)
    2. Hisyam Wildan Alfath (0110222206) 
    3. Dean Pramona (0110222163)
""")

# Buttons
st.title("Creating Buttons")
# Defining a Button
button = st.button("Click Here")
if button:
    st.write("You have clicked the button")
else:
    st.write("You have not clicked the button")

# Radio Buttons
st.title("Creating Radio Buttons")
# Defining Radio Buttons
gender = st.radio(
"Select your Gender", 
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write('You have selected Female.')
else:
    st.write('You have selected Others.')

# Check Boxes
st.title('Creating Checkboxes')
st.write('Select your Hobbies')
# Defining Check Boxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Drop-Downs
st.title('Creating Dropdowns')
# Creating Dropdown
country = st.selectbox('Select your hobby',
('Books', 'Movies', 'Sports')) 

# Multiselects
st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/Tv Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

# Download Buttons
# st.header("Download Button")
# downLoad = st.download_button(
# label = "Download Image",
# data =open("assets/cat.jpeg", "rb"),
# file_name = "cat.jpeg",
# mime = "image/jpeg"
# )

# Progress Bars
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

# Spinners
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')