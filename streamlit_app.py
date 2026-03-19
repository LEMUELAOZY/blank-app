import streamlit as st
import random

st.set_page_config(page_title="⭐ Star Navigator", layout="wide", page_icon="✨")

# -----------------------------
# DATA
# -----------------------------
stars = {
    "altair": {
        "name": "Altair",
        "short_desc": "Bright star in Aquila",
        "info": "Altair is part of the Summer Triangle and is one of the closest bright stars to Earth.",
        "sky_position": "Northern sky during summer evenings",
        "features": "Forms the Summer Triangle with Vega and Deneb.",
        "image": "images/altair.png"
    },
    "vega": {
        "name": "Vega",
        "short_desc": "Very bright star in Lyra",
        "info": "Vega is one of the brightest stars visible from Earth.",
        "sky_position": "High in the northern summer sky",
        "features": "Part of the Summer Triangle.",
        "image": "images/vega.png"
    }
}

constellations = {
    "ursa_major": {
        "name": "Ursa Major",
        "short_desc": "Large northern constellation containing the Big Dipper.",
        "info": "Ursa Major contains the Big Dipper which helps locate Polaris.",
        "image": "images/ursa_major.png"
    },
    "orion": {
        "name": "Orion",
        "short_desc": "Prominent winter constellation.",
        "info": "Orion is easily recognized by Orion's Belt.",
        "image": "images/orion.png"
    }
}

# -----------------------------
# GLASS UI STYLE
# -----------------------------
glass_style = """
<style>
body {
    background-color: #070F2B;
    color: white;
}
.glass-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
}
.stButton>button {
    background-color: #1B1A55;
    color: white;
    border-radius: 10px;
}
.stRadio>div>label, .stSelectbox>div>label {
    color: #9290C3;
}
</style>
"""
st.markdown(glass_style, unsafe_allow_html=True)

st.title("✨ Constellation Star Navigator ✨")
st.markdown("<div class='glass-box'>Select a star or constellation to see details and visualization.</div>", unsafe_allow_html=True)

# -----------------------------
# TWO-COLUMN LAYOUT
# -----------------------------
col1, col2 = st.columns(2)

with col2:  # Right column for input
    mode = st.radio("What do you know about your location?", ("Exact coordinates", "Environmental description", "No idea"))

    if mode == "Exact coordinates":
        lat = st.number_input("Enter Latitude:", value=0.0)
        lon = st.number_input("Enter Longitude:", value=0.0)
        visibility = st.selectbox("Sky Visibility", ["Clear", "Partial", "Low", "Obstructed"])

        if visibility == "Clear":
            view_choice = st.radio("What do you see?", ("A single star", "Multiple stars / constellation"))
            if view_choice == "A single star":
                star_choice = st.selectbox("Choose Star", list(stars.keys()))
            else:
                star_choice = st.selectbox("Choose Constellation", list(constellations.keys()))
        else:
            st.warning("Sky visibility is limited. Cannot provide precise details.")
            star_choice = None

    elif mode == "Environmental description":
        sea_color = st.selectbox("Sea color:", ["Blue", "Green", "Turquoise"])
        sea_life = st.selectbox("Sea life observed:", ["Fish", "Birds", "Whales", "None"])
        wind_dir = st.selectbox("Wind direction:", ["North", "South", "East", "West"])
        star_choice = random.choice(list(constellations.keys()))

    else:  # No idea
        sky_visible = st.radio("Can you see the sky and stars?", ("Yes", "No"))
        if sky_visible == "Yes":
            star_choice = st.selectbox("Choose Constellation", list(constellations.keys()))
        else:
            star_choice = random.choice(list(stars.keys()))

# -----------------------------
# DISPLAY IMAGE AND INFO
# -----------------------------
with col1:  # Left column for visualization
    if star_choice:
        if star_choice in stars:
            st.image(stars[star_choice]["image"], use_column_width=True)
        elif star_choice in constellations:
            st.image(constellations[star_choice]["image"], use_column_width=True)

with col2:  # Right column for details
    if star_choice:
        if star_choice in stars:
            star = stars[star_choice]
            st.markdown(f"<div class='glass-box'><h3>{star['name']}</h3><p>{star['short_desc']}</p></div>", unsafe_allow_html=True)
            st.write(f"Info: {star['info']}")
            st.write(f"Sky Position: {star['sky_position']}")
            st.write(f"Features: {star['features']}")
        elif star_choice in constellations:
            const = constellations[star_choice]
            st.markdown(f"<div class='glass-box'><h3>{const['name']}</h3><p>{const['short_desc']}</p></div>", unsafe_allow_html=True)
            st.write(f"Info: {const['info']}")
