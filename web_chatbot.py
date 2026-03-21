import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. UI & DESIGN (CLEAR NEON TEXT)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Ultra Max", page_icon="🎤", layout="wide")

bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", 
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .main-card {{
        background: rgba(0, 0, 0, 0.85); border: 2px solid #00ffcc;
        border-radius: 20px; padding: 20px; text-align: center; color: white;
        box-shadow: 0 0 20px #00ffcc; margin-bottom: 20px;
    }}
    .bot-msg {{
        background: rgba(0, 0, 0, 0.95); color: #00ffcc !important; 
        padding: 18px; border-radius: 15px; border-left: 5px solid #00ffcc;
        font-size: 1.1em; font-weight: bold; text-shadow: 2px 2px 4px #000;
        margin-bottom: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }}
    .user-msg {{
        background: rgba(255, 255, 255, 0.15); color: white !important; 
        padding: 12px; border-radius: 10px; text-align: right;
        margin-bottom: 10px; font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MEGA BRAIN (SUBJECTS + LEVELS + QUIZ)
# ==========================================
knowledge = {
    "Maths Expert": {
        "Medium ⚙️": "Square area is Side*Side. Triangle sum is 180°.",
        "Thinking 🤔": "Heron's Formula: Area = √[s(s-a)(s-b)(s-c)].",
        "Pro 🔥": "If x+1/x=3, then x²+1/x² = 7. Volume of Sphere = 4/3πr³."
    },
    "Science Lab": {
        "Medium ⚙️": "Cell is life's unit. Water is H2O.",
        "Thinking 🤔": "Newton's 2nd Law: F = ma. Gravity on Earth is 9.8 m/s².",
        "Pro 🔥": "Mitochondria has its own DNA. Speed of light is 3*10^8 m/s."
    }
}

def get_ultra_response(q, level, sub):
    q = q.lower()
    # Identity
    if any(w in q for w in ["kaun", "who", "name"]):
        return "Mera naam YashProBot.ai hai! Mujhe Yash Tiwari (Class 9-B) ne banaya hai."
    
    # Knowledge Search
    for key, val in knowledge.get(sub, {}).items():
        if level == key:
            if "pucho" in q or "tell" in q or "batao" in q:
                return f"[{level}] {sub} Knowledge: {val}"

    # Default Quiz Logic
    if "quiz" in q or "question" in q or "sawal" in q:
        return f"Chaliye {sub} ka {level} test shuru karte hain! Kya aap taiyar hain?"

    return f"Jai Shree Ram! Yash Tiwari ke bot ne suna: '{q}'. Main {sub} mein {level} par kaam kar raha hoon."

# ==========================================
# 3. SIDEBAR (LEVEL & MIKE CONTROLS)
# ==========================================
with st.sidebar:
    st.markdown("<div class='main-card'>👑 YASH TIWARI</div>", unsafe_allow_html=True)
    st.metric("🏆 Score", st.session_state.score)
    st.markdown("---")
    
    # LEVEL SELECTION (Wapas aa gaya!)
    level_opt = st.selectbox("🧠 Level Change", ["Medium ⚙️", "Thinking 🤔", "Pro 🔥"])
    sub_opt = st.selectbox("📚 Subject Select", ["Maths Expert", "Science Lab", "SST & GK"])
    
    st.markdown("---")
    st.success("🎤 Mike: Active & Talking")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    if st.button("🌲 Change Background"):
        st.session_state.bg = random.choice(bgs)
        st.rerun()

# ==========================================
# 4. CHAT ENGINE (MIKE & VOICE)
# ==========================================
st.markdown("<div class='main-card'><h1>🤖 YashProBot.ai Ultra</h1><p>Level: "+level_opt+" | Subject: "+sub_opt+"</p></div>", unsafe_allow_html=True)

for m in st.session_state.chat:
    msg_style = "user-msg" if m["role"] == "user" else "bot-msg"
    st.markdown(f"<div class='{msg_style}'>{m['content']}</div>", unsafe_allow_html=True)

# User Input
u_input = st.chat_input("Level aur Subject chun kar kuch bhi puchiye...")

if u_input:
    st.session_state.chat.append({"role": "user", "content": u_input})
    
    # Brain Processing with Level & Subject
    ans = get_ultra_response(u_input, level_opt, sub_opt)
    st.session_state.chat.append({"role": "bot", "content": ans})
    
    # MIKE / VOICE (Har answer ke baad auto-play)
    try:
        tts = gTTS(text=ans[:150], lang='hi')
        af = io.BytesIO()
        tts.write_to_fp(af)
        st.audio(af, format='audio/mp3', autoplay=True)
    except: pass
    
    st.rerun()
