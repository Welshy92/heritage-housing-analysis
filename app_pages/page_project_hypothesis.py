import streamlit as st


def project_hypothesis_body():

    st.write("## Project Hypothesis & Validation")

    # Some basic inormation on the dataset used
    st.success(
        f"* We suspect the size of the house is a big factor in it's "
        f"sale price. - **Correct**. \n \n"
        f"Both Pearson and Spearman correlation methods reveal a strong"
        f"positive correlation between the overall quality of the house"
        f"(OverallQual) and its sale price. This suggests that houses with"
        f"higher quality ratings tend to sell for more. \n"

        f"* We suspect that the newer a house is, the more expensive "
        f"they end up being. - **Correct** \n \n"
        f"The year of construction(YearBuilt) shows a moderate positive "
        f"correlation with the sale price. Pearson correlation "
        f"coefficient suggests that newer houses usually en up "
        f"having higher prices. \n"

        f"* We suspect that a higher quality house will increase the price."
        f" - **Correct**. \n \n"
        f"Multiple variables, such as ground living area(GrLivArea), garage "
        f"area(GarageArea), total basement square footage(TotalBsmtSF), and "
        f"first floor square footage(1stFlrSF) exhibit strong positive "
        f"correlations with the sale price. The Pearson correlation "
        f"coefficients for these variables are quite high, showing that "
        f"larger houses usually end up having a higher sale price.\n \n"
    )

    st.info(
        f"The House Price Correlation Study supports all of the above. "
        f"We see that a new, big and well built house would most likely "
        f"fetch the highest price on the housing market. This insight can "
        f"be used by the client to potentially help make a few decisions "
        f"that could maximise the sale price of a house in Iowa."
    )
