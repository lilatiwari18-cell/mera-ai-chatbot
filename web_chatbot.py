import streamlit as st
import random
import time

# 1. Page Config & CSS for Dynamic Backgrounds and Neon Look
st.set_page_config(page_title="YashProBot.ai - Dynamic", page_icon="🤖", layout="wide")

# Setting up Session State for Background to persist on reruns
if 'current_bg' not in st.session_state:
    st.session_state.current_bg = "https://img.freepik.com/free-photo/view-planet-from-outer-space_23-2150821558.jpg" # Default Space

# All Your Requested Background Categories (HD Links)
bg_urls = {
    'Tree': "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d",
    'Animal': "https://images.unsplash.com/photo-1546182990-dffeafbe841d", # Lion
    'Minecraft': "https://user-images.githubusercontent.com/62492160/123547225-c61e8980-d737-11eb-8c68-0d196f4e1d3d.jpg",
    'PUBG': "https://img.freepik.com/premium-photo/pubg-game-wallpaper-4k_758410-141.jpg",
    'FreeFire': "https://images2.alphacoders.com/112/1125219.jpg",
    'Valorant': "https://user-images.githubusercontent.com/62492160/118360113-d3acb780-b586-11eb-8285-801244e83c07.png",
    'God of War': "https://images7.alphacoders.com/906/906232.jpg",
    'Goddess': "https://img.freepik.com/premium-photo/portrait-maa-durga-wallpaper-digital-art_758410-18.jpg" # Maa Durga
}

# Function to Change Background randomly
def change_background():
    category = random.choice(list(bg_urls.keys()))
    st.session_state.current_bg = bg_urls[category]
    st.toast(f"Background Changed to: {category}!", icon="🖼️")

# Injection of Dynamic CSS
st.markdown(f"""
    <style>
    /* Dynamic Background */
    .stApp {{
        background-color: #000b18;
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Neon Text Gradient for titles and sidebar */
    h1, h2, h3, .stMarkdown, .stSelectbox label, [data-testid="stSidebar"] div p {{
        background: linear-gradient(45deg, #00d2ff, #9b59b6, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }}

    /* Floating Robot Animation */
    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-20px) rotate(3deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    .stImage > img {{
        animation: float 6s ease-in-out infinite;
        filter: drop-shadow(0 0 15px #00fff2);
    }}

    /* Transparent Spaceship Module for Input */
    div.stTextInput > div > div > input {{
        background-color: rgba(0, 40, 80, 0.6) !important;
        color: #00fff2 !important;
        border: 2px solid #00fff2 !important;
        border-radius: 20px !important;
        padding: 18px !important;
        font-size: 19px !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 20px rgba(0, 255, 242, 0.4);
    }
    
    /* Glowing Button */
    .stButton>button {{
        background: linear-gradient(135deg, #00fff2 0%, #3a7bd5 100%);
        color: white;
        border: 2px solid #00fff2;
        border-radius: 30px;
        font-weight: bold;
        transition: 0.4s;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.6);
    }
    .stButton>button:hover {{
        transform: scale(1.1);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.9);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🛡️ Secure Portal: YashProBot.ai")
    u = st.text_input("Galaxy ID")
    p = st.text_input("Hyper-Key", type="password")
    if st.button("Unlock AI"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            change_background() # Initial background change
            st.rerun()
    st.stop()

# 3. Sidebar with Kanchney's Profile
with st.sidebar:
    st.markdown(f"## 🛸 Kanchney Tiwari")
    st.write("Galaxy Class 9th 'B'")
    st.write("PM Shri KV, Salempur")
    st.markdown("---")
    # Button to change background manually
    if st.button("🖼️ Change Background"):
        change_background()
        st.rerun()
    st.markdown("---")
    mode = st.radio("System Mode:", ["💬 SuperChat", "🎮 Quiz"])

# 4. Main Interface
st.title("🤖 YashProBot.ai - Dynamic Mode")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=KanchneyDynamic", width=280)
    st.write("🛰️ **Status:** Flying & Changing Looks")

with col2:
    st.write("### Kanchney, puchiye kya sawal hai?")
    user_msg = st.text_input("Transmit your command...")
    
    if st.button("Send Message"):
        if user_msg:
            # Automatic background change on sending a message
            change_background()
            with st.spinner("AI is processing..."):
                time.sleep(1.2)
                st.chat_message("assistant").write(f"Kanchney, aapne '{user_msg}' pucha. Main research kar raha hoon.")
