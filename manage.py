import streamlit as st
st.set_page_config(layout="wide")
st.title("Student Management")
st.sidebar.title("Fee Management")
st.sidebar.subheader("Add Student")
rollnumber= st.sidebar.number_input("Rollnumber")
name = st.sidebar.number_input("Name")
fees = st.sidebar.number_input("Fees")
add = st.sidebar.button("Add")
