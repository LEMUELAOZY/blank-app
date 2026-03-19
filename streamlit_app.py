import streamlit as st
import random

# --------------------------------------------------
# STAR DATABASE
# --------------------------------------------------

stars = {
    "altair":{
        "name":"Altair",
        "short_desc":"Bright star in Aquila",
        "info":"Altair is part of the Summer Triangle and is one of the closest bright stars to Earth.",
        "sky_position":"Northern sky during summer evenings",
        "features":"Forms the Summer Triangle with Vega and Deneb.",
        "map":"Altair is located in the Summer Triangle with Vega and Deneb.",
        "direction":"Rises in the East and sets in the West."
    },
    "vega":{
        "name":"Vega",
        "short_desc":"Very bright star in Lyra",
        "info":"Vega is one of the brightest stars visible from Earth.",
        "sky_position":"High in the northern summer sky",
        "features":"Part of the Summer Triangle.",
        "map":"Vega is located in Lyra, forming the Summer Triangle with Altair and Deneb.",
        "direction":"Appears high overhead during summer; use to estimate overhead direction."
    }
}

# --------------------------------------------------
# CONSTELLATION DATABASE
# --------------------------------------------------

constellations = {
    "ursa_major":{
        "name":"Ursa Major",
        "short_desc":"Contains the Big Dipper.",
        "info":"Ursa Major contains the Big Dipper which helps locate Polaris (North Star).",
        "stars_map":"Big Dipper stars: Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid",
        "direction":"Use the two outer stars of the Big Dipper to locate Polaris (North)."
    },
    "orion":{
        "name":"Orion",
        "short_desc":"Famous hunter constellation.",
        "info":"Orion contains Orion's Belt (three stars in a straight line).",
        "stars_map":"Orion stars: Betelgeuse, Bellatrix, Alnilam, Mintaka, Rigel",
        "direction":"Orion's Belt rises in the East and sets in the West."
    }
}

# --------------------------------------------------
# STREAMLIT APP
# --------------------------------------------------

st.set_page_config(page_title="Star Navigation Tool", layout="centered")
st.title("⭐ Star Navigation Tool ⭐")
st.write("Select the information you know about your location:")

mode = st.selectbox("Choose Mode:", ["Exact coordinates", "Environmental description", "No idea"])

def show_star_details(key):
    star = stars[key]
    st.subheader(f"{star['name']} ⭐")
    st.write(f"**Description:** {star['short_desc']}")
    st.write(f"**Info:** {star['info']}")
    st.write(f"**Sky Position:** {star['sky_position']}")
    st.write(f"**Features:** {star['features']}")
    st.write(f"**Map:** {star['map']}")
    st.write(f"**Direction:** {star['direction']}")

def show_constellation_details(key):
    const = constellations[key]
    st.subheader(f"{const['name']} 🌌")
    st.write(f"**Description:** {const['short_desc']}")
    st.write(f"**Info:** {const['info']}")
    st.write(f"**Stars Map:** {const['stars_map']}")
    st.write(f"**Direction:** {const['direction']}")

# ------------------------------
# Exact Coordinates Mode
# ------------------------------

if mode == "Exact coordinates":
    lat = st.number_input("Latitude:", value=0.0, format="%.6f")
    lon = st.number_input("Longitude:", value=0.0, format="%.6f")
    
    visibility = st.selectbox("Sky Visibility:", ["Clear", "Partial", "Low", "Obstructed"])
    
    if visibility == "Clear":
        view_choice = st.selectbox("What do you see?", ["A single star", "Multiple stars / constellation"])
        
        if view_choice == "A single star":
            star_choice = st.selectbox("Select Star:", list(stars.keys()))
            show_star_details(star_choice)
        else:
            const_choice = st.selectbox("Select Constellation:", list(constellations.keys()))
            show_constellation_details(const_choice)
    else:
        st.warning("Sky visibility is limited. Cannot provide precise details.")

# ------------------------------
# Environmental Description Mode
# ------------------------------

elif mode == "Environmental description":
    sea_color = st.selectbox("Sea color:", ["Blue", "Green", "Turquoise"])
    sea_life = st.text_input("Sea life observed (fish/birds/whales):")
    wind_dir = st.selectbox("Wind direction:", ["North", "South", "East", "West"])
    
    st.info("Analyzing environment...")
    random_const = random.choice(list(constellations.keys()))
    show_constellation_details(random_const)

# ------------------------------
# No Idea Mode
# ------------------------------

elif mode == "No idea":
    sky_visible = st.selectbox("Can you see the sky and stars?", ["Yes", "No"])
    if sky_visible == "Yes":
        const_choice = st.selectbox("Select Constellation:", list(constellations.keys()))
        show_constellation_details(const_choice)
    else:
        land_visible = st.selectbox("Can you see land or landmarks?", ["Yes", "No"])
        if land_visible == "Yes":
            mountain = st.selectbox("Do you see mountains?", ["Yes", "No"])
            coast = st.selectbox("Do you see a coastline?", ["Yes", "No"])
            random_const = random.choice(list(constellations.keys()))
            show_constellation_details(random_const)
        else:
            clue = st.text_input("Provide any useful clue:")
            random_star = random.choice(list(stars.keys()))
            show_star_details(random_star)
