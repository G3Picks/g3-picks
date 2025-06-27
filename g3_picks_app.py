
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="G3 Picks", layout="wide")

# Load users
with open("users.json", "r") as f:
    users = json.load(f)

# Styling
st.markdown("""
    <style>
        body { background-color: #0f0f0f; color: #fff; font-family: 'Poppins', sans-serif; }
        .header { font-size: 48px; color: #FFD700; font-weight: bold; }
        .sub { font-size: 18px; color: #AAAAAA; margin-bottom:  30px; }
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 0 15px rgba(0,255,208,0.1);
        }
        .ev-tag { color: #00FFD0; font-weight: bold; }
        .section-title { font-size: 24px; margin-top: 40px; color: #FFD700; }
    </style>
""", unsafe_allow_html=True)

# Login logic
email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Login"):
    user = users.get(email)
    if user and user['password'] == password:
        st.session_state['user'] = email
    else:
        st.sidebar.error("Invalid credentials")

# Logged in view
if 'user' in st.session_state:
    st.markdown("<div class='header'>G3 Picks</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Big Dawgs Top Daily Sportsbook Picks</div>", unsafe_allow_html=True)

    st.sidebar.success(f"Logged in as {st.session_state['user']}")

    st.markdown("<div class='section-title'>🔥 Today's Top Picks</div>", unsafe_allow_html=True)
    top_picks = [
        {"player": "Jayson Tatum", "prop": "Over 27.5 Points", "ev": "+12.5%"},
        {"player": "Steph Curry", "prop": "Over 4.5 3PM", "ev": "+10.2%"},
        {"player": "Luka Doncic", "prop": "Over 9.5 Assists", "ev": "+9.8%"},
    ]
    for pick in top_picks:
        st.markdown(f"<div class='card'><b>{pick['player']}</b><br>{pick['prop']}<br><span class='ev-tag'>EV: {pick['ev']}</span></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>📈 Active Odds</div>", unsafe_allow_html=True)
    odds_df = pd.DataFrame({
        "Player": ["Booker", "Embiid", "Butler"],
        "Prop": ["Over 5.5 AST", "Over 11.5 REB", "Over 21.5 PTS"],
        "PrizePicks": ["-115", "-110", "-120"],
        "Book Odds": ["+105", "+100", "+110"],
        "EV": ["+7.2%", "+5.9%", "+6.4%"]
    })
    st.dataframe(odds_df)

else:
    st.markdown("<div class='header'>G3 Picks</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Please log in to view today's best sportsbook props.</div>", unsafe_allow_html=True)
