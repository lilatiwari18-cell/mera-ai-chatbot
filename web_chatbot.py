import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. UI & DESIGN (CLEAR NEON TEXT & BACKGROUND)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Final Boss", page_icon="⚡", layout="wide")

# High-Res Tree Backgrounds
bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", # Dark Forest
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9", # Tree Canopy
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"  # Sunlight Forest
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

# Neon Glassmorphism CSS for better visibility
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .welcome-box {{
        background: rgba(0, 0, 0, 0.85); border: 2px solid #00ffcc;
        border-radius: 20px; padding: 20px; text-align: center; color: white;
        box-shadow: 0 0 20px #00ffcc; margin-bottom: 20px;
    {{
    .bot-msg {{
        background: rgba(0, 0, 0, 0.9); color: #00ffcc !important; 
        padding: 15px; border-radius: 15px; border: 2px solid #00ffcc;
        font-size: 1.1em; font-weight: bold; text-shadow: 2px 2px 4px #000;
        margin-bottom: 15px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
    }}
    .user-msg {{
        background: rgba(255, 255, 255, 0.2); color: white !important; 
        padding: 10px; border-radius: 10px; text-align: right;
        margin-bottom: 10px; font-weight: bold; text-shadow: 1px 1px 2px #000;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MEGA DATABASE (OFFLINE SECURE)
# ==========================================
@st.cache_data
def get_database():
    return {
        "Maths Expert": {
            "Medium ⚙️": [("3x + 10 = 40. Find x.", "10"), ("Area of rectangle (L=5, B=4)?", "20")],
            "Thinking 🤔": [("Heron's Formula: s if a=6, b=8, c=10.", "12"), ("Root of 144?", "12")],
            "Pro 🔥": [("If x + 1/x = 3, find x^2 + 1/x^2.", "7"), ("Volume of Sphere with radius 3 (use pi=3)?", "108")]
        },
        "Science Lab": {
            "Medium ⚙️": [("Powerhouse of Cell?", "mitochondria"), ("Formula of Salt?", "nacl")],
            "Thinking 🤔": [("SI unit of Force?", "newton"), ("Gas we breathe in?", "oxygen")],
            "Pro 🔥": [("Mass of Earth?", "6x10^24"), ("Discovery of Nucleus?", "rutherford")]
        },
        "SST & GK": {
            "Medium ⚙️": [("Capital of India?", "delhi"), ("Who is PM?", "modi")],
            "Thinking 🤔": [("Iron Man of India?", "patel"), ("First War of Independence?", "1857")],
            "Pro 🔥": [("Article 370 was in?", "kashmir"), ("Largest Continent?", "asia")]
        }
    }

data = get_database()

def get_answer(user_q, level, sub):
    q = user_q.lower()
    
    if any(w in q for w in ["kaun", "who", "name"]):
        return f"Mera naam YashProBot.ai hai! Mujhe Class 9-B ke software star Yash Tiwari ne banaya hai."

    if any(w in q for w in ["quiz", "question", "sawal"]):
        sub_data = data.get(sub, data["SST & GK"])
        lvl_data = sub_data.get(level, sub_data["Medium ⚙️"])
        ques, ans = random.choice(lvl_data)
        st.session_state.last_ans = ans
        return f"🌟 QUIZ TIME! 🌟\nQuestion: {ques}\n(Type answer for +10 points!)"

    if 'last_ans' in st.session_state and st.session_state.last_ans.lower() in q:
        st.session_state.score += 10
        del st.session_state.last_ans
        return "🎉 SAHI JAWAB! Yash Tiwari is proud of you. Aapko mile +10 Points!"

    if "kya kar sakte ho" in q:
        return "Main Maths solve kar sakta hoon, Quiz le sakta hoon, Voice message bhej sakta hoon aur Bina Net ke bhi chal sakta hoon!"

    return f"Jai Shree Ram! Yash Tiwari ke bot ne aapka sawal '{user_q}' sun liya hai. Quiz khelne ke liye 'Quiz' likhein."

# ==========================================
# 3. SIDEBAR (PROFILE, CONTROLS & MUSIC)
# ==========================================
with st.sidebar:
    st.markdown("<div style='background:rgba(0,255,204,0.2); padding:10px; border-radius:10px; border:1px solid #00ffcc; text-align:center;'>👑 YASH TIWARI</div>", unsafe_allow_html=True)
    st.write("Section: 9-B | KV Salempur")
    st.
