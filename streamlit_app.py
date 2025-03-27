import streamlit as st
from datetime import datetime

#Page configuration
st.set_page_config(
    page_title="My app",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

#Title
st.title("App: :green[prova 1] :cucumber:")

#Header
st.header("This is a header")
st.write("# This is also a header")
st.write("## This is a second header")
st.write("### This is a third header")

#Text
st.write("**Welcome** to my new *app*")
st.write("> this is a blockquote")

#HTML writing
st.markdown('<p style="color:yellow; font-size:20px;">this is yellow</p>', unsafe_allow_html=True)

#Slider
data = st.slider("Select a value", 0 , 100)
st.write("You selected:", data)

st.slider("select a range:", 0, 100, (30,70))

#Button
sport_list = ["Volleyball", "Football", "Basketball"]

if st.button("Sport", type="secondary"):
    st.write(sport_list)

#Checkbox
if st.checkbox("I like it!"):
    st.write("Thank you")
else:
    st.write("Oh noooo")

#Radio
st.radio("Which is your favourite sport?", sport_list)

#Selectbox
chosen=st.selectbox("Choose:", sport_list)

#Multiselect
chosen1=st.multiselect("Choose your sports:", sport_list)

#Calendar

st.date_input("Select date range:",value=(datetime(2025,3,15),datetime(2025,5,30)))

