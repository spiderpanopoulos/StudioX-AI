import streamlit as st


def show_chat():
    st.title("🤖 StudioX AI")
    st.caption("Your AI Roblox Development Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask StudioX anything about Roblox...")

    if prompt:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            st.write("AI connection coming soon!")

        st.session_state.messages.append({
            "role": "assistant",
            "content": "AI connection coming soon!"
        })
