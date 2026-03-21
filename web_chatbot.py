import streamlit as st
import google.generativeai as genai
import random
import time
from gtts import gTTS
import io

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai", page_icon="🤖", layout="wide")

# API Key Setup
# Yaad se requirements.txt mein google-generativeai likh dena!
genai.configure(api_key="AIzaSyBVXk7hPDoPIswSBE9ILskN7aIcND-k904")
model = genai.GenerativeModel('gemini-pro')

# Background History
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d"

# 2. CSS (Clean & Professional)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .chat-bubble {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #ff9933;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Yash Tiwari Profile)
with st.sidebar:
    st.header("👑 Developer Profile")
    st.success("**Name:** Yash Tiwari")
    st.write("**Father:** Mr. Awadhesh Tiwari")
    st.write("**Mother:** Mrs. Lila Tiwari")
    st.write("**Class:** 9th 'B' | KV Salempur")
    st.markdown("---")
    lang = st.selectbox("🌐 Robot Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🌲 Change Tree Look"):
        st.session_state.current_bg = f"https://picsum.photos/1920/1080?nature,tree&sig={random.randint(1,100)}"
        st.rerun()

# 4. Main Interface
st.title("🤖 YashProBot.ai")

for msg in st.session_state.messages:
    st.markdown(f"<div class='chat-bubble'><b>{msg['role']}:</b> {msg['content']}</div>", unsafe_allow_html=True)

# Input Row
st.markdown("---")
col_input, col_btn = st.columns([5, 1])

with col_input:
    user_q = st.text_input("", placeholder="Sawal puchiye, Yash Tiwari...", label_visibility="collapsed", key="user_msg")

with col_btn:
    submit = st.button("🎙️ Send")

if submit and user_q:
    st.session_state.messages.append({"role": "Yash Tiwari", "content": user_q})
    
    # AI Brain (Gemini) Response
    try:
        response = model.generate_content(f"You are YashProBot created by Yash Tiwari. Answer this to Yash: {user_q}")
        bot_reply = response.text
    except:
        bot_reply = f"Jai Shree Ram Yash Tiwari! Main abhi API se connect nahi ho pa raha hoon, lekin aapka sawal '{user_q}' bahut accha hai."

    st.session_state.messages.append({"role": "YashProBot", "content": bot_reply})
    
    # Audio Output
    tts = gTTS(text=bot_reply[:200], lang='hi')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
    
    st.rerun()
