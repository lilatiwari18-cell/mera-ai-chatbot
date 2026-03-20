import streamlit as st
import random
import time

st.set_page_config(page_title="YashProBot.ai", page_icon="🤖")

# Login Check
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Login to YashProBot")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if u == "admin" and p == "12345":
            st.session_state['logged_in'] = True
            st.rerun()
    st.stop()

# 100% Working Robot Links
robots = [
    f"https://api.dicebear.com/7.x/bottts/svg?seed={random.randint(1,1000)}",
    f"https://api.dicebear.com/7.x/bottts/svg?seed={random.randint(1001,2000)}"
]

with st.sidebar:
    st.header("👨‍💻 Kanchney Tiwari")
    st.write("Class 9th 'B' | KV Salempur")
    mode = st.radio("Feature", ["AI Chat", "Make Quiz"])

st.title("🤖 YashProBot.ai")

col1, col2 = st.columns([1, 2])

with col1:
    # Ye link hamesha naya stylish robot dikhayega
    st.image(random.choice(robots), width=250)
    st.caption("Main aapka stylish robot hoon!")

with col2:
    st.write("### Namaste Kanchney!")
    msg = st.text_input("Kuch puchiye:")
    if st.button("Send"):
        st.success(f"Aapne pucha: {msg}. Main is par kaam kar raha hoon!")
