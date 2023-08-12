import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts first
from app_pages.page_summary import page_summary_body
from app_pages.house_price_study import house_price_study_body
# from app_pages.page_project_hypothesis import page_project_hypothesis_body


app = MultiPage(app_name="Heritage")  # Creates an instance of the app

# Adding app pages
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Price Correlation study", house_price_study_body)

app.run()  # Run the  app
