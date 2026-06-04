import os
import streamlit as st
import requests

st.set_page_config(page_title="Gezi Rehberi", page_icon="🌍")

st.title("🌍 Gezi Rehberi")

STRAPI_URL = os.getenv("STRAPI_URL", "http://localhost:1337")

cities_response = requests.get(f"{STRAPI_URL}/api/cities")
cities = cities_response.json()["data"]

city_names = [city["name"] for city in cities]

selected_city = st.selectbox("Şehir Seç", city_names)
st.subheader(f"{selected_city} Mekanları")

places_response = requests.get(f"{STRAPI_URL}/api/places?populate=*")
places = places_response.json()["data"]

filtered_places = []

for place in places:
    if place["city"] and place["city"]["name"] == selected_city:
        filtered_places.append(place)

if len(filtered_places) == 0:
    st.warning("Bu şehir için mekan bulunamadı.")
else:
    for place in filtered_places:
        st.markdown(f"### 📍 {place['name']}")

        if place["cover_image"]:
            image_url = STRAPI_URL + place["cover_image"]["url"]
            st.image(image_url, width=350)

        st.write(place["description"])
        st.write(f"⭐ Puan: {place['rating']}/5")
        st.divider()