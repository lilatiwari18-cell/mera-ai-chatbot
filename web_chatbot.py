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
st.set_page_config(page_title="YashProBot.ai - Ultra", page_icon="🌳", layout="wide")

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

# CSS for Glassmorphism, Glowing Buttons, & Profile Glowing
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .dev-card {{
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #2ecc71;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 0 15px #2ecc71;
        text-align: center;
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
# Yahan अपनी Free API Key डालना, वरना image generation fail होगा.
API_KEY = "AIzaSyB2HzWiPt9BJ4_FgLB2nzJM6LtwzDCO-i0" 
genai.configure(api_key=API_KEY)
# We need two models: one for chat, one for image gen (e.g., Gemini 1.5 Pro can do both)
try:
    model_chat = genai.GenerativeModel('gemini-pro')
except:
    st.error("API Key missing! Google Gemini key, otherwise chatbot is basic.")
    model_chat = None

def get_ai_response(prompt):
    if not model_chat: return "Basic brain: Need API Key for thinking!"
    try:
        response = model_chat.generate_content(prompt)
        return response.text
    except:
        return "Thinking mode failed! API Key limit maybe."

# --- IDEA: DUMMY IMAGE GEN (REPLACE WITH REAL GEN) ---
def create_image_dummy(prompt):
    # This function should call a model capable of generating images. 
    # For now, we simulate image creation with nature photos.
    # In real deploy, we would use something like Stable Diffusion API or an advanced model.
    # To demonstrate `Pillow` use, we are manipulating a nature image.
    try:
        base_img = Image.open(requests.get(random.choice(tree_photos), stream=True).raw)
        # We manipulate the image using `Pillow` (dummy manipulation)
        base_img = base_img.convert('L').point(lambda x: 0 if x < 128 else 255, '1') # Black & White
        return base_img
    except:
        return None

# ==========================================
# 3. SIDEBAR (DEVELOPER PROFILE)
# ==========================================
with st.sidebar:
    st.markdown("<div class='dev-card'>", unsafe_allow_html=True)
    st.image(f"https://api.dicebear.com/7.x/bottts/svg?seed=Yash&backgroundColor=2ecc71", width=120)
    st.header("👑 Yash Tiwari")
    st.info("""
    **Father:** Mr. Awadhesh Tiwari  
    **Mother:** Mrs. Lila Tiwari  
    **Class:** 9th 'B' | KV Salempur
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # NEW FEATURE 1: SUBJECT MODE & THINKING LEVEL
    mode = st.selectbox("📚 Study Modes", ["General Chat", "Maths Expert", "Python Coder", "Science Lab"])
    think_level = st.selectbox("🧠 Thinking Levels", ["Pro Level 🔥 (Detailed)", "Thinking 🤔 (Step-by-Step)", "Medium ⚙️ (Quick)"])
    
    lang = st.radio("🗣️ Language", ["Hinglish", "Hindi", "Bhojpuri", "English"])
    
    # NEW FEATURE 2: SAFARI MUSIC SWITCH
    music_on = st.checkbox("🎵 Music (Amplifier x Safari)", value=True)
    
    if st.button("🌲 New Tree Look"):
        change_bg()
        st.rerun()
    if st.button("🗑️ Reset Chat"):
        st.session_state.chat_history = []
        st.rerun()

# --- Music HTML ---
if music_on:
    # Amplifier/Safari dummy tune player. Use a real embed link if available.
    music_html = """
        <audio id="bg-music" autoplay loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("bg-music");
            audio.volume = 0.2; 
        </script>
    """
    st.components.v1.html(music_html, height=0)

# ==========================================
# 4. CHAT INTERFACE & MASTER LOGIC
# ==========================================
st.title("🤖 YashProBot.ai - Ultra Mode 🚀")
st.write(f"### Jai Shree Ram, Yash Tiwari! Main taiyar hoon level: {think_level}")

# Display History (Chat bubbles)
for chat in st.session_state.chat_history:
    role_icon = "👤" if chat['role'] == "user" else "🤖"
    with st.chat_message(chat['role'], avatar=role_icon):
        st.markdown(chat['content'])
        # Display image if present
        if 'generated_image' in chat:
            st.image(chat['generated_image'], caption="AI Generated Image", width=300)

# Input Row
st.markdown("---")
c1, c2 = st.columns([6, 1])
with c1:
    user_input = st.text_input("", placeholder=f"Ask anything in {mode} mode... try 'Create image of a robotic tree'", label_visibility="collapsed")
with c2:
    send_btn = st.button("🎙️ Send")

# Master Logic (Yash's Masterpiece)
if send_btn and user_input:
    # 1. Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # --- Idea: Image Gen Check ---
    image_to_generate = None
    if "create image" in user_input.lower() or "draw" in user_input.lower():
        with st.spinner("YashProBot photo bana raha hai..."):
            image_to_generate = create_image_dummy(user_input.split("image of ")[-1]) # Use split as dummy method
    
    # 2. Get AI Chat Response based on think_level
    with st.spinner("YashProBot soch raha hai..."):
        full_prompt = f"""
            Imagine you are YashProBot, an AI made by Yash Tiwari from Class 9B. 
            Mode: {mode}. Thinking Level: {think_level}. 
            Answer this question to Yash in {lang}: {user_input}.
            If image generation was requested, start the answer by saying 'Okay Yash! Creating image...'
        """
        answer = get_ai_response(full_prompt)
    
    # 3. Prepare bot message structure
    bot_message = {"role": "assistant", "content": answer}
    if image_to_generate:
        bot_message["generated_image"] = image_to_generate # Save image in history

    # Add bot response to history
    st.session_state.chat_history.append(bot_message)
    
    # 4. Generate Voice
    tts = gTTS(text=answer[:200], lang='hi') # Limit to 200 chars for speed
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp, format='audio/mp3')
    
    # 5. Refresh
    change_bg()
    st.rerun()
