# app.py
import streamlit as st
from satanic_calculator import SatanicCalculator  # Assuming you put your class in satanic_calculator.py

# Initialize calculator
if 'calc' not in st.session_state:
    st.session_state.calc = SatanicCalculator()

st.title("Satanic Calculator 😈 (For Fun Only)")

st.write("This calculator will always give you the wrong answer... intentionally.")

# User input
expression = st.text_input("Enter a math expression (e.g., 2 + 2):")

if st.button("Calculate"):
    if expression.strip() != "":
        response = st.session_state.calc.respond(expression)
        st.success(f"Response: {response}")
    else:
        st.warning("Please enter a valid expression.")

# Mode switcher
if st.button(f"Switch Mode (Current: {st.session_state.calc.mode})"):
    st.session_state.calc.switch_mode()
