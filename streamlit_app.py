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
        "ascii":"""
        *
       ***
      *****
       ***
        *
""",
        "map":"""
        *      *
           *
             X <--- Altair
               *
            *
        *         *
""",
        "direction":"""
        *      *
           *
             X ----> West
               *         |
            *            |
        *         *      v South

Altair rises in the East and sets in the West.
Follow its movement to estimate western direction.
"""
    },
    "vega":{
        "name":"Vega",
        "short_desc":"Very bright star in Lyra",
        "info":"Vega is one of the brightest stars visible from Earth.",
        "sky_position":"High in the northern summer sky",
        "features":"Part of the Summer Triangle.",
        "ascii":"""
      *
     ***
    *****
     ***
      *
""",
        "map":"""
       *
      * *
     * X *
      * *
       *
""",
        "direction":"""
       *
      * *
     * X * ----> Zenith
      * *
       *

Vega often appears high overhead during summer.
Use its height to estimate overhead direction.
"""
    }
}

# --------------------------------------------------
# CONSTELLATION DATABASE
# --------------------------------------------------

constellations = {
    "ursa_major":{
        "name":"Ursa Major",
        "short_desc":"Large northern constellation containing the Big Dipper.",
        "info":"Ursa Major contains the Big Dipper which helps locate Polaris.",
        "ascii":"""
          *
             *
               *
                 *
              *
        *            *
""",
        "stars_map":"""
        * Dubhe
           *
             *
               *
            *
        *         *
""",
        "direction":"""
        *      *
           *
             X ----> Polaris (North)
               *          |
            *             |
        *         *       v South

Follow the two outer stars of the Big Dipper upward
to locate Polaris which indicates true north.
"""
    },
    "orion":{
        "name":"Orion",
        "short_desc":"Famous hunter constellation.",
        "info":"Orion contains Orion's Belt which forms a straight line of three stars.",
        "ascii":"""
          *       *
             * * *
          *   *   *
             * * *
          *       *
""",
        "stars_map":"""
        * Betelgeuse
           *
         * * *   <--- Orion's Belt
           *
        * Rigel
""",
        "direction":"""
           * *
         * X X X ---> East
           *
        *         *
            |
            v West

Orion's Belt rises in the East and sets in the West.
"""
    }
}

# --------------------------------------------------
# STREAMLIT APP
# --------------------------------------------------

st.title("⭐ Star Charter Navigation Tool ⭐")

st.write("### What do you know about your location?")

mode = st.radio(
    "Select Mode",
    ("Exact coordinates", "Environmental description", "No idea")
)

def show_star_details(key):
    star = stars[key]
    st.subheader(f"Star: {star['name']}")
    st.write(f"**Description:** {star['short_desc']}")
    st.text(star["ascii"])
    st.write(f"**Additional Info:** {star['info']}")
    st.write(f"**Sky Position:** {star['sky_position']}")
    st.write(f"**Features:** {star['features']}")
    st.text(star["map"])
    st.text(star["direction"])

def show_constellation_details(key):
    const = constellations[key]
    st.subheader(f"Constellation: {const['name']}")
    st.write(f"**Description:** {const['short_desc']}")
    st.text(const["ascii"])
    st.write(f"**Info:** {const['info']}")
    st.text(const["stars_map"])
    st.text(const["direction"])

if mode == "Exact coordinates":
    lat = st.number_input("Enter Latitude:", value=0.0)
    lon = st.number_input("Enter Longitude:", value=0.0)
    
    visibility = st.selectbox(
        "Sky Visibility",
        ["Clear", "Partial", "Low", "Obstructed"]
    )
    
    if visibility == "Clear":
        view_choice = st.radio("What do you see?", ("A single star", "Multiple stars / constellation"))
        
        if view_choice == "A single star":
            star_choice = st.selectbox("Choose Star", list(stars.keys()))
            show_star_details(star_choice)
        else:
            const_choice = st.selectbox("Choose Constellation", list(constellations.keys()))
            show_constellation_details(const_choice)
    else:
        st.warning("Sky visibility is limited. Cannot provide precise details.")

elif mode == "Environmental description":
    sea_color = st.text_input("Sea color (blue/green/turquoise):")
    sea_life = st.text_input("Sea life observed (fish/birds/whales):")
    wind_dir = st.text_input("Wind direction (north/south/east/west):")
    
    st.info("Analyzing environment...")
    random_const = random.choice(list(constellations.keys()))
    show_constellation_details(random_const)

elif mode == "No idea":
    sky_visible = st.radio("Can you see the sky and stars?", ("Yes", "No"))
    if sky_visible == "Yes":
        const_choice = st.selectbox("Choose Constellation", list(constellations.keys()))
        show_constellation_details(const_choice)
    else:
        land_visible = st.radio("Can you see land or landmarks?", ("Yes", "No"))
        if land_visible == "Yes":
            mountain = st.radio("Do you see mountains?", ("Yes", "No"))
            coast = st.radio("Do you see a coastline?", ("Yes", "No"))
            random_const = random.choice(list(constellations.keys()))
            show_constellation_details(random_const)
        else:
            clue = st.text_input("Provide any useful clue:")
            random_star = random.choice(list(stars.keys()))
            show_star_details(random_star)
