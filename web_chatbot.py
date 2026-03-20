import streamlit as st
import random
import time
from gtts import gTTS
import io

# 1. Page & Space CSS
st.set_page_config(page_title="YashProBot.ai - Voice", page_icon="🎙️", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #001f3f 0%, #000b18 100%);
        background-image: url('https://user-images.githubusercontent.com/62492160/114111306-039c3600-98e3-11eb-84da-50117094b85c.jpg');
        background-size: cover;
        color: #e0f7fa;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .stImage > img { animation: float 5s ease-in-out infinite; filter: drop-shadow(0 0 15px #00d2ff); }
    
    div.stTextInput > div > div > input {
        background-color: rgba(0, 40, 80, 0.5) !important;
        color: #00ffea !important;
        border: 2px solid #00d2ff !important;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Function: Robot Voice Generator
def robot_speak(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    return fp

# 2. Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🚀 Space Portal: YashProBot.ai")
    u = st.text_input("Galaxy ID")
    p = st.text_input("Hyper-Key", type="password")
    if st.button("Launch"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
    st.stop()

# 3. Main Interface
st.title("🤖 YashProBot Voice Edition")

col1, col2 = st.columns([1, 2])

with col1:
    seed = random.randint(1, 9999)
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={seed}", width=280)
    st.write("🛰️ **Status:** Flying in Space")

with col2:
    st.write(f"### Namaste Kanchney! Main bol sakta hoon.")
    user_query = st.text_input("🎙️ Mike On: Kuch puchiye...", placeholder="Jaise: Kaise ho robot?")
    
    if st.button("Send & Speak"):
        if user_query:
            # Robot ka jawab (Hinglish/Bhojpuri mix)
            reply_text = f"Kanchney, aapne pucha {user_query}. Main ek smart space robot hoon aur aapki madad ke liye taiyar hoon!"
            
            st.chat_message("assistant").write(reply_text)
            
            # Voice Generate karein
            with st.spinner("Robot apni awaaz taiyar kar raha hai..."):
                audio_data = robot_speak(reply_text)
                st.audio(audio_data, format='audio/mp3')
                st.success("🔊 Upar 'Play' button dabayein aur meri awaaz sunein!")
