import streamlit as st
from src.password_generator import RandomPasswordGenerator
import time

st.image("src/images/banner.png", width=350)
st.header("Random Password")
st.sidebar.write("""
    Create a robust and unpredictable password using a mix of letters,
    numbers, and symbols. This method ensures a high level of
    security, making it suitable for various online accounts and applications.
""")

length_of_password = st.number_input(
    "Select the number of digits for your PIN code:",
    min_value=1, max_value=100, step=1)
include_numbers = st.toggle("Include Numbers")
include_symbols = st.toggle("Include Symbols")

on_click = st.button("Generate PIN Code")

random_password = RandomPasswordGenerator(
    length=length_of_password,
    include_numbers=include_numbers,
    include_symbols=include_symbols)

random_pass = random_password.generate()

if on_click:
    with st.spinner("Generating Random Password..."):
        time.sleep(3)
    st.subheader("Random Password is ready")
    st.warning(random_pass)