import streamlit as st
st.set_page_config(layout="wide")
st.sidebar.title("Menu")
st.sidebar.subheader("Choose an option")
st.title("Student Management")
st.sidebar.title("Fee Management")
st.sidebar.subheader("Add Student")
rollnumber= st.sidebar.number_input("Rollnumber")
name = st.sidebar.text_input("Name")
fees = st.sidebar.number_input("Fees")
add = st.sidebar.button("Add")

