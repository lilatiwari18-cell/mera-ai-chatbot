import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="YashProBot.ai", page_icon="🤖", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf,#2e7bcf); color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to YashProBot.ai")
    st.subheader("Kanchney's Personal AI Assistant")
    user = st.text_input("Username (Type 'admin')")
    pw = st.text_input("Password (Type '12345')", type="password")
    if st.button("Login"):
        if user == "admin" and pw == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Galat Password! Dubara koshish karein.")
    st.stop()

# 3. Stylish Robot Photos List
sitting_robots = [
    "https://cdn.pixabay.com/photo/2023/11/04/18/12/cute-robot-8365615_1280.png",
    "https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
    "https://cdn-icons-png.flaticon.com/512/2044/2044810.png"
]

talking_robots = [
    "https://cdn-icons-png.flaticon.com/512/4712/4712139.png",
    "https://cdn-icons-png.flaticon.com/512/1782/1782384.png",
    "https://cdn-icons-png.flaticon.com/512/6134/6134346.png"
]

# 4. Sidebar with Profile
with st.sidebar:
    st.header("👨‍💻 Developer Profile")
    st.write("**Name:** Kanchney Tiwari (Yash)")
    st.write("**Class:** 9th 'B'")
    st.write("**School:** PM Shri KV Chero, Salempur")
    st.markdown("---")
    st.write("👪 **Parents:**")
    st.write("- Mr. Awadhesh Tiwari")
    st.write("- Mrs. Lila Tiwari")
    st.markdown("---")
    lang = st.selectbox("🌐 Language", ["Hinglish", "Hindi", "English", "Bhojpuri"])
    mode = st.radio("🛠 Feature", ["AI Chat", "Make Quiz", "Generate Photo"])

# 5. Main Chat Interface
st.title("🤖 YashProBot.ai")

if "answering" not in st.session_state:
    st.session_state.answering = False

col1, col2 = st.columns([1, 2])

with col1:
    if st.session_state.answering:
        # Random Stylish Robot while answering
        st.image(random.choice(talking_robots), width=300)
        st.caption("YashProBot is Thinking...")
    else:
        # Random Stylish Robot while sitting
        st.image(random.choice(sitting_robots), width=300)
        st.caption("YashProBot is ready to help!")

with col2:
    st.write(f"### Namaste Kanchney!")
    
    if mode == "AI Chat":
        user_input = st.text_input("Aapka sawal:", placeholder="Yahan kuch puchiye...")
        if st.button("Send Message"):
            if user_input:
                st.session_state.answering = True
                st.session_state.last_msg = user_input
                st.rerun()

    elif mode == "Make Quiz":
        st.write("📝 **Quick Quiz Mode**")
        st.info("What is the square root of 144?")
        ans = st.text_input("Your Answer:")
        if st.button("Submit"):
            if ans == "12": st.success("Sahi jawab, Kanchney!")
            else: st.error("Try again!")

    elif mode == "Generate Photo":
        prompt = st.text_input("Kaisi photo chahiye?", placeholder="Example: Robot playing cricket")
        if st.button("Generate Art"):
            st.session_state.answering = True
            st.session_state.last_msg = f"Generating: {prompt}"
            st.rerun()

# 6. Response Display
if st.session_state.answering:
    with col2:
        st.markdown("---")
        with st.spinner("AI processing..."):
            time.sleep(1.5)
            st.chat_message("assistant").write(f"Kanchney, main aapke '{st.session_state.last_msg}' par kaam kar raha hoon. Jawab {lang} mein taiyar hai!")
            
            if st.button("Clear / Next"):
                st.session_state.answering = False
                st.rerun()
