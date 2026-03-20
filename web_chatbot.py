import streamlit as st
import random
import time
from gtts import gTTS
import io

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai - Jai Shree Ram", page_icon="🚩", layout="wide")

# Session State for History & Background
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://wallpaperaccess.com/full/2042797.jpg"

# God and Natural Backgrounds only
bg_urls = {
    'Maa Durga': "https://wallpaperaccess.com/full/2042797.jpg",
    'Mahadev': "https://wallpaperaccess.com/full/1123013.jpg",
    'Ram Darbar': "https://wallpaperaccess.com/full/4890635.jpg",
    'Forest Waterfall': "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d",
    'Mountain Sunrise': "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    'Deep Jungle': "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"
}

def change_bg():
    st.session_state.current_bg = random.choice(list(bg_urls.values()))

# UI Styling with Glassmorphism
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* Text Glow Effect */
    h1, h2, h3, .stMarkdown, p, b {{
        color: white !important;
        text-shadow: 2px 2px 10px #000000, 0 0 5px #ff9933;
    }}
    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 0, 0, 0.7) !important;
        backdrop-filter: blur(10px);
        border-right: 2px solid #ff9933;
    }}
    /* Chat Bubbles */
    .chat-bubble {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #ff9933;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🚩 Jai Shree Ram - YashProBot")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Access Starship"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
    st.stop()

# 3. Sidebar with All Personal Details
with st.sidebar:
    st.header("👑 Developer Profile")
    st.write(f"**Name:** Kanchney Tiwari (Yash)")
    st.write(f"**Father's Name:** Mr. Awadhesh Tiwari")
    st.write(f"**Mother's Name:** Mrs. Lila Tiwari")
    st.write(f"**Class:** 9th 'B'")
    st.write(f"**School:** PM Shri KV Chero, Salempur")
    st.markdown("---")
    lang = st.selectbox("🌐 Robot Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🖼️ Change Divine Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# 4. Main Chat Logic
st.title("🤖 YashProBot.ai - Voice Edition")

col1, col2 = st.columns([1, 2])

with col1:
    # Floating Space Robot
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={random.randint(1,1000)}&backgroundColor=ff9933", width=250)
    st.write("🛰️ **Status:** Divine Mode Active")

with col2:
    st.write(f"### Jai Shree Ram, Kanchney!")
    
    # Display Saved History
    for msg in st.session_state.messages:
        st.markdown(f"<div class='chat-bubble'><b>{msg['role']}:</b> {msg['content']}</div>", unsafe_allow_html=True)

    # Input Form
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("🎙️ Mike On: Sawal puchiye...", placeholder="Ask anything...")
        submit = st.form_submit_button("Send & Speak 🎙️")

    if submit and user_input:
        st.session_state.messages.append({"role": "Kanchney", "content": user_input})
        
        # Robot Voice Response Logic
        replies = {
            "Hinglish": f"Jai Shree Ram Kanchney! Main aapka robot aapke sawal '{user_input}' ka jawab taiyar kar raha hoon.",
            "Bhojpuri": f"Jai Shree Ram Kanchney! Raur prashna '{user_input}' bahut neek ba, rukiye batawat tani.",
            "Hindi": f"Jai Shree Ram Kanchney! Aapka sawal vishleshan ke liye bhej diya gaya hai.",
            "English": f"Jai Shree Ram Kanchney! I am processing your request regarding '{user_input}'."
        }
        
        bot_reply = replies[lang]
        st.session_state.messages.append({"role": "YashProBot", "content": bot_reply})
        
        # Generate Audio (The Mike Feature)
        tts = gTTS(text=bot_reply, lang='hi' if lang != "English" else 'en')
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        st.audio(audio_fp, format='audio/mp3')
        
        change_bg() # Automatically change to next God/Nature photo
        st.rerun()
