import streamlit as st

with st.form("user_form"):
    name=st.text_input("Full Name:", placeholder="Enter your name...")
    age=st.number_input("Age:", min_value=1,max_value=100, value=25, step=1)
    gender=st.selectbox("Gender:", ["Select and option", "Male", "Female", "Other"])
    submitted=st.form_submit_button("Submit")

if submitted:
    if name and gender != "Select an option":
        st.success(f"Form successfully submitted:\n\n**Name:** {name}\n**Age:** {age}\n**Gender:** {gender}")
    else:
        st.warning("Something went wrong!")