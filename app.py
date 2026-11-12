
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="StudioX AI",
    page_icon="🚀",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚀 StudioX AI")
st.sidebar.caption("Explore. Create. Build.")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Explore", "AI Creator", "Script Lab", "Model Lab", "Settings"]
)

# Dashboard
if page == "Dashboard":
    st.title("🚀 StudioX AI")
    st.subheader("Your AI-powered Roblox development workspace.")

    st.write("Welcome to StudioX AI!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Projects", "0")

    with col2:
        st.metric("Scripts", "0")

    with col3:
        st.metric("Status", "Online")

    st.divider()
    st.subheader("Quick Start")
    st.write("Choose a tool from the sidebar to get started.")

# Explore
elif page == "Explore":
    st.title("🌎 Explore")
    st.write("Discover Roblox game ideas, genres and trends.")

# AI Creator
elif page == "AI Creator":
    st.title("🤖 AI Creator")
    st.write("Create Roblox development ideas with AI.")

# Script Lab
elif page == "Script Lab":
    st.title("💻 Script Lab")
    st.write("Your future Luau scripting workspace.")

# Model Lab
elif page == "Model Lab":
    st.title("🧊 Model Lab")
    st.write("Your future 3D asset creation workspace.")

# Settings
elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("StudioX AI configuration.")
