import streamlit as st
import random
import time
from gtts import gTTS
import io

# 1. Page Config (Mobile Friendly)
st.set_page_config(page_title="YashProBot.ai - Free Access", page_icon="🌳", layout="wide")

# Session State for History & Background
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d"

# 20 High-Quality Tree & Nature Photos
tree_photos = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
    "https://images.unsplash.com/photo-1507502707541-f369a3b18502", "https://images.unsplash.com/photo-1473448912268-2022ce9509d8",
    "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86", "https://images.unsplash.com/photo-1448375033490-4c1b413ed748",
    "https://images.unsplash.com/photo-1425913397330-cf8af2ff40a1", "https://images.unsplash.com/photo-1502082553048-f009c37129b9",
    "https://images.unsplash.com/photo-1476231682828-37e571bc172f", "https://images.unsplash.com/photo-1444492412393-5510b18122f2",
    "https://images.unsplash.com/photo-1496715976403-7e36dc43f17b", "https://images.unsplash.com/photo-1501854140801-50d01674aa3e",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e", "https://images.unsplash.com/photo-1511497584788-876760111969",
    "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d", "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
    "https://images.unsplash.com/photo-1472214103451-9374bd1c798e", "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc",
    "https://images.unsplash.com/photo-1421789665209-c9b2a435e3dc", "https://images.unsplash.com/photo-1433086966358-54859d0ed716"
]

def change_bg():
    st.session_state.current_bg = random.choice(tree_photos)

# 2. Advanced CSS (No Password Required)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    h1, h2, h3, p, b, .stMarkdown {{
        color: white !important;
        text-shadow: 2px 2px 10px black;
    }}

    /* Chat Bubbles for History */
    .chat-bubble {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #2ecc71;
    }}

    /* Colorful Buttons */
    .stButton>button {{
        background: linear-gradient(45deg, #ff9933, #ff5e62) !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold;
        border: none;
    }}

    /* Sidebar Background */
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 30, 0, 0.85) !important;
        backdrop-filter: blur(10px);
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Profile & Language)
with st.sidebar:
    st.header("👑 Developer Profile")
    st.write(f"**Name:** Yash (Kanchan) Tiwari")
    st.write(f"**Father:** Mr. Awadhesh Tiwari")
    st.write(f"**Mother:** Mrs. Lila Tiwari")
    st.write(f"**Class:** 9th 'B' | KV Salempur")
    st.markdown("---")
    lang = st.selectbox("🌐 Language Changer", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🌲 Change Tree Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# 4. Main Chat Logic
st.title("🤖 YashProBot.ai")

# Display History
for msg in st.session_state.messages:
    st.markdown(f"<div class='chat-bubble'><b>{msg['role']}:</b> {msg['content']}</div>", unsafe_allow_html=True)

st.markdown("---")

# 5. Pro Layout: Mike and Text box Side-by-Side
col_in, col_btn = st.columns([5, 1])

with col_in:
    user_q = st.text_input("", placeholder="Class 1-12 ka koi bhi sawal puchiye...", label_visibility="collapsed", key="chat_input")

with col_btn:
    send_click = st.button("🎙️ Send")

if send_click and user_q:
    st.session_state.messages.append({"role": "Kanchney", "content": user_q})
    
    # Robot Logic
    replies = {
        "Hinglish": f"Jai Shree Ram Kanchney! Main aapke sawal '{user_q}' par research kar raha hoon.",
        "Bhojpuri": f"Jai Shree Ram Kanchney! Raur sawal '{user_q}' bahut badhiya ba, rukiye batavat tani.",
        "Hindi": f"Jai Shree Ram Kanchney! Aapka prashna '{user_q}' vishleshan ke liye bhej diya gaya hai.",
        "English": f"Jai Shree Ram Kanchney! Processing your query: '{user_q}'."
    }
    
    bot_reply = replies[lang]
    st.session_state.messages.append({"role": "YashProBot", "content": bot_reply})
    
    # Voice Output
    tts = gTTS(text=bot_reply, lang='hi' if lang != "English" else 'en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
    
    change_bg() # Automatically change tree photo
    st.rerun()
