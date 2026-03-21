import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. UI & DESIGN (NEON & CLEAR TEXT)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Knowledge Hub", page_icon="🧠", layout="wide")

bgs = ["https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", "https://images.unsplash.com/photo-1502082553048-f009c37129b9"]
if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

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
    }}
    .bot-msg {{
        background: rgba(0, 0, 0, 0.9); color: #00ffcc !important; 
        padding: 15px; border-radius: 15px; border: 2px solid #00ffcc;
        font-size: 1.1em; font-weight: bold; text-shadow: 2px 2px 4px #000;
        margin-bottom: 15px;
    }}
    .user-msg {{
        background: rgba(255, 255, 255, 0.2); color: white !important; 
        padding: 10px; border-radius: 10px; text-align: right; font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MEGA BRAIN (QUIZ + KNOWLEDGE BASE)
# ==========================================
knowledge_base = {
    "science": {
        "cell": "Cell is the basic structural and functional unit of life. Mitochondria is its powerhouse!",
        "force": "Force is a push or pull. Formula: F = m × a (Mass × Acceleration).",
        "water": "Water formula is H2O. It freezes at 0°C and boils at 100°C.",
        "atom": "Atom is the smallest unit of matter, made of protons, neutrons, and electrons."
    },
    "maths": {
        "heron": "Heron's Formula: Area = √[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2.",
        "triangle": "A triangle has 3 sides and the sum of its angles is always 180 degrees.",
        "square": "Area of Square = Side × Side. Perimeter = 4 × Side.",
        "pi": "The value of Pi (π) is approximately 3.14 or 22/7."
    },
    "sst": {
        "gandhi": "Mahatma Gandhi is the Father of the Nation. He led the Dandi March and Quit India movement.",
        "constitution": "The Indian Constitution was written by Dr. B.R. Ambedkar and adopted on 26 Jan 1950.",
        "earth": "Earth is the 3rd planet from the Sun and the only one with life."
    }
}

def get_answer(user_q):
    q = user_q.lower()
    
    # 1. Identity
    if any(w in q for w in ["kaun", "who", "name"]):
        return "Mera naam YashProBot.ai hai! Mujhe Class 9-B ke Yash Tiwari ne banaya hai."

    # 2. Knowledge Search (Har subject ka answer)
    for subject in knowledge_base:
        for keyword in knowledge_base[subject]:
            if keyword in q:
                return f"💡 {subject.upper()} INFO: " + knowledge_base[subject][keyword]

    # 3. Quiz Trigger
    if "quiz" in q or "question" in q:
        return "🌟 QUIZ MODE: Chaliye 'Science' ya 'Maths' ka ek sawal puchiye!"

    return f"Jai Shree Ram! Yash Tiwari ke bot ne suna: '{user_q}'. Main abhi seekh raha hoon, par aap 'Cell', 'Force', ya 'Heron' ke baare mein puch sakte hain!"

# ==========================================
# 3. SIDEBAR & INTERFACE
# ==========================================
with st.sidebar:
    st.markdown("<div class='welcome-box' style='padding:10px;'>👑 YASH TIWARI</div>", unsafe_allow_html=True)
    st.write("Section: 9-B | KV Salempur")
    st.metric("🏆 Score", st.session_state.score)
    st.markdown("---")
    st.success("🎤 Mike: Ready")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    if st.button("🌲 Change Tree"):
        st.session_state.bg = random.choice(bgs)
        st.rerun()

st.markdown("<div class='welcome-box'><h1>🤖 YashProBot.ai</h1><p>Knowledge Hub for All Subjects</p></div>", unsafe_allow_html=True)

for m in st.session_state.chat:
    div_class = "user-msg" if m["role"] == "user" else "bot-msg"
    label = "👤 You" if m["role"] == "user" else "🤖 Bot"
    st.markdown(f"<div class='{div_class}'>{label}: {m['content']}</div>", unsafe_allow_html=True)

# Input Row
col1, col2 = st.columns([5, 1])
with col1:
    u_input = st.chat_input("Ask about Cell, Force, Gandhi, Maths...")
with col2:
    if st.button("🎤 Mike"):
        st.toast("Listening...")

# Process
if u_input:
    st.session_state.chat.append({"role": "user", "content": u_input})
    bot_reply = get_answer(u_input)
    st.session_state.chat.append({"role": "assistant", "content": bot_reply})
    
    # Voice
    try:
        tts = gTTS(text=bot_reply[:150], lang='hi')
        af = io.BytesIO()
        tts.write_to_fp(af)
        st.audio(af, format='audio/mp3')
    except: pass
    st.rerun()
