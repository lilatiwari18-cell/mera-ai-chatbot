import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import json

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("sk-proj-MPGEcKdSKk4gsbzHDUczuyEQcn7deN85BZ00a3qNUEq-TZDGICfOCAffek4J2_6elaIe9VMjNFT3BlbkFJlh6YpnjV7qnXijIr73x_1CGqRZQ8VYDOZNkHyiMqTERcV16iu7o6TaADEmOdq3OJwHt88p0oUA"))

# Page config
st.set_page_config(page_title="Yash AI 🤖", layout="wide")

# 🎨 Background style
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 🔐 LOGIN SYSTEM
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "yash" and password == "1234":
        st.session_state.logged_in = True
    else:
        st.error("Wrong credentials")

if not st.session_state.logged_in:
    st.stop()

# Title
st.title("🤖 Yash AI Chatbot + Image Generator 🎨")
st.write("Made by **Yash Tiwari** 🚀")

# 🎤 Voice Input
def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, could not understand"

# 🔊 Voice Output
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 🎤 Mic button
if st.button("🎤 Speak"):
    user_input = voice_input()
else:
    user_input = st.chat_input("Type your message...")

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
        # 🤖 Chatbot
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a smart AI tutor for class 1 to 12 students.
Explain answers in simple language.
"""
                    }
                ] + st.session_state.messages
            )

            reply = response.choices[0].message.content
            st.write(reply)

            st.session_state.messages.append({
                "role": "assistant",
                "content": reply
            })

            # 🔊 Speak button
            if st.button("🔊 Speak Reply"):
                speak(reply)

# 📄 Download chat
if st.button("💾 Download Chat"):
    chat_data = json.dumps(st.session_state.messages, indent=2)

    st.download_button(
        label="Download",
        data=chat_data,
        file_name="chat.json",
        mime="application/json"
    )
