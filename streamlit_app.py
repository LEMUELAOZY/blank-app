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
        "svg": """
<svg width="400" height="400">
  <circle cx="200" cy="200" r="8" fill="yellow"/>
  <circle cx="100" cy="100" r="5" fill="white"/>
  <circle cx="300" cy="100" r="5" fill="white"/>
  <circle cx="100" cy="300" r="5" fill="white"/>
  <circle cx="300" cy="300" r="5" fill="white"/>
</svg>
"""
    },
    "vega": {
        "name": "Vega",
        "short_desc": "Very bright star in Lyra",
        "info": "Vega is one of the brightest stars visible from Earth.",
        "sky_position": "High in the northern summer sky",
        "features": "Part of the Summer Triangle.",
        "svg": """
<svg width="400" height="400">
  <circle cx="200" cy="100" r="8" fill="yellow"/>
  <circle cx="100" cy="200" r="5" fill="white"/>
  <circle cx="300" cy="200" r="5" fill="white"/>
  <circle cx="200" cy="300" r="5" fill="white"/>
</svg>
"""
    }
}

constellations = {
    "ursa_major": {
        "name": "Ursa Major",
        "short_desc": "Large northern constellation containing the Big Dipper.",
        "info": "Ursa Major contains the Big Dipper which helps locate Polaris.",
        "svg": """
<svg width="400" height="300">
  <circle cx="50" cy="50" r="8" fill="yellow"/>
  <circle cx="100" cy="50" r="8" fill="yellow"/>
  <circle cx="150" cy="75" r="8" fill="yellow"/>
  <circle cx="200" cy="100" r="8" fill="yellow"/>
  <circle cx="250" cy="125" r="8" fill="yellow"/>
  <line x1="50" y1="50" x2="100" y2="50" stroke="white" stroke-width="2"/>
  <line x1="100" y1="50" x2="150" y2="75" stroke="white" stroke-width="2"/>
  <line x1="150" y1="75" x2="200" y2="100" stroke="white" stroke-width="2"/>
  <line x1="200" y1="100" x2="250" y2="125" stroke="white" stroke-width="2"/>
</svg>
"""
    }
}

# -----------------------------
# GLASS UI STYLE
# -----------------------------
glass_style = """
<style>
.glass-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(8px);
    border-radius: 15px;
    padding: 20px;
    color: white;
    margin-bottom: 20px;
}
body {
    background-color: #0b0c1a;
    color: white;
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
        sea_color = st.text_input("Sea color (blue/green/turquoise):")
        sea_life = st.text_input("Sea life observed (fish/birds/whales):")
        wind_dir = st.text_input("Wind direction (north/south/east/west):")
        star_choice = random.choice(list(constellations.keys()))

    else:  # No idea
        sky_visible = st.radio("Can you see the sky and stars?", ("Yes", "No"))
        if sky_visible == "Yes":
            star_choice = st.selectbox("Choose Constellation", list(constellations.keys()))
        else:
            star_choice = random.choice(list(stars.keys()))

# -----------------------------
# DISPLAY SVG AND INFO
# -----------------------------
with col1:  # Left column for SVG visualization
    if star_choice:
        if star_choice in stars:
            st.markdown(stars[star_choice]["svg"], unsafe_allow_html=True)
        elif star_choice in constellations:
            st.markdown(constellations[star_choice]["svg"], unsafe_allow_html=True)

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
