
import streamlit as st
import pandas as pd
import json
import time

st.set_page_config(page_title="G3 Picks", layout="wide")

# --- Style ---
st.markdown("""
    <style>
    body { background-color: #0f0f0f; }
    .big-header { color: #FFD700; font-size: 48px; font-weight: bold; }
    .sub-header { color: #AAAAAA; font-size: 20px; margin-bottom: 20px; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        color: #fff;
    }
    .ev-tag {
        color: #00FF9D;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Auth ---
with open("users.json", "r") as f:
    users = json.load(f)

def login(email, password):
    user = users.get(email)
    return user and user["password"] == password

# --- Login ---
email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Login"):
    if login(email, password):
        st.session_state["logged_in"] = True
        st.session_state["email"] = email
    else:
        st.sidebar.error("Invalid credentials")

# --- Logged in view ---
if st.session_state.get("logged_in"):
    st.markdown("<div class='big-header'>G3 Picks</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Big Dawgs Top Daily Sportsbook Picks</div>", unsafe_allow_html=True)

    st.sidebar.success(f"Logged in as {st.session_state['email']}")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())

    # --- Filters ---
    with st.sidebar:
        st.markdown("### Filters")
        st.selectbox("Sport", ["All", "NBA", "MLB", "NFL"])
        st.selectbox("Stat", ["All", "Points", "Rebounds", "Hits", "Passing Yards"])
        st.slider("EV% Threshold", 0, 50, 10)

    # --- Mock Top 5 Picks ---
    st.markdown("### 🔥 Today's Top 5 Picks")
    picks = [
        {"player": "LeBron James", "prop": "Over 7.5 assists", "line": "+120", "ev": "+14.5%"},
        {"player": "Shohei Ohtani", "prop": "Over 1.5 Total Bases", "line": "+115", "ev": "+12.1%"},
        {"player": "Jalen Brunson", "prop": "Over 25.5 points", "line": "+110", "ev": "+10.8%"},
        {"player": "Ronald Acuña Jr.", "prop": "Over 0.5 HR", "line": "+240", "ev": "+9.2%"},
        {"player": "Nikola Jokic", "prop": "Over 11.5 rebounds", "line": "+105", "ev": "+8.7%"},
    ]
    for pick in picks:
        st.markdown(f"<div class='glass-card'>"
                    f"<b>{pick['player']}</b><br>"
                    f"{pick['prop']} @ <b>{pick['line']}</b><br>"
                    f"<span class='ev-tag'>Expected Value: {pick['ev']}</span>"
                    "</div>", unsafe_allow_html=True)

    # --- Mock Top Current Active Odds ---
    st.markdown("### 📈 Top Current Active Odds")
    odds_df = pd.DataFrame({
        "Player": ["Devin Booker", "Aaron Judge", "Justin Jefferson"],
        "Prop": ["Over 5.5 assists", "Over 1.5 hits", "Over 90.5 yards"],
        "PrizePicks": ["-115", "-120", "-110"],
        "Best Book Odds": ["+100", "+105", "+110"],
        "EV %": ["+7.1%", "+5.8%", "+4.9%"]
    })
    st.dataframe(odds_df.style.set_properties(**{
        'background-color': '#111',
        'color': 'white',
        'border-color': 'white'
    }), height=250)

else:
    st.markdown("<div class='big-header'>G3 Picks</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Login to view daily value picks.</div>", unsafe_allow_html=True)
