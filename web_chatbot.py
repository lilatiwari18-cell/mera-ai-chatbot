import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. THE DESIGNER INTERFACE (PRO LOOK)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Ultra Boss", page_icon="⚡", layout="wide")

# High-Res Nature Backgrounds
bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", # Dark Forest
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9", # Tree Canopy
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e", # Sunlight Forest
    "https://images.unsplash.com/photo-1473448912268-2022ce9509d8"  # Autumn Trees
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

# Neon Glassmorphism CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .main-box {{
        background: rgba(0, 0, 0, 0.8); border: 2px solid #00ffcc;
        border-radius: 20px; padding: 25px; text-align: center;
        box-shadow: 0 0 20px #00ffcc; color: white;
    }}
    .chat-msg {{
        background: rgba(255, 255, 255, 0.1); padding: 12px;
        border-radius: 10px; margin: 10px 0; border-left: 4px solid #00ffcc;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. THE MEGA DATABASE (ALL SUBJECTS & LEVELS)
# ==========================================
data = {
    "Maths Expert": {
        "Medium ⚙️": [
            ("3x + 10 = 40. Find x.", "10"),
            ("Area of rectangle (L=5, B=4)?", "20"),
            ("Value of 2^5?", "32")
        ],
        "Thinking 🤔": [
            ("Heron's Formula: s if a=6, b=8, c=10.", "12"),
            ("Area of Triangle with sides 3, 4, 5.", "6"),
            ("Sum of angles in a Quadrilateral?", "360")
        ],
        "Pro 🔥": [
            ("If x + 1/x = 3, find x^2 + 1/x^2.", "7"),
            ("Volume of Sphere with radius 3 (use 22/7)?", "113.14"),
            ("Find x: (x-1)/2 = 5.", "11")
        ]
    },
    "Science Lab": {
        "Medium ⚙️": [("Powerhouse of Cell?", "mitochondria"), ("Formula of Salt?", "nacl")],
        "Thinking 🤔": [("SI unit of Force?", "newton"), ("Acid in Lemon?", "citric")],
        "Pro 🔥": [("Mass of Earth?", "6x10^24"), ("Discovery of Nucleus?", "rutherford")]
    },
    "SST & GK": {
        "Medium ⚙️": [("Capital of India?", "delhi"), ("Who is PM?", "modi")],
        "Thinking 🤔": [("Iron Man of India?", "patel"), ("First War of Independence?", "1857")],
        "Pro 🔥": [("Article 370 was in?", "kashmir"), ("Largest Continent?", "asia")]
    }
}

def get_answer(user_q, level, sub):
    q = user_q.lower()
    
    # 1. Identity Check
    if any(word in q for word in ["kaun", "who", "name"]):
        return f"Mera naam YashProBot.ai hai! Mujhe Class 9-B ke software star Yash Tiwari ne banaya hai. Main {sub} ka expert hoon!"

    # 2. Quiz Logic
    if any(word in q for word in ["quiz", "question", "sawal", "test"]):
        subject_data = data.get(sub, data["SST & GK"])
        level_data = subject_data.get(level, subject_data["Medium ⚙️"])
        ques, ans = random.choice(level_data)
        st.session_state.last_ans = ans
        return f"🌟 QUIZ TIME! 🌟\nQuestion: {ques}\n(Tip: Type the answer to get +10 points!)"

    # 3. Answering Logic (Checking last quiz)
    if 'last_ans' in st.session_state and st.session_state.last_ans.lower() in q:
        st.session_state.score += 10
        del st.session_state.last_ans
        return "🎉 SAHI JAWAB! Yash Tiwari proud of you. Aapko mile +10 Points!"

    # 4. Feature Check
    if "kya kar sakte ho" in q:
        return "Main Maths solve kar sakta hoon, Quiz le sakta hoon, Voice message bhej sakta hoon aur High-speed bina API ke chalta hoon!"

    return "Jai Shree Ram! Aapka sawal accha hai, par main abhi seekh raha hoon. Yash Tiwari se contact karein!"

# ==========================================
# 3. SIDEBAR & SCOREBOARD
# ==========================================
with st.sidebar:
    st.markdown("<div class='main-box' style='padding:10px;'>⚡ YASH-PRO-AI ⚡</div>", unsafe_allow_html=True)
    st.metric("🏆 Your Score", st.session_state.score)
    
    st.markdown("---")
    level = st.selectbox("🧠 Thinking Level", ["Medium ⚙️", "Thinking 🤔", "Pro 🔥"])
    subject = st.selectbox("📚 Subject Select", ["Maths Expert", "Science Lab", "SST & GK", "English Grammar"])
    
    st.markdown("---")
    st.markdown("🎵 **Amplifier x Safari Mode**")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    if st.button("🌲 Change Tree Background"):
        st.session_state.bg = random.choice(bgs)
        st.rerun()

# ==========================================
# 4. MAIN CHAT ENGINE
# ==========================================
st.markdown("<div class='main-box'><h1>🤖 Welcome Friend!</h1><p>The Ultimate Bot by Yash Tiwari</p></div>", unsafe_allow_html=True)

for m in st.session_state.chat:
    with st.container():
        st.markdown(f"<div class='chat-msg'><b>{m['role']}:</b> {m['content']}</div>", unsafe_allow_html=True)

u_input = st.chat_input("Type 'Give me a quiz' or talk to Yash's Bot...")

if u_input:
    st.session_state.chat.append({"role": "Yash Tiwari", "content": u_input})
    
    # Brain Processing
    bot_reply = get_answer(u_input, level, subject)
    st.session_state.chat.append({"role": "YashProBot", "content": bot_reply})
    
    # Voice Synthesis
    tts = gTTS(text=bot_reply[:150], lang='hi')
    af = io.BytesIO()
    tts.write_to_fp(af)
    st.audio(af, format='audio/mp3')
    
    st.rerun()
