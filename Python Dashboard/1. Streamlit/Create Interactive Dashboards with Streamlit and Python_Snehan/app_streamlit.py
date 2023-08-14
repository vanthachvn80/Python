# app_streamlit.py
import streamlit as st

# Title of the dashboard
st.title("My Interactive Dashboard")

# A slider widget
age = st.slider("Select your age:", 0, 100, 25)

# A text input widget
name = st.text_input("Enter your name:", "John Doe")

# Displaying the selected values
st.write(f"Hello {name}, you are {age} years old.")
