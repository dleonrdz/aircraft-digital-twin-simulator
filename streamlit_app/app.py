import streamlit as st
from aircraft_digital_twin_simulator.app import get_aircraft_maintenance_response

st.title("Aircraft Maintenance Assistance")

aircraft_id = st.text_input("Please enter the aircraft id (format: AC-###):")

if st.button("Get Maintenance Report"):
    if aircraft_id:
        response = get_aircraft_maintenance_response(aircraft_id)
        st.text_area("Maintenance Report", response, height=300)
    else:
        st.warning("Please enter an aircraft id.")
