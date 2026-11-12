import streamlit as st

SYSTEM_INSTRUCTIONS = """You are StudioX AI, a helpful Roblox development assistant.
Help users learn Roblox Studio and Luau. Prefer correct, beginner-friendly explanations.
When writing code, state where each script belongs (for example ServerScriptService,
StarterPlayerScripts, or a Part). Explain important assumptions and never claim code
was tested in Roblox Studio unless it actually was. Keep suggestions age-appropriate.
"""


def _init_chat_state():
    if "studiox_conversations" not in st.session_state:
        st.session_state.studiox_conversations = {
            "conversation_1": {
                "title": "New conversation",
                "messages": [],
            }
        }
    if "studiox_active_conversation" not in st.session_state:
        st.session_state.studiox_active_conversation = "conversation_1"
    if "studiox_next_conversation" not in st.session_state:
        st.session_state.studiox_next_conversation = 2
    if "studiox_conversation_picker" not in st.session_state:
        st.session_state.studiox_conversation_picker = st.session_state.studiox_active_conversation


def _new_conversation():
    number = st.session_state.studiox_next_conversation
    key = f"conversation_{number}"
    st.session_state.studiox_conversations[key] = {"title": "New conversation", "messages": []}
    st.session_state.studiox_next_conversation += 1
    st.session_state.studiox_active_conversation = key
    st.session_state.studiox_conversation_picker = key


def _get_api_key():
    try:
        return st.secrets.get("OPENAI_API_KEY", "")
    except Exception:
        return ""


def _generate_answer(messages):
    api_key = _get_api_key()
    if not api_key:
        return (
            "The AI connection is not configured yet. Your message is saved in this "
            "conversation for this browser session. To enable real AI replies, an "
            "adult can help configure an OpenAI API key in Streamlit Secrets. API "
            "usage may cost money; do not add billing details or keys without a parent "
            "or guardian."
        )

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-6-luna",
            instructions=SYSTEM_INSTRUCTIONS,
            input=[
                {"role": item["role"], "content": item["content"]}
                for item in messages
            ],
        )
        return response.output_text or "I couldn't produce a text response. Please try again."
    except Exception as exc:
        st.error("The AI request did not work. Check the API configuration and try again.")
        return f"Connection error: {type(exc).__name__}. No API key is displayed here."


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
    _init_chat_state()
    conversations = st.session_state.studiox_conversations

    st.title("✦ AI Creator")
    st.caption("Your workspace for Roblox ideas, Luau scripts and debugging.")

    left, right = st.columns([5, 1])
    with right:
        st.button("＋ New", use_container_width=True, on_click=_new_conversation)
    with left:
        labels = {
            key: value["title"]
            for key, value in conversations.items()
        }
        active = st.selectbox(
            "Conversation",
            options=list(labels.keys()),
            format_func=lambda key: labels[key],
            label_visibility="collapsed",
            key="studiox_conversation_picker",
        )
        st.session_state.studiox_active_conversation = active

    current = conversations[st.session_state.studiox_active_conversation]
    if not current["messages"]:
        st.info(
            "Try asking: **Create a checkpoint system in Luau** or "
            "**Explain the difference between a Script and a LocalScript.**"
        )

    for message in current["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask about Roblox, Luau, game systems...")
    if prompt:
        current["messages"].append({"role": "user", "content": prompt})
        if current["title"] == "New conversation":
            current["title"] = prompt[:36] + ("…" if len(prompt) > 36 else "")
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("StudioX is thinking..."):
                answer = _generate_answer(current["messages"])
            st.markdown(answer)
        current["messages"].append({"role": "assistant", "content": answer})
        st.rerun()

    if current["messages"]:
        st.caption("Conversation history is kept in this active browser session, not a permanent account.")
        if st.button("Clear this conversation"):
            current["messages"] = []
            current["title"] = "New conversation"
            st.rerun()
