import streamlit as st


def show_chat():
    st.markdown(
        """
        <style>
        div[data-testid="stChatInput"] textarea {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            caret-color: #ffffff !important;
            background-color: #151c2c !important;
        }

        div[data-testid="stChatInput"] textarea::placeholder {
            color: #aab4c5 !important;
            -webkit-text-fill-color: #aab4c5 !important;
            opacity: 1 !important;
        }

        div[data-testid="stChatInput"] {
            border-color: #52617a !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
