import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, 1,help="Select days to forecast")
view = st.selectbox("Select Data to View", ('Temperature', 'Sky'))

st.subheader(f"{view} for the next {days} days in {place}")

