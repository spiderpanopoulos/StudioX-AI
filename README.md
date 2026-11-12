# 🚀 StudioX AI

**Explore. Create. Build.**

A Roblox development workspace built with Python and Streamlit.

## Current modules

- **Dashboard:** Session-level conversation and message counts.
- **Explore:** Original Roblox game concepts and system ideas.
- **AI Creator:** Multi-conversation chat interface. Real AI replies are optional and require an OpenAI API key in Streamlit Secrets.
- **Script Lab:** Edit and download starter Luau scripts.
- **Model Lab:** Create and download 3D asset design briefs.

## Run locally

1. Install dependencies: `pip install -r requirements.txt`
2. Start the app: `streamlit run app.py`

## Optional OpenAI connection

Add an `OPENAI_API_KEY` secret in Streamlit's app settings. Never commit API keys to GitHub or paste them into source code. API usage is billed separately and may incur charges. A parent or guardian should review billing and usage limits before enabling paid API access.

The app uses the OpenAI Responses API. Without the secret, the interface and offline tools remain available, but AI Creator will explain that the AI connection is not configured.

## Important limitations

- Chat history is kept in Streamlit's current browser session; there is no account system or permanent cloud history yet.
- Script Lab is a text editor and template library, not a Luau runtime. Test code in Roblox Studio.
- Model Lab creates design briefs only; it does not generate 3D files.
- Explore contains curated ideas, not live Roblox trend analytics.
- The hosted Streamlit app cannot directly edit a running Roblox Studio project. A separate local integration would be needed for that.

## Security

This repository is public. Do not store secrets, passwords, API keys, or private user data in it.
