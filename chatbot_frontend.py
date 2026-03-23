import streamlit as st
from chatbot_backend import demo_memory, demo_conversation

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Chat with your AI assistant below 👇")

# Initialize memory (only once)
if "memory" not in st.session_state:
    st.session_state.memory = demo_memory()

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", placeholder="Type your message here...")

# Send button
if st.button("Send") and user_input:
    response = demo_conversation(user_input, st.session_state.memory)
    
    # Save messages
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
st.subheader("💬 Chat History")
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"🧑 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")