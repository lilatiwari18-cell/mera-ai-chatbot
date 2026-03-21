import streamlit as st
import google.generativeai as genai
from PIL import Image
import random
import time
from gtts import gTTS
import io

# ==========================================
# 1. PAGE CONFIG & DESIGN (NEON NATURE)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Master", page_icon="🌳", layout="wide")

# 20 High-Quality Tree Photos
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

if 'current_bg' not in st.session_state:
    st.session_state.current_bg = tree_photos[0]
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def change_bg():
    st.session_state.current_bg = random.choice(tree_photos)

# CSS for Glassmorphism and Glowing Buttons
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 25px;
        border: 2px solid #2ecc71;
    }}
    .stButton>button {{
        background: linear-gradient(45deg, #ff9933, #ff5e62) !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 153, 51, 0.3);
    }}
    h1, h2, h3, p, b, .stMarkdown {{
        color: white !important;
        text-shadow: 2px 2px 5px black;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. AI BRAIN SETUP (Gemini)
# ==========================================
# Yahan apni API Key daalein (Ya Streamlit Secrets use karein)
API_KEY = "AIzaSyBVXk7hPDoPIswSBE9ILskN7aIcND-k904" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Bhai, API Key check karo! Ya fir internet slow hai."

# ==========================================
# 3. SIDEBAR (DEVELOPER PROFILE)
# ==========================================
with st.sidebar:
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed={random.randint(1,99)}&backgroundColor=2ecc71", width=150)
    st.header("👑 Developer Profile")
    st.info(f"""
    **Name:** Yash (Kanchan) Tiwari  
    **Father:** Mr. Awadhesh Tiwari  
    **Mother:** Mrs. Lila Tiwari  
    **Class:** 9th 'B'  
    **School:** PM Shri KV Chero, Salempur
    """)
    st.markdown("---")
    lang = st.selectbox("🌐 Robot Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    if st.button("🌲 Change Tree Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Reset Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# ==========================================
# 4. CHAT INTERFACE
# ==========================================
st.title("🤖 YashProBot.ai - The Master Bot")
st.write("### Jai Shree Ram, Kanchney! Main taiyar hoon Class 1-12 ke sawalon ke liye.")

# Display History
for chat in st.session_state.chat_history:
    role_icon = "👤" if chat['role'] == "user" else "🤖"
    with st.chat_message(chat['role'], avatar=role_icon):
        st.markdown(chat['content'])

# Input Row
st.markdown("---")
c1, c2 = st.columns([6, 1])

with c1:
    user_input = st.text_input("", placeholder="Maths, Science ya Coding ka sawal puchiye...", label_visibility="collapsed")
with c2:
    send_btn = st.button("🎙️ Send")

if send_btn and user_input:
    # 1. Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # 2. Get AI Brain Response
    with st.spinner("YashProBot soch raha hai..."):
        full_prompt = f"Imagine you are YashProBot, an AI made by Yash Tiwari from Class 9B. Answer this in {lang}: {user_input}"
        answer = get_ai_response(full_prompt)
    
    # 3. Add bot response
    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    
    # 4. Generate Voice
    tts = gTTS(text=answer[:200], lang='hi' if lang != "English" else 'en') # Limit to 200 chars for speed
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
    
    # 5. Refresh
    change_bg()
    st.rerun()

# ==========================================
# 5. EXTRA FEATURES (MATHS EXPERT)
# ==========================================
if st.checkbox("Show Quick Formulas (Class 9)"):
    st.write("📐 **Heron's Formula:** Area = $\sqrt{s(s-a)(s-b)(s-c)}$")
    st.write("🐍 **Pygame Init:** `pygame.init()`")
