import streamlit as st

# Website ka Title
st.title("🤖 Mera AI Chatbot")
st.write("Namaste! Main ek Python-based AI hoon. Mujhse baatchit karein.")

# Chat history ko store karne ke liye (taaki message gayab na ho)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User se input lena
if prompt := st.chat_input("Yahan kuch type karein..."):
    # User ka message screen par dikhana
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Chatbot ka logic (Aap yahan apni dictionary wala logic laga sakte hain)
    response = "Main abhi seekh raha hoon, lekin aapne kaha: " + prompt
    if "hello" in prompt.lower():
        response = "Hello! Kaise ho aap?"
    elif "game" in prompt.lower():
        response = "Mujhe pata hai aapko games pasand hain!"

    # Chatbot ka jawab screen par dikhana
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
