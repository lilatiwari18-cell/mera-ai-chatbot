import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. UI & DESIGN (CLEAR NEON GLASS LOOK)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Final Boss", page_icon="💎", layout="wide")

# High-Res Nature Backgrounds
bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", # Dark Forest
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9", # Canopy
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"  # Sunlight
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

# Custom CSS for Design & Clear Text
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .glass-card {{
        background: rgba(0, 0, 0, 0.85); 
        border: 2px solid #00ffcc;
        border-radius: 25px; 
        padding: 25px; 
        text-align: center; 
        color: white;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.4);
        margin-bottom: 20px;
    }}
    .bot-bubble {{
        background: linear-gradient(135deg, rgba(0,255,204,0.2), rgba(0,0,0,0.95));
        color: #00ffcc !important; 
        padding: 18px; 
        border-radius: 15px 15px 15px 0px; 
        border-left: 5px solid #00ffcc;
        font-size: 1.1em; 
        font-weight: bold;
        margin-bottom: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }}
    .user-bubble {{
        background: rgba(255, 255, 255, 0.15); 
        color: white !important; 
        padding: 12px; 
        border-radius: 15px 15px 0px 15px; 
        text-align: right;
        margin-bottom: 15px; 
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. THE KNOWLEDGE ENGINE (LEVELS & SUBJECTS)
# ==========================================
@st.cache_data
def get_mega_brain():
    return {
        "Maths Expert": {
            "Medium ⚙️": "Circle Area = πr². Rectangle = L×B.",
            "Thinking 🤔": "Heron's Formula: √[s(s-a)(s-b)(s-c)].",
            "Pro 🔥": "If x+1/x=3, then x²+1/x²=7. Sphere Vol = 4/3πr³."
        },
        "Science Lab": {
            "Medium ⚙️": "Cell is life's unit. Water formula is H2O.",
            "Thinking 🤔": "Force F = m×a. Earth Gravity g = 9.8 m/s².",
            "Pro 🔥": "Speed of light is 3x10^8 m/s. DNA is in Nucleus."
        },
        "SST & GK": {
            "Medium ⚙️": "Narendra Modi is India's PM. Delhi is the Capital.",
            "Thinking 🤔": "Article 370 was in Kashmir. Patel is Iron Man.",
            "Pro 🔥": "India became Republic on 26 Jan 1950. Asia is largest."
        }
    }

data = get_mega_brain()

def get_response(q, level, sub):
    q = q.lower()
    if any(w in q for w in ["kaun", "who", "name"]):
        return "Mera naam YashProBot.ai hai! Mujhe Class 9-B ke software star Yash Tiwari ne banaya hai."
    
    subject_db = data.get(sub, data["SST & GK"])
    if any(w in q for w in ["batao", "tell", "what", "pucho", "info"]):
        return f"💡 [{level}] {sub} Info: " + subject_db.get(level, "Seeking more data...")

    if any(w in q for w in ["quiz", "question", "sawal", "test"]):
        return f"🌟 {sub} ({level}) Quiz: Kya aap taiyar hain? Jawab likhein!"

    return f"Jai Shree Ram! Aapne {sub} mein {level} par '{q}' pucha. Yash Tiwari ka bot seekh raha hai!"

# ==========================================
# 3. SIDEBAR CONTROLS (LEVEL & SUBJECT)
# ==========================================
with st.sidebar:
    st.markdown("<div class='glass-card' style='padding:10px;'>👑 YASH TIWARI</div>", unsafe_allow_html=True)
    st.write("**Section:** 9-B | KV Salempur")
    st.metric("🏆 Your Score", st.session_state.score)
