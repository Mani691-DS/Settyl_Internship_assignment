# app.py
import streamlit as st
import pandas as pd
from model import collaborative_filtering, content_based_filtering

# Load data
users = pd.read_csv('users.csv')
products = pd.read_csv('products.csv')
purchases = pd.read_csv('purchases.csv')
browsing_history = pd.read_csv('browsing_history.csv')

# Streamlit application
st.title("Product Recommendation System")

# User input section
user_id = st.number_input("Enter User ID:", min_value=1, step=1,max_value=5)
algorithm = st.selectbox("Select Recommendation Algorithm:", 
                          options=["Collaborative Filtering", "Content-Based Filtering", "Hybrid"])

if st.button("Get Recommendations"):
    # Retrieve all purchased and browsed product IDs
    purchased_product_ids = purchases[purchases['user_id'] == user_id]['product_id'].unique()
    browsed_product_ids = browsing_history[browsing_history['user_id'] == user_id]['product_id'].unique()

    # Products the user has already interacted with
    interacted_products = products[products['product_id'].isin(purchased_product_ids) | 
                                   products['product_id'].isin(browsed_product_ids)]

    # Generate recommendations based on selected algorithm
    if algorithm == "Collaborative Filtering":
        recommendations = collaborative_filtering(user_id, purchases, browsing_history, products)
    elif algorithm == "Content-Based Filtering":
        recommendations = content_based_filtering(user_id, purchases, browsing_history, products)
    elif algorithm == "Hybrid":
        collaborative_recommendations = collaborative_filtering(user_id, purchases, browsing_history, products)
        content_based_recommendations = content_based_filtering(user_id, purchases, browsing_history, products)
        recommendations = pd.concat([collaborative_recommendations, content_based_recommendations]).drop_duplicates()

    # Exclude already interacted products from recommendations
    recommended_products = recommendations[~recommendations['product_id'].isin(purchased_product_ids) & 
                                           ~recommendations['product_id'].isin(browsed_product_ids)]

    # Prepare the data for output
    interacted_products_display = interacted_products[['product_id', 'product_name', 'price', 'rating']].copy()
    interacted_products_display['source'] = interacted_products_display['product_id'].apply(
        lambda x: 'Purchased' if x in purchased_product_ids else 'Browsed'
    )

    recommended_products_display = recommended_products[['product_id', 'product_name', 'price', 'rating']].copy()
    recommended_products_display['source'] = 'Recommended'

    # Show results
    st.subheader("Interacted Products")
    st.write(interacted_products_display)

    st.subheader("Recommended Products")
    st.write(recommended_products_display)

