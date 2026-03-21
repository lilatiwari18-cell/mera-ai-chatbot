import streamlit as st
import random
from gtts import gTTS
import io

# ==========================================
# 1. THE DESIGNER INTERFACE (NEON GLASS LOOK)
# ==========================================
st.set_page_config(page_title="YashProBot.ai - Ultra Design", page_icon="💎", layout="wide")

# High-Res Tree/Nature Backgrounds
bgs = [
    "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d", # Dark Forest
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9", # Canopy
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"  # Sunlight
]

if 'bg' not in st.session_state: st.session_state.bg = bgs[0]
if 'chat' not in st.session_state: st.session_state.chat = []
if 'score' not in st.session_state: st.session_state.score = 0

# Custom CSS for Design & Clear Text
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{st.session_state.bg}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    /* Main Card */
    .glass-card {{
        background: rgba(0, 0, 0, 0.8); 
        border: 2px solid #00ffcc;
        border-radius: 25px; 
        padding: 30px; 
        text-align: center; 
        color: white;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
        margin-bottom: 25px;
    }}
    /* Bot Chat Bubble */
    .bot-bubble {{
        background: linear-gradient(135deg, rgba(0,255,204,0.2), rgba(0,0,0,0.9));
        color: #00ffcc !important; 
        padding: 20px; 
        border-radius: 15px 15px 15px 0px; 
        border-left: 5px solid #00ffcc;
        font-size: 1.15em; 
        font-weight: bold;
        text-shadow: 1px 1px 3px black;
        margin-bottom: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }}
    /* User Chat Bubble */
    .user-bubble {{
        background: rgba(255, 255, 255, 0.15); 
        color: white !important; 
        padding: 12px; 
        border-radius: 15px 15px 0px 15px; 
        text-align: right;
        margin-bottom: 15px; 
        font-weight: 500;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background: rgba(0, 0, 0, 0.9) !important;
        border-right: 2px solid #00ffcc;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. THE KNOWLEDGE ENGINE (LEVELS & SUBJECTS)
# ==========================================
@st.cache_data
def get_mega_brain():
    return {
        "Maths Expert": {
            "Medium ⚙️": "Circle Area = πr². Rectangle = L×B.",
            "Thinking 🤔": "Heron's Formula: √[s(s-a)(s-b)(s-c)].",
            "Pro 🔥": "If x+1/x=3, then x²+1/x²=7. Sphere Vol = 4/3πr³."
        },
        "Science Lab": {
            "Medium ⚙️": "Cell is life's unit. Water formula is H2O.",
            "Thinking 🤔": "Force F = m×a. Earth Gravity g = 9.8 m/s².",
            "Pro 🔥": "Speed of light is 3x10^8 m/s. DNA is in Nucleus."
        },
        "SST & GK": {
            "Medium ⚙️": "Modi is India's PM. Delhi is the Capital.",
            "Thinking 🤔": "Article 370 was in Kashmir. Patel is Iron Man.",
            "Pro 🔥": "India became Republic on 26 Jan 1950. Asia is largest."
        }
    }

data = get_mega_brain()

def get_response(q, level, sub):
    q = q.lower()
    # 1. Identity
    if any(w in q for w in ["kaun", "who", "name"]):
        return "Mera naam YashProBot.ai hai! Mujhe Class 9-B ke software star Yash Tiwari ne banaya hai."
    
    # 2. Smart Knowledge Fetch
    subject_db = data.get(sub, data["SST & GK"])
    if any(w in q for w in ["batao", "tell", "what", "pucho", "info"]):
        return f"💡 [{level}] Info: " + subject_db.get(level, "Seeking data...")

    # 3. Quiz Trigger
    if any(w in q for w in ["quiz", "question", "sawal", "test"]):
        return f"🌟 {sub} ({level}) Quiz: Kya aap taiyar hain? 'Start' likhein!"

    return f"Jai Shree Ram! Aapne {sub} mein {level} par '{q}' pucha. Yash Tiwari ka bot seekh raha hai!"

# ==========================================
# 3. SIDEBAR CONTROLS (THE SETTINGS)
# ==========================================
with st.sidebar:
    st.markdown("<div class='glass-card' style='padding:10px;'>👑 YASH TIWARI</div>", unsafe_allow_html=True)
    st.write("**Section:** 9-B | KV Salempur")
    st.metric("🏆 Your Score", st.session_state.score)
    
    st.markdown("---")
    level_choice = st.selectbox("🧠 Choose Brain Level", ["Medium ⚙️", "Thinking 🤔", "Pro 🔥"])
    sub_choice = st.selectbox("📚 Select Subject", ["Math
