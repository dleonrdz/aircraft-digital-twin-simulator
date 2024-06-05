import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aircraft_digital_twin_simulator.app import get_aircraft_maintenance_response

st.title("Aircraft Maintenance Assistant")

# Add welcome message
st.write("Welcome to your AIrcaft Maintenance Assistant")

aircraft_id = st.text_input("Please enter the aircraft id (format: AC-###):")

# Create two empty columns for centering the button
col1, col2, col3 = st.columns([1, 2, 1])

response = ''
with col2:
    # Centered Get Maintenance Report button
    if st.button("Get Maintenance Report"):
        if aircraft_id:
            response = get_aircraft_maintenance_response(aircraft_id)
            st.session_state['response'] = response
        else:
            st.warning("Please enter an aircraft id.")

st.text_area("Maintenance Report", response, height=300)
