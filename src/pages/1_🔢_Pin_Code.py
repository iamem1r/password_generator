import streamlit as st
from src.password_generator import PinGenerator
import time

st.image("src/images/banner.png", width=350)
st.header("Pin Code")
st.sidebar.write("""
    Generate a Personal Identification Number (PIN)
    for quick and convenient access. Ideal for
    scenarios where a numeric code is preferred,
    such as unlocking a device or accessing a secure area.
""")

length_of_pin = st.number_input(
    "Select the number of digits for your PIN code:",
    min_value=1, max_value=100, step=1)

on_click = st.button("Generate PIN Code")


if on_click:
    pin = PinGenerator(length=length_of_pin)
    pin_code = pin.generate()
    with st.spinner("Genrating PIN Code..."):
        time.sleep(3)
    st.subheader("Pin Code is ready")
    st.warning(pin_code)
