import streamlit as st
from riddleapp import *
from sciencequiz import *
from greekapp import *
from pythonquiz import *

st.markdown("""
<style>
.stApp{
    background-color: black;
}
<style>
""",unsafe_allow_html=True)


st.title("GENERAL QUIZ")
user_entry = st.radio("Choose Your Options:", ["Science & Nature", "Greek Mythology", "Riddle", "Python"])

if user_entry == "Riddle":
    riddle()
elif user_entry == "Science & Nature":
    science()
elif user_entry == "Greek Mythology":
    greek()
elif user_entry == "Python":
    python()


