import streamlit as st
import time

# Page Setup
st.set_page_config(page_title="yashprobot.ai", page_icon="🤖", layout="wide")

# Login Check
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to yashprobot.ai")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pw == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Galat Password!")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("👨‍💻 Developer")
    st.write("**Name:** Kanchney Tiwari (Yash)")
    st.write("**School:** PM Shri KV Salempur")
    lang = st.selectbox("🌐 Language", ["Hinglish", "Hindi", "English", "Bhojpuri"])
    mode = st.radio("🛠 Feature", ["AI Chat", "Make Quiz", "Generate Photo"])

# Main Area
st.title("🤖 YashProBot.ai")

if "answering" not in st.session_state:
    st.session_state.answering = False

col1, col2 = st.columns([1, 2])

with col1:
    if st.session_state.answering:
        # Naya Link for Standing Robot
        st.image("https://img.freepik.com/free-vector/cute-robot-waving-hand-cartoon-character_1308-123344.jpg", width=300)
    else:
        # Naya Link for Sitting Robot
        st.image("https://img.freepik.com/free-vector/cute-robot-sitting-desk-with-laptop_1308-134265.jpg", width=300)

with col2:
    st.write(f"### Namaste Kanchney!")
    user_input = st.text_input("Aapka sawal:", placeholder="Yahan likhein...")
    
    if st.button("Puchiye / Send"):
        if user_input:
            st.session_state.answering = True
            st.rerun()

if st.session_state.answering:
    with col2:
        st.info(f"Kanchney, aapne pucha: {user_input}")
        st.success(f"Jawab {lang} mein taiyar hai! (Demo Mode)")
        if st.button("Theek hai (Robot Sit Down)"):
            st.session_state.answering = False
            st.rerun()
