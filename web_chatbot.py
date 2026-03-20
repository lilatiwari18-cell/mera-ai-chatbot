import streamlit as st
import random
import time

# 1. Page Config & Advanced CSS for Space Theme
st.set_page_config(page_title="YashProBot.ai - Deep Space", page_icon="🚀", layout="wide")

# Advanced CSS: Background, Animations, and Text Colors
st.markdown("""
    <style>
    /* Real Space Background with Nebula and Stars */
    .stApp {
        background-color: #000b18;
        background-image: url('https://img.freepik.com/free-photo/view-planet-from-outer-space_23-2150821558.jpg'); /* Real Space View */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* 1. Gradient (Color Changing) Text for Titles and Content */
    .stHeader, h1, h2, h3, .stMarkdown, div[data-testid="stSidebar"] p {
        background: linear-gradient(45deg, #00d2ff, #9b59b6, #e0f7fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }

    /* 2. Floating Space Robot Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-25px) rotate(4deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .stImage > img {
        animation: float 7s ease-in-out infinite;
        filter: drop-shadow(0 0 20px #00fff2); /* Neon Glow */
    }

    /* 3. Transparent Spaceship Module for Input */
    div.stTextInput > div > div > input {
        background-color: rgba(0, 40, 80, 0.5) !important;
        color: #00fff2 !important;
        border: 2px solid #00fff2 !important;
        border-radius: 20px !important;
        padding: 18px !important;
        font-size: 19px !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 20px rgba(0, 255, 242, 0.4);
    }
    div.stTextInput > div > div > input::placeholder {
        color: #008cba;
    }

    /* 4. Glowing Rocket Launch Button */
    .stButton>button {
        background: linear-gradient(135deg, #00fff2 0%, #3a7bd5 100%);
        color: white;
        border: 2px solid #00fff2;
        border-radius: 30px;
        font-weight: bold;
        transition: 0.4s;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.6);
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.9);
    }
    
    /* 5. Space Sidebar Profile */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 10, 24, 0.6);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(0, 210, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Login System - Galaxy Portal
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🌟 Enter YashProBot.ai - Galaxy Portal")
    st.write("✨ **Welcome Captain Kanchney! Activate AI Starship.** ✨")
    col1, col2 = st.columns([1,1])
    with col1:
        u = st.text_input("Galaxy ID (Type 'admin')", key="id")
    with col2:
        p = st.text_input("Secret Hyper-Key (Type '12345')", type="password", key="key")
        
    if st.button("🚀 Activate Starship AI", key="activate"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Access Denied! Wrong Key.")
    st.stop()

# 3. Space Sidebar with Kanchney's Profile
with st.sidebar:
    st.markdown(f"## 🛸 Kanchney Tiwari")
    st.write("Galaxy Class 9th 'B'")
    st.write("PM Shri KV, Salempur")
    st.markdown("---")
    st.write("**Mission Control:** Mr. Awadhesh & Mrs. Lila Tiwari")
    mode = st.radio("System Mode:", ["💬 AI SuperChat", "🎮 Logic Quiz"])

# 4. Main Starship Interface
st.title("🤖 YashProBot.ai - Zero Gravity Mode")

col1, col2 = st.columns([1, 2])

with col1:
    # 5. Advanced DiceBear Space Robot (with background choices)
    # Using 'bottts' style for robotic space look
    robot_url = f"https://api.dicebear.com/7.x/bottts/svg?seed=KanchneySpace&backgroundColor=00fff2,2a5298"
    st.image(robot_url, width=320)
    st.markdown("#### Status: <span style='color:#00ff00'>● Fully Functional (Flying)</span>", unsafe_allow_html=True)

with col2:
    st.write("### Kanchney, main deep space analysis ke liye taiyar hoon.")
    
    # 6. Stylish Spaceship Input Module
    user_msg = st.text_input("🚀 Transmit your command to AI...", placeholder="Example: Galaxy Explorer Protocol...", key="msg_input")
    
    if st.button("Transmit to Hyper-Processor", key="send"):
        if user_msg:
            with st.spinner("Processing in hyperspace..."):
                time.sleep(1.2)
                st.snow()
                st.chat_message("assistant").write(f"Kanchney, main aapke '{user_msg}' command par space research kar raha hoon.")
