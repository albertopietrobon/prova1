import streamlit as st

#Title
st.title("App: prova 1")

#Text
st.write("Welcome to my new app")

#Data
data = st.slider("Select a value", 0 , 100)
st.write("You selected:", data)

