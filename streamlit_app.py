import streamlit as st 

st.write( "# Largest Number Finder App")

num1 = st.number_input("FN")
num2 = st.number_input("SN")
num3 = st.number_input("TN")

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

print("The maximum number is", max_num)
