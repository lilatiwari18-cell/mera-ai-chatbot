import streamlit as st
import random
import time

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai - Dynamic", page_icon="🤖", layout="wide")

# Session State for Background
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d" # Default Tree

# All Background Categories
bg_urls = {
    'Tree': "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d",
    'Animal': "https://images.unsplash.com/photo-1546182990-dffeafbe841d",
    'Minecraft': "https://wallpaperaccess.com/full/46631.jpg",
    'PUBG': "https://wallpaperaccess.com/full/1513943.jpg",
    'FreeFire': "https://wallpaperaccess.com/full/1242319.jpg",
    'Valorant': "https://wallpaperaccess.com/full/2573229.jpg",
    'God of War': "https://wallpaperaccess.com/full/171542.jpg",
    'Goddess': "https://wallpaperaccess.com/full/2042797.jpg"
}

def change_background():
    category = random.choice(list(bg_urls.keys()))
    st.session_state.current_bg = bg_urls[category]

# FIXED CSS (Double brackets used to avoid f-string error)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}
    
    /* Neon Text Style */
    h1, h2, h3, .stMarkdown, [data-testid="stSidebar"] p {{
        background: linear-gradient(45deg, #00d2ff, #9b59b6, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}

    /* Flying Robot Animation */
    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-20px) rotate(3deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    .stImage > img {{
        animation: float 6s ease-in-out infinite;
        filter: drop-shadow(0 0 15px #00fff2);
    }}

    /* Message Module */
    div.stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: #00fff2 !important;
        border: 2px solid #00fff2 !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
    }}
    
    .stButton>button {{
        background: linear-gradient(135deg, #00fff2 0%, #3a7bd5 100%);
        color: white;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🛡️ YashProBot Entry")
    u = st.text_input("Galaxy ID")
    p = st.text_input("Hyper-Key", type="password")
    if st.button("Unlock"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
    st.stop()

# 3. Sidebar
with st.sidebar:
    st.markdown(f"## 🛸 Kanchney Tiwari")
    st.write("Class 9th 'B' | KV Salempur")
    if st.button("🖼️ Change Look"):
        change_background()
        st.rerun()
    st.markdown("---")
    mode = st.radio("Mode:", ["Chat", "Quiz"])

# 4. Main Chat
st.title("🤖 YashProBot.ai - Space Pro")

col1, col2 = st.columns([1, 2])

with col1:
    seed = random.randint(1, 1000)
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={seed}", width=250)
    st.write("🛰️ **Status:** Flying")

with col2:
    st.write(f"### Namaste Kanchney!")
    msg = st.text_input("Command bhejiye...", key="input")
    
    if st.button("Send Message"):
        if msg:
            change_background() # Background changes on send
            with st.spinner("AI thinking..."):
                time.sleep(1)
                st.chat_message("assistant").write(f"Captain Kanchney, main '{msg}' analyze kar raha hoon.")
