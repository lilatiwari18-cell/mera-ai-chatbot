import streamlit as st
import time

# 1. Page Settings
st.set_page_config(page_title="yashprobot.ai", page_icon="🤖", layout="wide")

# Custom CSS for YashProBot Look
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { background-color: #1E88E5; color: white; border-radius: 8px; font-weight: bold; }
    .sidebar .sidebar-content { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 2. Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to yashprobot.ai")
    st.info("Please Login to access Yash's AI Assistant")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pw == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Galat Password! Try again.")
    st.stop()

# 3. Sidebar with Personal Details
with st.sidebar:
    st.header("👨‍💻 Developer Profile")
    st.write("**Name:** Yash (Kanchan) Tiwari")
    st.write("**Class:** 9th 'B'")
    st.write("**School:** PM Shri KV Chero, Salempur")
    st.write("**Address:** Near St. Paul's School, Devpar, Salempur")
    st.markdown("---")
    st.write("👪 **Parents:**")
    st.write("- Mr. Awadhesh Tiwari")
    st.write("- Mrs. Lila Tiwari")
    st.markdown("---")
    
    lang = st.selectbox("🌐 Language", ["Hinglish", "Hindi", "English", "Bhojpuri", "Sanskrit", "Urdu", "Arabic", "Gujarati", "Bengali", "Tamil"])
    sub = st.selectbox("📚 Subject (1-12)", ["Maths", "Science", "SST", "AI", "English", "Hindi", "Biology", "Commerce", "Humanity"])
    mode = st.radio("🛠 Feature", ["AI Chat", "Make Quiz", "Generate Photo"])

# 4. Robot Animation & Interface
st.title("🤖 YashProBot.ai")

if "answering" not in st.session_state:
    st.session_state.answering = False

col1, col2 = st.columns([1, 2])

with col1:
    if st.session_state.answering:
        # Standing Robot (Answer Mode)
        st.image("http://googleusercontent.com/image_collection/image_retrieval/2528766189316112488_0", caption="YashProBot is explaining...")
    else:
        # Sitting Robot (Study Mode)
        st.image("http://googleusercontent.com/image_collection/image_retrieval/2354808910096508476_0", caption="YashProBot is studying at his desk...")

with col2:
    st.write(f"### Hello! Main {sub} ka expert hoon.")
    user_input = st.text_input("Aapka sawal ya Image prompt:", placeholder="Yahan likhein...")
    
    if st.button("Puchiye / Send"):
        if user_input:
            st.session_state.answering = True
            st.rerun()

# 5. Logic for Standing Robot
if st.session_state.answering:
    with col2:
        with st.spinner("YashProBot soch raha hai..."):
            time.sleep(3) # Animation feel
            
            if mode == "Generate Photo":
                st.success("YashProBot ne aapki photo generate kar di hai!")
                st.image("https://via.placeholder.com/500x300.png?text=AI+Generated+Image+by+YashProBot", caption=user_input)
            elif mode == "Make Quiz":
                st.write(f"📝 **{sub} Quiz in {lang}:**")
                st.write("1. What is the most important part of this topic?")
            else:
                st.chat_message("assistant").write(f"Main YashProBot hoon. Aapke sawal '{user_input}' ka jawab {lang} mein taiyar hai...")
            
            if st.button("Answer Mil Gaya! (Sit Down)"):
                st.session_state.answering = False
                st.rerun()
