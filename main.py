import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, 1, help="Select days to forecast")
view = st.selectbox("Select Data to View", ('Temperature', 'Sky'))

if place:
    st.subheader(f"{view} for the next {days} days in {place}")
    data = backend.get_data(place, days)
    dates = [item['dt_txt'] for item in data]
    if view == "Temperature":
        temperatures = [item['main']['temp']/10 for item in data]
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)
    if view == "Sky":
        sky = [item['weather'][0]['main'] for item in data]
        imagespaths = ["images/"+item.lower()+".png" for item in sky]
        st.image(imagespaths, width=100, caption=dates)




