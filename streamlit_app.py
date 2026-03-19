import streamlit as st
import random

# -------------------
# IMAGE PATHS
# -------------------

STAR_IMAGES = {
    "Altair": "images/altair.png",
    "Vega": "images/vega.png"
}

CONSTELLATION_IMAGES = {
    "Ursa Major": "images/ursa_major.png",
    "Orion": "images/orion.png"
}

# -------------------
# DATA
# -------------------

stars = {
    "Altair": {
        "short_desc": "Bright star in Aquila",
        "info": "Altair is part of the Summer Triangle and is one of the closest bright stars to Earth.",
        "sky_position": "Northern sky during summer evenings",
        "features": "Forms the Summer Triangle with Vega and Deneb."
    },
    "Vega": {
        "short_desc": "Very bright star in Lyra",
        "info": "Vega is one of the brightest stars visible from Earth.",
        "sky_position": "High in the northern summer sky",
        "features": "Part of the Summer Triangle."
    }
}

constellations = {
    "Ursa Major": {
        "short_desc": "Large northern constellation with the Big Dipper.",
        "info": "Ursa Major contains stars useful for locating Polaris.",
    },
    "Orion": {
        "short_desc": "Famous hunter constellation.",
        "info": "Orion contains a straight line of three stars known as Orion’s Belt.",
    }
}

# -------------------
# PAGE CONFIG + STYLES
# -------------------

st.set_page_config(page_title="⭐ Star Navigator", layout="wide")

glassy_style = """
<style>
body {
    background-color: #070f2b;
    color: white;
}

.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 22px;
    margin-top: 15px;
    border: 1px solid rgba(255,255,255,0.15);
}

.glass-title {
    font-size: 26px;
    font-weight: bold;
    color: #9290c3;
}

</style>
"""

st.markdown(glassy_style, unsafe_allow_html=True)

# -------------------
# TITLE
# -------------------
st.markdown("<div class='glass-card'><span class='glass-title'>✨ Constellation Star Navigator ✨</span></div>", unsafe_allow_html=True)

# -------------------
# TWO-COLUMN LAYOUT
# -------------------

col_left, col_right = st.columns([1.3, 1])

with col_right:

    option = st.selectbox("Choose what you see:", ["-- Select --", "Star", "Constellation"])
    
    selection = None

    if option == "Star":
        selection = st.selectbox("Choose a Star:", ["Altair", "Vega"])
    
    elif option == "Constellation":
        selection = st.selectbox("Choose a Constellation:", ["Ursa Major", "Orion"])
    
    if selection:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write(f"### {selection}")

        if option == "Star":
            data = stars[selection]
            st.write(f"**Description:** {data['short_desc']}")
            st.write(f"**Sky Position:** {data['sky_position']}")
            st.write(f"**Features:** {data['features']}")
            st.write(f"**Info:** {data['info']}")
        
        else:  # constellation
            data = constellations[selection]
            st.write(f"**Description:** {data['short_desc']}")
            st.write(f"**Info:** {data['info']}")

        st.markdown("</div>", unsafe_allow_html=True)


with col_left:

    if selection:
        if option == "Star" and selection in STAR_IMAGES:
            st.image(STAR_IMAGES[selection], use_column_width=True)

        elif option == "Constellation" and selection in CONSTELLATION_IMAGES:
            st.image(CONSTELLATION_IMAGES[selection], use_column_width=True)

    else:
        st.markdown("<div class='glass-card'><center><em>Select a star or constellation 👈</em></center></div>", unsafe_allow_html=True)
