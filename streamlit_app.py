import streamlit as st 

st.write( "#Largest Number Finder App")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

print("The maximum number is", max_num)
