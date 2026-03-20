import streamlit as st
import random
import time

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai - Pro", page_icon="🚩", layout="wide")

# Session State for History & Background
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://wallpaperaccess.com/full/2042797.jpg"

# Background URLs
bg_urls = {
    'Space': "https://wallpaperaccess.com/full/1219590.jpg",
    'Minecraft': "https://wallpaperaccess.com/full/46631.jpg",
    'Goddess': "https://wallpaperaccess.com/full/2042797.jpg",
    'PUBG': "https://wallpaperaccess.com/full/1513943.jpg",
    'Nature': "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d"
}

def change_bg():
    st.session_state.current_bg = random.choice(list(bg_urls.values()))

# Double brackets {{ }} to avoid SyntaxError
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    h1, h2, h3, .stMarkdown, p {{
        color: #ffffff !important;
        font-weight: bold;
        text-shadow: 2px 2px 8px #000000;
    }}
    div.stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: #00fff2 !important;
        border: 2px solid #ff9933 !important;
        border-radius: 15px;
    }}
    /* Chat Bubble Style */
    .chat-bubble {{
        background-color: rgba(255, 255, 255, 0.15);
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        backdrop-filter: blur(5px);
        border-left: 5px solid #ff9933;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🚩 YashProBot - Jai Shree Ram")
    u = st.text_input("Galaxy ID")
    p = st.text_input("Hyper-Key", type="password")
    if st.button("Unlock Starship"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
    st.stop()

# 3. Sidebar (Language & Profile)
with st.sidebar:
    st.header("🚩 Jai Shree Ram")
    st.write(f"**Captain:** Kanchney Tiwari")
    st.markdown("---")
    lang = st.selectbox("🌐 Choose Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🖼️ Change Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Clear History"):
        st.session_state.messages = []
        st.rerun()

# 4. Main Chat Interface
st.title("🤖 YashProBot.ai")

col1, col2 = st.columns([1, 2])

with col1:
    # Flying Robot
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={random.randint(1,500)}", width=250)
    st.write("🛰️ **Status:** Active & Flying")

with col2:
    st.write(f"### Jai Shree Ram, Kanchney!")
    
    # Display Chat History
    for message in st.session_state.messages:
        with st.container():
            st.markdown(f"<div class='chat-bubble'><b>{message['role']}:</b> {message['content']}</div>", unsafe_allow_html=True)

    # Input Area
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Type here...", placeholder="Sawal puchiye...")
        submit_button = st.form_submit_button(label='Send Message')

    if submit_button and user_input:
        # Save User Message
        st.session_state.messages.append({"role": "Kanchney", "content": user_input})
        
        # Robot Logic based on Language
        responses = {
            "Hinglish": f"Jai Shree Ram Kanchney! Main aapke '{user_input}' par kaam kar raha hoon.",
            "Bhojpuri": f"Jai Shree Ram Kanchney! Raur sawal '{user_input}' bahut badhiya ba.",
            "Hindi": f"Jai Shree Ram Kanchney! Aapka prashna '{user_input}' vishleshan ke liye bhej diya gaya hai.",
            "English": f"Jai Shree Ram Kanchney! Processing your query: '{user_input}'."
        }
        
        # Save Robot Response
        st.session_state.messages.append({"role": "YashProBot", "content": responses[lang]})
        change_bg() # Background changes on each message
        st.rerun()
