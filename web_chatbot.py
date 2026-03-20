import streamlit as st
import time

# 1. Page Settings
st.set_page_config(page_title="yashprobot.ai", page_icon="🤖", layout="wide")

# Custom CSS for YashProBot Look
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to yashprobot.ai")
    st.info("Please Login to access Kanchney's AI Assistant")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pw == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Galat Password! Try again.")
    st.stop()

# 3. Sidebar with Updated Name
with st.sidebar:
    st.header("👨‍💻 Developer Profile")
    st.write("**Name:** Kanchney Tiwari (Yash)") # Updated Name Here
    st.write("**Class:** 9th 'B'")
    st.write("**School:** PM Shri KV Chero, Salempur")
    st.write("**Address:** Near St. Paul's School, Devpar, Salempur")
    st.markdown("---")
    st.write("👪 **Parents:**")
    st.write("- Mr. Awadhesh Tiwari")
    st.write("- Mrs. Lila Tiwari")
    st.markdown("---")
    
    lang = st.selectbox("🌐 Language", ["Hinglish", "Hindi", "English", "Bhojpuri"])
    sub = st.selectbox("📚 Subject", ["Maths", "Science", "SST", "AI"])
    mode = st.radio("🛠 Feature", ["AI Chat", "Make Quiz", "Generate Photo"])

# 4. Robot Interface
st.title("🤖 YashProBot.ai")

if "answering" not in st.session_state:
    st.session_state.answering = False

col1, col2 = st.columns([1, 2])

with col1:
    if st.session_state.answering:
        st.image("http://googleusercontent.com/image_collection/image_retrieval/2528766189316112488_0", caption="YashProBot is explaining...")
    else:
        st.image("http://googleusercontent.com/image_collection/image_retrieval/2354808910096508476_0", caption="YashProBot is studying...")

with col2:
    st.write(f"### Namaste Kanchney! Main {sub} ka expert hoon.")
    user_input = st.text_input("Aapka sawal:", placeholder="Yahan likhein...")
    
    if st.button("Puchiye / Send"):
        if user_input:
            st.session_state.answering = True
            st.rerun()

# 5. Answer Logic
if st.session_state.answering:
    with col2:
        with st.spinner("YashProBot soch raha hai..."):
            time.sleep(2)
            st.chat_message("assistant").write(f"Kanchney, aapne '{user_input}' pucha hai. Main iska jawab {lang} mein taiyar kar raha hoon...")
            
            if st.button("Answer Mil Gaya!"):
                st.session_state.answering = False
                st.rerun()
