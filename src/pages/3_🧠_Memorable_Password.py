import streamlit as st
from src.password_generator import MemorablePasswordGenerator
import time

st.image("src/images/banner.png", width=350)
st.header("Memorable Password")
st.sidebar.write("""
    Craft a password that is both strong and easy to remember. This method
    generates a memorable combination of words or phrases,
    striking the perfect balance between security and user convenience.
    Ideal for users who prioritize both security and ease of recall.
""")

num_of_words = st.slider(
    "Select the number of digits for your PIN code:")
separator = st.text_input(
    label="What is your sepator?",
    max_chars=3
)
capitalize = st.toggle("Do you want to capitalize you password?")

on_click = st.button("Generate PIN Code")

memorable_password = MemorablePasswordGenerator(
    num_of_words=num_of_words,
    separator=separator,
    capitalize=capitalize
)

memorable_pass = memorable_password.generate()

if on_click:
    with st.spinner("Generating Password..."):
        time.sleep(3)
    st.subheader("Memorable Password is ready")
    st.warning(memorable_pass)
