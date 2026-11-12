import streamlit as st

SCRIPT_TEMPLATES = {
    "Coin leaderstats": """-- Place this Script in ServerScriptService
game.Players.PlayerAdded:Connect(function(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local coins = Instance.new("IntValue")
    coins.Name = "Coins"
    coins.Value = 0
    coins.Parent = leaderstats
end)
""",
    "Simple checkpoint": """-- Place this Script inside each checkpoint Part.
-- Set the Part's Attribute "CheckpointNumber" to a different number.
local checkpoint = script.Parent

checkpoint.Touched:Connect(function(hit)
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if not player then return end

    local current = player:GetAttribute("Checkpoint")
    local number = checkpoint:GetAttribute("CheckpointNumber") or 1

    if not current or number > current then
        player:SetAttribute("Checkpoint", number)
    end
end)
""",
    "Part touch message": """-- Place this Script inside a Part.
local part = script.Parent
local debounce = {}

part.Touched:Connect(function(hit)
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if not player or debounce[player] then return end

    debounce[player] = true
    print(player.Name .. " touched the part!")

    task.wait(1)
    debounce[player] = nil
end)
""",
}


def show_script_lab():
    st.title("⌘ Script Lab")
    st.caption("Start from a template, edit Luau and export your script.")
    template_name = st.selectbox("Starter template", list(SCRIPT_TEMPLATES))
    default_code = SCRIPT_TEMPLATES[template_name]
    code = st.text_area(
        "Luau editor",
        value=default_code,
        height=360,
        key=f"script_editor_{template_name}",
    )
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "Download .lua",
            data=code,
            file_name=template_name.lower().replace(" ", "_") + ".lua",
            mime="text/plain",
            use_container_width=True,
        )
    with col2:
        if st.button("Reset to template", use_container_width=True):
            st.session_state[f"script_editor_{template_name}"] = default_code
            st.rerun()
    st.info(
        "The editor is a text editor, not a Roblox Luau runtime. Test scripts in "
        "Roblox Studio before using them in a published experience."
    )


def show_explore():
    st.title("🌎 Explore")
    st.caption("Game concepts to help you plan your next Roblox experience.")
    ideas = [
        ("Obby with changing routes", "Players choose between safe, tricky and timed paths.", "Obby", "Checkpoints, timer, route choices"),
        ("Cozy space station", "Players maintain a small station and unlock new rooms.", "Simulation", "Resource collection, upgrades, quests"),
        ("Museum of mysteries", "Players explore rooms and solve logic puzzles together.", "Adventure", "Clue system, doors, inventory"),
        ("Mini-game arcade", "A hub that rotates through short skill-based games.", "Party", "Round manager, leaderboard, rewards"),
        ("Build-a-planet", "Players customize a tiny planet and visit friends.", "Creative", "Placement system, saving, visitors"),
        ("Pet discovery garden", "Players discover friendly creatures and decorate habitats.", "Collection", "Discovery journal, habitats, cosmetics"),
    ]
    cols = st.columns(2)
    for index, (name, description, genre, systems) in enumerate(ideas):
        with cols[index % 2]:
            with st.container(border=True):
                st.subheader(name)
                st.write(description)
                st.caption(f"Genre: {genre}")
                st.write(f"**Possible systems:** {systems}")
    st.caption("These are original project ideas, not live Roblox trend rankings.")


def show_model_lab():
    st.title("◇ Model Lab")
    st.caption("Plan a 3D asset before building it in your 3D workflow.")
    with st.form("model_brief_form"):
        name = st.text_input("Asset name", placeholder="Example: Small sci-fi generator")
        style = st.selectbox("Visual style", ["Low-poly", "Cartoon", "Realistic", "Sci-fi", "Fantasy"])
        purpose = st.text_area("What should it look like and do?", placeholder="Describe shape, materials, colors and purpose...")
        scale = st.selectbox("Approximate size", ["Small prop", "Character-sized", "Large structure"])
        submitted = st.form_submit_button("Create asset brief")
    if submitted:
        if not name.strip() or not purpose.strip():
            st.warning("Add an asset name and a short description first.")
        else:
            brief = (
                f"ASSET: {name}\nSTYLE: {style}\nSIZE: {scale}\n"
                f"DESCRIPTION: {purpose}\n\n"
                "ROBLOX NOTES:\n- Keep the silhouette readable.\n"
                "- Use a sensible part count and anchored parts where appropriate.\n"
                "- Check collision and material settings in Roblox Studio.\n"
            )
            st.session_state["studiox_latest_model_brief"] = brief
    brief = st.session_state.get("studiox_latest_model_brief")
    if brief:
        st.subheader("Your asset brief")
        st.code(brief, language="text")
        st.download_button("Download brief", brief, file_name="studiox_asset_brief.txt", mime="text/plain")
    st.info(
        "This module currently creates design briefs. It does not yet generate or export "
        "3D model files or insert assets into Roblox Studio."
    )
