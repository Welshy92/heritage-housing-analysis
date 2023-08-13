import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    # Some basic inormation on the dataset used
    st.info(
        f"#### Jargon & Project Terms \n \n"
        f"* SalePrice - The Price that the property sold for. \n"
        f"* 1stFlrSF - First floor in square feet. \n"
        f"* GarageArea - Size of garage in square feet. \n"
        f"* GrLivArea - Above grade (ground) living area in square feet \n"
        f"* OverallQual - Rates the overall material and finish of the house"
        f" out of 10. 1 being very poor and 10 being very good. \n"
        f"* TotalBsmtSF - Basement area in square feet. \n"
        f"* YearBuilt - Original contruction date. \n \n"
        f"#### Project Dataset \n \n"
        f"The dataset is sourced from [Kaggle]"
        f"(https://www.kaggle.com/codeinstitute/housing-prices-data).\n"
        f"The dataset has almost 1.5 thousand rows and represents housing "
        f"records from Ames, Iowa, indicating house profile"
        f"(Floor Area, Basement, Garage, Kitchen, Lot, "
        f"Porch, Wood Deck, Year Built) and its respective"
        f" sale price for houses built between 1872 and 2010.")

    # Link to README file for users to view the full documentation.
    st.warning(
        f"* For additional information, please read the [Project README file]"
        f"(https://github.com/Welshy92/heritage-housing-analysis/blob/main/README.md).")

    # Business requirements (Copied from the README)
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the "
        f"house attributes correlate with the sale price."
        f" Therefore, the client expects data visualisations of the"
        f" correlated variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale "
        f"price from her four inherited houses and any other "
        f"house in Ames, Iowa."
    )
