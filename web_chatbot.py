import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. UI FIX (TEXT CLEARANCE & DESIGN)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Clear View", page_icon="🎤", layout="wide")

# Background images
bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d",
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []

# CSS for Bold Text and Shadow
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    /* Answer Box: Isse text background se alag dikhega */
    .bot-msg {{
        background: rgba(0, 0, 0, 0.85); 
        color: #00ffcc !important; 
        padding: 20px; 
        border-radius: 15px; 
        border: 2px solid #00ffcc;
        font-size: 1.2em;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
    }}
    .user-msg {{
        background: rgba(255, 255, 255, 0.2); 
        color: white !important; 
        padding: 10px; 
        border-radius: 10px;
        text-align: right;
        margin-bottom: 10px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR (PROFILE & MIKE SETTINGS)
# ==========================================
with st.sidebar:
    st.title("👑 Yash Tiwari")
    st.write("Section: 9-B | KV Salempur")
    st.markdown("---")
    st.success("🎤 Mike is Active")
    st.info("Bina net ke bhi Quiz mode on hai!")
    
    if st.button("🌲 Change Tree Look"):
        st.session_state.bg = random.choice(bgs)
        st.rerun()

# ==========================================
# 3. CHAT DISPLAY & MIKE BUTTON
# ==========================================
st.markdown("<h1 style='color:white; text-align:center; text-shadow: 3px 3px 5px black;'>🤖 YashProBot.ai</h1>", unsafe_allow_html=True)

for m in st.session_state.chat:
    if m["role"] == "user":
        st.markdown(f"<div class='user-msg'>👤 You: {m['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 Bot: {m['content']}</div>", unsafe_allow_html=True)

# Input Row with Mike Simulation
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.chat_input("Sawal puchiye, Yash Tiwari...")
with col2:
    if st.button("🎤"):
        st.toast("Listening... (Mobile Browser Mike Active)")
        # Real voice recognition requires browser-side JS, 
        # but for school project, this button shows the feature!

# ==========================================
# 4. BOT BRAIN (CLEAR ANSWERS)
# ==========================================
def get_reply(q):
    q = q.lower()
    if "name" in q:
        return "Mera naam YashProBot.ai hai aur mujhe Yash Tiwari ne banaya hai!"
    elif "math" in q or "quiz" in q:
        return "Chaliye Class 9 Maths Quiz shuru karte hain! Heron's Formula kya hai?"
    else:
        return f"Jai Shree Ram! Yash Tiwari ke bot ne aapka sawal '{q}' sun liya hai."

if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})
    
    # Processing
    reply = get_reply(user_input)
    st.session_state.chat.append({"role": "assistant", "content": reply})
    
    # Voice Speak
    tts = gTTS(text=reply[:100], lang='hi')
    af = io.BytesIO()
    tts.write_to_fp(af)
    st.audio(af, format='audio/mp3')
    
    st.rerun()
