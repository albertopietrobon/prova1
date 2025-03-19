import streamlit as st

#Page configuration
st.set_page_config(
    page_title="My app",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

#Title
st.title("App: :blue[prova 1]")

#Header
st.header("This is a header")
st.write("# This is also a header")
st.write("## This is a second header")
st.write("### This is a third header")

#Text
st.write("**Welcome** to my new *app*")
st.write("> this is a blockquote")

#Slider
data = st.slider("Select a value", 0 , 100)
st.write("You selected:", data)

#Button
sport_list = ["Volleyball", "Football", "Basketball"]

if st.button("Sport", type="primary"):
    st.write(sport_list)

#Radio
st.radio("Which is your favourite sport?", sport_list)