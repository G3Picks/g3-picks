
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="G3 Picks", layout="wide")

# Login System
with open("users.json", "r") as f:
    users = json.load(f)

def login(email, password):
    user = users.get(email)
    return user and user["password"] == password

# UI
st.markdown("<h1 style='color:#FFD700;'>G3 Picks</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#AAAAAA;'>Big Dawgs Top Daily Sportsbook Picks</h4>", unsafe_allow_html=True)

email = st.text_input("Email")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if login(email, password):
        st.success("Logged in as " + email)
        st.write("Here would be the picks dashboard...")
    else:
        st.error("Invalid credentials.")
