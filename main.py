import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, 1, help="Select days to forecast")
view = st.selectbox("Select Data to View", ('Temperature', 'Sky'))
st.subheader(f"{view} for the next {days} days in {place}")


data = backend.get_data(place,days,view)



dates,temperatures = get_data(days)
figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)