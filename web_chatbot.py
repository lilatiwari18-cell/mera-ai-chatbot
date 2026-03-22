import streamlit as st
import random

st.set_page_config(page_title="Yash AI 🤖", layout="wide")

# 🌄 20 Background Images (free Unsplash links)
backgrounds = [
"https://images.unsplash.com/photo-1501785888041-af3ef285b470",
"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
"https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
"https://images.unsplash.com/photo-1493244040629-496f6d136cc3",
"https://images.unsplash.com/photo-1506744038136-46273834b3fb",
"https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
"https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
"https://images.unsplash.com/photo-1501785888041-af3ef285b470",
"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
"https://images.unsplash.com/photo-1503264116251-35a269479413",
"https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
"https://images.unsplash.com/photo-1519681393784-d120267933ba",
"https://images.unsplash.com/photo-1491553895911-0055eca6402d",
"https://images.unsplash.com/photo-1439066615861-d1af74d74000",
"https://images.unsplash.com/photo-1502082553048-f009c37129b9",
"https://images.unsplash.com/photo-1469474968028-56623f02e42e",
"https://images.unsplash.com/photo-1500534623283-312aade485b7",
"https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
"https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
]

# 🎨 Background changer
if "bg" not in st.session_state:
    st.session_state.bg = random.choice(backgrounds)

if st.button("🌄 Change Background"):
    st.session_state.bg = random.choice(backgrounds)

# 💎 Stylish CSS
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins&display=swap');

.stApp {{
    background: url("{st.session_state.bg}");
    background-size: cover;
    background-position: center;
}}

h1, h2, h3 {{
    font-family: 'Pacifico', cursive;
    color: #ffffff;
}}

p, div {{
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
}}

.chat-box {{
    background: rgba(0,0,0,0.5);
    padding: 15px;
    border-radius: 15px;
}}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Yash AI Chatbot")
st.write("✨ Made by Yash Tiwari")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

# Simple reply
def reply_func(q):
    if "hello" in q.lower():
        return "Hello 👋! Kaise ho?"
    elif "kaun ho" in q.lower():
        return "Main Yash ka AI chatbot hoon 😎"
    else:
        return "Nice question 😄 main abhi simple version hoon."

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = reply_func(user_input)

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
