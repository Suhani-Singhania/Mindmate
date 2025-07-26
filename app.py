import streamlit as st
from datetime import datetime
import pandas as pd
import time

# --- User name input ---
user_name = st.text_input("👤 Enter your name (optional):", value="Guest").strip()
if user_name == "":
    user_name = "Guest"

# --- Title ---
st.title("🧠 MindMate – Your Calm Coding Companion")
st.markdown("#### ✨ *Helping minds untangle, one thought at a time.* ✨")
st.markdown("---")

# --- Mood Tracker ---
st.subheader("🌦 How are you feeling today?")
mood = st.selectbox("Pick your mood:", ["😊 Happy", "😐 Okay", "😔 Sad", "😠 Angry", "😰 Anxious", "🥱 Tired"])
reason = st.text_input("Optional: What's on your mind?")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Journal Entry ---
st.markdown("---")
st.subheader("📝 Journal Reflection")
journal_entry = st.text_area("Write your thoughts here...", height=200)

if st.button("📩 Submit Entry"):
    new_data = pd.DataFrame([{
        "Username": user_name,
        "Timestamp": timestamp,
        "Mood": mood,
        "Reason": reason,
        "Journal": journal_entry
    }])

    try:
        existing_data = pd.read_csv("mood_log.csv")
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        updated_data = new_data

    updated_data.to_csv("mood_log.csv", index=False)
    st.success(f"🌿 Entry saved! Thanks, {user_name}. You’re doing great.")

# --- Divider ---
st.markdown("---")

# --- Focus Timer ---
st.subheader("⏳ Focus Timer")
focus_minutes = st.slider("How many minutes do you want to focus?", 1, 60, 25)

if st.button("▶️ Start Focus Session"):
    with st.empty():
        for remaining in range(focus_minutes * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_display = f"{mins:02d}:{secs:02d}"
            st.markdown(f"""
                <div style='
                    font-size: 36px;
                    color: #294D61;
                    text-align: center;
                    padding: 15px;
                    border-radius: 10px;
                    background-color: #f0f5f9;
                    border: 1px solid #d4dce4;
                    margin: 20px 0;
                '>
                    🧘 Focus Time Remaining: <strong>{time_display}</strong>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

    st.audio("alarm.ogg", format="audio/ogg", start_time=0)
    st.success("🔔 Time’s up! Great job staying focused.")
    st.text_input("How do you feel after this session?", placeholder="e.g., Calm, tired, satisfied...")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:14px;'>🌸 Take care of your thoughts — they shape your days. – MindMate</div>", unsafe_allow_html=True)
