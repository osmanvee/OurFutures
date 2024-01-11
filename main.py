import streamlit as st
import langchain_helper as lch

story_template = """
In the year 2060, person_name found himself in a transformed location_name, a city reborn under the auspices of sustainability. Towering above the skyline were skyscrapers, not of steel and glass, but of living greenery, with gardens cascading from their rooftops and walls. The air was fresher, filled with the oxygen and scents of a thousand different plants, a stark contrast to the location_name of old.

person_name, a lifelong resident, marveled at how the streets had changed. Electric vehicles glided silently along roads lined with lush trees, their leaves a vibrant testament to the city's commitment to clean air. Solar panels and wind turbines were as common as lampposts, powering homes and businesses with renewable energy.

For person_name, this new world was not just a visual delight but a lifestyle revolution. His diet was sourced from vertical farms scattered throughout the city, ensuring fresh, organic produce year-round. Rainwater harvesting and greywater recycling had become the norm, drastically reducing his water footprint.

Most strikingly, the community had evolved. Neighbors shared resources and knowledge, fostering a culture of cooperation and mutual support. person_name often spent his evenings in community gardens, cultivating both crops and friendships.

This green transformation had deeply impacted person_name's life. He had become an advocate for sustainable living, educating others about the benefits of a life harmoniously intertwined with nature. His own home was a microcosm of this new world, equipped with a small rooftop garden and a rainwater collection system.
"""


st.title("🌎 Our Futures 🌎")

user_name = st.sidebar.text_input(
  label="What is your name?",
  max_chars=30 # Change this to whatever limit you want
  )

user_age = st.sidebar.text_input(
  label="Your Age",
  max_chars=10 # Change this to whatever limit you want
  )
  
user_location = st.sidebar.selectbox("What is your Location", ("Canada - Westcoast", "Canada - Eastcoast", "South America", "USA (west)", "USA (east)", "Asia", "Europe"))


story_input = st.sidebar.text_area(
  label="Input Story",
  value=story_template,  # Set the default value
  max_chars=6000 # Change this to whatever limit you want
  )

future_year = st.sidebar.selectbox("What year do you want to jump into?", ("2040 AD",  "2050 AD", "2060 - 2070 AD", "2080 AD", "5000 AD"))

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "This is a playground to test story writing for Our Futures Project"

    # Add a button to trigger story generation
    generate_button = st.button("Generate Story")

if generate_button and story_input:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        response = lch.generate_future_story(user_name, user_age, user_location, story_input, future_year, openai_api_key)
        st.text(response['story_response'])