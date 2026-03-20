import streamlit as st
import random
import time
from gtts import gTTS
import io

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai - Tree Edition", page_icon="🌳", layout="wide")

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

# 2. Stylish CSS with Colorful Buttons
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Neon Text Style */
    h1, h2, h3, p, b, .stMarkdown {{
        color: white !important;
        text-shadow: 2px 2px 10px black;
    }}

    /* Input Box Glassmorphism */
    div.stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: #2ecc71 !important;
        border: 2px solid #2ecc71 !important;
        border-radius: 15px !important;
        font-size: 18px;
    }}

    /* COLORFUL BUTTONS */
    .stButton>button {{
        background: linear-gradient(45deg, #ff9933, #ff5e62) !important; /* Orange Gradient */
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 153, 51, 0.4);
        transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 153, 51, 0.7);
        border: 2px solid white !important;
    }}

    /* Chat Bubbles */
    .chat-bubble {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
        border-left: 5px solid #2ecc71;
    }}
    
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 30, 0, 0.8) !important;
        backdrop-filter: blur(10px);
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Your Details)
with st.sidebar:
    st.header("👑 Developer Profile")
    st.write(f"**Name:** Kanchney Tiwari (Yash)")
    st.write(f"**Father's Name:** Mr. Awadhesh Tiwari")
    st.write(f"**Mother's Name:** Mrs. Lila Tiwari")
    st.write(f"**Class:** 9th 'B' | KV Salempur")
    st.markdown("---")
    lang = st.selectbox("🌐 Robot Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🌲 Change Tree Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Reset All"):
        st.session_state.messages = []
        st.rerun()

# 4. Main Chat Interface
st.title("🤖 YashProBot.ai - Tree Pro")

# Show Chat History
for msg in st.session_state.messages:
    st.markdown(f"<div class='chat-bubble'><b>{msg['role']}:</b> {msg['content']}</div>", unsafe_allow_html=True)

st.markdown("---")

# 5. Pro Layout: Mike and Text box side-by-side
col_input, col_btn = st.columns([5, 1])

with col_input:
    user_input = st.text_input("", placeholder="Yahan likhein...", label_visibility="collapsed", key="msg_box")

with col_btn:
    # Colored Button for Send/Mike
    submit = st.button("🎙️ Send")

if submit and user_input:
    st.session_state.messages.append({"role": "Kanchney", "content": user_input})
    
    # Robot Logic based on Language
    replies = {
        "Hinglish": f"Jai Shree Ram Kanchney! Main aapka robot '{user_input}' ka jawab de raha hoon.",
        "Bhojpuri": f"Jai Shree Ram Kanchney! Raur prashna '{user_input}' bahut badhiya ba.",
        "Hindi": f"Jai Shree Ram Kanchney! Aapka sawal vishleshan ke liye bhej diya gaya hai.",
        "English": f"Jai Shree Ram Kanchney! Processing: '{user_input}'."
    }
    
    bot_reply = replies[lang]
    st.session_state.messages.append({"role": "YashProBot", "content": bot_reply})
    
    # Voice Output
    tts = gTTS(text=bot_reply, lang='hi' if lang != "English" else 'en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
    
    change_bg() # Automatically pick one of the 20 tree photos
    st.rerun()
