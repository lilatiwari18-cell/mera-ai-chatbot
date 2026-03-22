import streamlit as st
import random
import time
import base64

# --- 1. UI & STYLING (Cursive & Dark Mode) ---
st.set_page_config(page_title="YashProBot.ai", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    
    .stApp { background-color: #0e1117; color: white; }
    
    .cursive-font {
        font-family: 'Dancing Script', cursive;
        font-size: 24px !important;
        color: #00f2fe;
    }
    
    .caution-box {
        background-color: #ff4b4b22;
        border: 2px solid #ff4b4b;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA BANK (1st to 12th All Subjects) ---
knowledge_base = {
    "Primary (1-5)": [{"q": "How many legs does a spider have?", "a": "8", "lvl": "Medium"}],
    "Middle (6-8)": [{"q": "Process of plants making food?", "a": "Photosynthesis", "lvl": "Pro"}],
    "Class 9-10": [
        {"q": "Formula of Baking Soda?", "a": "NaHCO3", "lvl": "Thinking"},
        {"q": "Valency of Carbon?", "a": "4", "lvl": "Pro"}
    ],
    "Class 11-12": [
        {"q": "Derivative of sin(x)?", "a": "cos(x)", "lvl": "Pro"},
        {"q": "Who proposed the Bohr Model?", "a": "Niels Bohr", "lvl": "Thinking"}
    ]
}

# --- 3. SIDEBAR (Wallpaper Logic: 30 Trees / 20 Robots) ---
with st.sidebar:
    st.title("Settings")
    theme = st.radio("Choose Theme:", ["Nature/Trees", "3D Robots"])
    st.write("---")
    
    if theme == "Nature/Trees":
        # Logic for 30 random nature images
        img_id = random.randint(1, 30)
        st.image(f"https://picsum.photos/seed/nature{img_id}/400/300", caption=f"Natural Look #{img_id}")
    else:
        # Logic for 20 random robot images
        img_id = random.randint(1, 20)
        st.image(f"https://robohash.org/robot{img_id}?set=set1", caption=f"3D Robot #{img_id}")
    
    st.write("---")
    st.info("Created by: Yash Tiwari")

# --- 4. MAIN APP ---
st.markdown('<div class="caution-box">⚠️ CAUTION: YashProBot is Thinking | 100% Private & Safe</div>', unsafe_allow_html=True)
st.title("🤖 YashProBot.ai")

# Chat History Session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div class="cursive-font">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 5. INPUT & BOT LOGIC ---
col1, col2 = st.columns([0.85, 0.15])
with col2:
    if st.button("🎙️"):
        st.toast("Listening... (Speak now)")

with col1:
    user_input = st.chat_input("Dost, mujhse sawal pucho...")

if user_input:
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot Brain (Thinking Simulation)
    with st.chat_message("assistant"):
        with st.spinner("Analyzing data..."):
            time.sleep(1)
        
        # Rule: Always starts with "Chatbot give Answer:"
        prefix = "Chatbot give Answer: "
        
        if any(word in user_input.lower() for word in ["quiz", "question", "sawal"]):
            cat = random.choice(list(knowledge_base.keys()))
            item = random.choice(knowledge_base[cat])
            response = f"{prefix} [{cat}] Sawal: {item['q']} | Level: {item['lvl']}"
        else:
            response = f"{prefix} Hello mere dost! Main YashProBot hoon. Main 1st se 12th tak ki padhai mein help kar sakta hoon. Poochiye kya poochna hai?"

        st.markdown(f'<div class="cursive-font">{response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
