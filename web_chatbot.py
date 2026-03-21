import streamlit as st
import random
from gtts import gTTS
import io

# 1. PAGE CONFIG
st.set_page_config(page_title="YashProBot.ai", page_icon="🤖", layout="wide")

# 2. TOP BANNER: WELCOME FRIEND
st.markdown(f"""
    <div style="background: rgba(41, 128, 185, 0.3); padding: 25px; border-radius: 20px; border: 2px solid #3498db; text-align: center; margin-bottom: 30px;">
        <h1 style="color: white; text-shadow: 2px 2px 10px #3498db;">👋 Welcome Friend! 👋</h1>
        <p style="color: #ecf0f1; font-size: 1.3em;">Created by: <b>Yash Tiwari</b> (Class 9-B)</p>
    </div>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (DEVELOPER PROFILE & MUSIC)
with st.sidebar:
    st.markdown("### 👑 Developer Profile")
    st.success("**Yash Tiwari**")
    st.info("School: PM Shri KV Chero, Salempur")
    
    st.markdown("---")
    st.markdown("### 🎵 Music (Amplifier x Safari)")
    # Music Player
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.caption("Press Play to start the music!")

    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# 4. SMART BRAIN (Offline Mode)
def smart_brain(q):
    q = q.lower()
    if "name" in q:
        return "Mera naam YashProBot.ai hai aur mujhe Yash Tiwari ne banaya hai!"
    elif "hello" in q or "hi" in q:
        return "Jai Shree Ram Friend! Main Yash Tiwari ka personal AI hoon. Main aapki kya madad kar sakta hoon?"
    elif "maths" in q or "heron" in q:
        return "Maths Mode: Area = sqrt(s(s-a)(s-b)(s-c)). Yash ne mujhe ye sikhaya hai!"
    else:
        return f"Dost, '{q}' ka jawab mere paas jaldi aayega. Tab tak Yash Tiwari se baat karein!"

# 5. CHAT INTERFACE
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Displaying chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
user_input = st.chat_input("Yash ke bot se kuch puchiye...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Bot Response
    reply = smart_brain(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
    
    # Text-to-Speech (Hindi)
    tts = gTTS(text=reply[:100], lang='hi')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
