import streamlit as st


def show_chat():
    st.title("AI Creator")
    st.caption("Your Roblox development assistant")

    if "studiox_messages" not in st.session_state:
        st.session_state.studiox_messages = []

    if st.button("＋ New conversation", key="new_studiox_chat"):
        st.session_state.studiox_messages = []
        st.rerun()

    for message in st.session_state.studiox_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask about Roblox, Luau, game systems...")
    if not prompt:
        return

    st.session_state.studiox_messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = (
        "The chat interface is ready. The AI model has not been connected yet. "
        "In the next step, we'll connect the OpenAI API securely through "
        "Streamlit Secrets so your API key is never stored in GitHub."
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.studiox_messages.append(
        {"role": "assistant", "content": answer}
    )
