import streamlit as st
from openai import OpenAI

# API key from Streamlit secrets
client = OpenAI(api_key=st.secrets[""])

# Page config
st.set_page_config(page_title="Yash AI 🤖", layout="wide")

# 🎨 Natural background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #89f7fe, #66a6ff);
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Yash AI - Smart Study Chatbot")
st.write("Made by **Yash Tiwari** 🚀")

# 🧠 Level selector
level = st.selectbox("Select Answer Level 🧠", 
                     ["Basic 😄", "Medium 🙂", "Pro 😎", "Thinking 🧠"])

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Ask anything (Study / General / Image)...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # 🎨 Image generation
    if "image" in user_input.lower() or "draw" in user_input.lower():
        with st.chat_message("assistant"):
            st.write("🎨 Generating image...")

            img = client.images.generate(
                model="gpt-image-1",
                prompt=user_input,
                size="512x512"
            )

            image_url = img.data[0].url
            st.image(image_url)

            reply = "Here is your image 🎨"

            st.session_state.messages.append({
                "role": "assistant",
                "content": reply
            })

    else:
        # 🤖 Smart chatbot with levels
        with st.chat_message("assistant"):

            system_prompt = f"""
You are a friendly AI tutor for class 1 to 12 students.

Rules:
- Answer all subjects (Math, Science, English, etc.)
- Be friendly and conversational (like a human friend)
- If user asks casual questions (like "tum kya kar rahe ho"), reply naturally
- Adjust explanation based on level:

Basic: very simple, short
Medium: clear with small explanation
Pro: detailed explanation
Thinking: deep explanation with logic and reasoning

Give clean, correct answers.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt + f"\nLevel: {level}"}
                ] + st.session_state.messages
            )

            reply = response.choices[0].message.content
            st.write(reply)

            st.session_state.messages.append({
                "role": "assistant",
                "content": reply
            })
