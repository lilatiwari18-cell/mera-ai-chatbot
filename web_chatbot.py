import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="YashProBot.ai", page_icon="🤖", layout="wide")

# 2. Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to YashProBot.ai")
    st.info("Kanchney's Personal AI Assistant")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pw == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Galat Password! Dubara koshish karein.")
    st.stop()

# 3. Sidebar
with st.sidebar:
    st.header("👨‍💻 Developer Profile")
    st.write("**Name:** Kanchney Tiwari (Yash)")
    st.write("**Class:** 9th 'B'")
    st.write("**School:** PM Shri KV Chero, Salempur")
    st.markdown("---")
    lang = st.selectbox("🌐 Language", ["Hinglish", "Hindi", "English", "Bhojpuri"])
    sub = st.selectbox("📚 Subject", ["Maths", "Science", "SST", "AI"])
    mode = st.radio("🛠 Feature", ["AI Chat", "Make Quiz", "Generate Photo"])

# 4. Robot Logic & Photos
st.title("🤖 YashProBot.ai")

if "answering" not in st.session_state:
    st.session_state.answering = False

col1, col2 = st.columns([1, 2])

with col1:
    if st.session_state.answering:
        # REAL ROBOT PHOTO (Talking/Standing)
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712139.png", width=280)
        st.caption("YashProBot is Thinking...")
    else:
        # REAL ROBOT PHOTO (Sitting/Studying)
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=280)
        st.caption("YashProBot is ready to help!")

# 5. Features Logic
with col2:
    st.write(f"### Namaste Kanchney! Main {sub} ka expert hoon.")
    
    if mode == "AI Chat":
        user_input = st.text_input("Aapka sawal:", placeholder="Yahan kuch puchiye...")
        if st.button("Puchiye / Send"):
            if user_input:
                st.session_state.answering = True
                st.rerun()

    elif mode == "Make Quiz":
        st.write("📝 **Quick Quiz for you!**")
        q_list = ["What is 25 x 4?", "Formula of (a+b)^2?", "Who discovered Gravity?", "Full form of AI?"]
        st.warning(random.choice(q_list))
        st.text_input("Apna jawab yahan likhein:")
        if st.button("Submit Answer"):
            st.success("Bahut badiya Kanchney! Sahi jawab.")

    elif mode == "Generate Photo":
        prompt = st.text_input("Kaisi photo banau?", placeholder="Example: Flying car in Salempur")
        if st.button("Generate Image"):
            st.session_state.answering = True
            st.info(f"Kanchney, main '{prompt}' ki image search kar raha hoon...")
            time.sleep(2)
            # Placeholder for generated image
            st.image("https://img.freepik.com/free-photo/view-futuristic-city-with-advanced-technology_23-2150821558.jpg", caption="AI Generated View")

# 6. Reset Button
if st.session_state.answering:
    if st.button("Theek hai (Robot Sit Down)"):
        st.session_state.answering = False
        st.rerun()
