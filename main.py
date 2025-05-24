import streamlit as st
from  langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", (
    "Indian", "American",
    "Mexican", "Italian", "Arabic"
))

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    restaurant_name = response['restaurant_name'].strip().strip('"')
    raw_items = response['menu_items']

    # Keep only part after colon (if model adds intro text)
    menu_only = raw_items.split(":")[-1]

    # Remove extra statements like "Let me know..."
    cleaned = menu_only.split("Let me")[0]

    # Split into list
    menu_items = [item.strip() for item in cleaned.split(",") if item.strip()]

    # ✅ Display
    st.header(restaurant_name)
    st.subheader("Menu Items")
    for item in menu_items:
        st.markdown(f"- {item}")


