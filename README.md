# 🚀 StudioX AI

**Explore. Create. Build.**

A Roblox development workspace built with Python and Streamlit.

## Current modules

- **Dashboard:** Session-level conversation and message counts.
- **Explore:** Original Roblox game concepts and system ideas.
- **AI Creator:** Multi-conversation chat interface powered by the Gemini API when configured.
- **Script Lab:** Edit and download starter Luau scripts.
- **Model Lab:** Create and download 3D asset design briefs.

## Run locally

1. Install dependencies: `pip install -r requirements.txt`
2. Start the app: `streamlit run app.py`

## Optional Gemini API connection

Add a `GEMINI_API_KEY` secret in Streamlit's app settings. Never commit API keys to GitHub, paste them into source code, or share them in chat. The Gemini API offers a free tier with usage limits. A parent or guardian should help with account setup and review the provider's privacy terms before enabling it.

Google's free-tier terms say submitted content may be used to improve its products. Do not send private or sensitive information to the AI.

Without the secret, the interface and offline tools remain available, but AI Creator will explain that the AI connection is not configured.

## Important limitations

- Chat history is kept in Streamlit's current browser session; there is no account system or permanent cloud history yet.
- Script Lab is a text editor and template library, not a Luau runtime. Test code in Roblox Studio.
- Model Lab creates design briefs only; it does not generate 3D files.
- Explore contains curated ideas, not live Roblox trend analytics.
- The hosted Streamlit app cannot directly edit a running Roblox Studio project. A separate local integration would be needed for that.

## Security

This repository is public. Do not store secrets, passwords, API keys, or private user data in it.
