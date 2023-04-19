import streamlit as st 

st.write( "# Largest Number Finder App")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")
num3 = st.number_input("Enter Third Number")

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

st.subheader("The maximum of above given given numbers is", max_num)
