import streamlit as st

from src.chat import show_chat
from src.labs import show_explore, show_model_lab, show_script_lab

st.set_page_config(
    page_title="StudioX AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #17233d 0, #0b0f19 42%);
        color: #f4f7ff;
    }
    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    [data-testid="stSidebar"] {
        background-color: #0d1422;
        border-right: 1px solid #26334b;
    }
    [data-testid="stMetric"] {
        background: #141e30;
        border: 1px solid #293852;
        padding: 16px;
        border-radius: 14px;
    }
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

if "studiox_conversations" not in st.session_state:
    st.session_state.studiox_conversations = {
        "conversation_1": {"title": "New conversation", "messages": []}
    }
if "studiox_scripts_created" not in st.session_state:
    st.session_state.studiox_scripts_created = 0

st.sidebar.title("🚀 StudioX AI")
st.sidebar.caption("Explore. Create. Build.")
st.sidebar.divider()

page = st.sidebar.radio(
    "WORKSPACE",
    ["Dashboard", "Explore", "AI Creator", "Script Lab", "Model Lab", "Settings"],
)

st.sidebar.divider()
st.sidebar.caption("StudioX AI · Early development")


def _api_configured():
    try:
        return bool(st.secrets.get("OPENAI_API_KEY", ""))
    except Exception:
        return False


if page == "Dashboard":
    st.title("🚀 StudioX AI")
    st.subheader("Your Roblox development workspace.")
    st.write("Plan ideas, write Luau and organize assets in one place.")
    conversations = st.session_state.studiox_conversations
    message_count = sum(len(item["messages"]) for item in conversations.values())
    col1, col2, col3 = st.columns(3)
    col1.metric("Conversations", len(conversations))
    col2.metric("Chat messages", message_count)
    col3.metric("AI connection", "Connected" if _api_configured() else "Not set up")
    st.divider()
    st.subheader("Quick start")
    cards = st.columns(3)
    with cards[0]:
        st.markdown("### ✦ AI Creator")
        st.write("Ask questions and work on Roblox systems.")
    with cards[1]:
        st.markdown("### ⌘ Script Lab")
        st.write("Edit starter Luau scripts and download them.")
    with cards[2]:
        st.markdown("### ◇ Model Lab")
        st.write("Write a clear brief for your next 3D asset.")
    st.caption("Note: AI connection requires an adult-managed API setup. Chat history is session-only.")

elif page == "Explore":
    show_explore()
elif page == "AI Creator":
    show_chat()
elif page == "Script Lab":
    show_script_lab()
elif page == "Model Lab":
    show_model_lab()
elif page == "Settings":
    st.title("⚙️ Settings")
    st.caption("StudioX AI configuration")
    configured = _api_configured()
    st.write("**OpenAI API:** " + ("Configured" if configured else "Not configured"))
    st.write("**Chat history:** Stored in the current browser session only.")
    st.write("**App hosting:** Streamlit Community Cloud.")
    st.divider()
    st.subheader("Enable real AI replies")
    st.write(
        "An adult can add an OPENAI_API_KEY secret in the Streamlit app settings. "
        "Never put an API key in GitHub or share it in chat. API usage is billed "
        "separately and may cost money, so ask a parent or guardian to review billing "
        "and usage limits before enabling it."
    )
    st.code('OPENAI_API_KEY = "your-key-goes-here"', language="toml")
    st.caption("Do not paste a real key into this example or into a public repository.")


