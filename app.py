import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts first
from app_pages.page_summary import page_summary_body
from app_pages.page_house_price_study import house_price_study_body
from app_pages.page_project_hypothesis import project_hypothesis_body
from app_pages.page_house_price import house_price_body
from app_pages.page_predict_house_prices import predict_house_price_body


# Creates an instance of the app
app = MultiPage(app_name="Heritage Housing Analysis")

# Adding app pages
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis & Validation", project_hypothesis_body)
app.add_page("House Price Correlation study", house_price_study_body)
app.add_page("House Price Predictor", house_price_body)
app.add_page("ML: Predict House Prices", predict_house_price_body)

app.run()  # Run the  app
