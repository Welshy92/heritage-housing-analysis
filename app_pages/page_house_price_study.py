import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def house_price_study_body():

    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("## Sale Price Study")
    st.info(
        f"* The client is interested in understanding the patterns"
        f" between a houses attributes and it's sale price ")

    # inspect data
    if st.checkbox("Inspect Sales list"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to the sale price. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "HousePriceStudy" notebook - "Conclusions and Next steps"
    st.info(
        f"The correlation indications and plots below interpretation "
        f"converge. It is indicated that: \n"
        f"*1stFlrSF, GarageArea, GrLivArea, OverallQual, TotalBsmtSF and "
        f"YearBuilt are the variables with the strongest correlation "
        f"to the SalePrice."
        f"* All of the 6 chosen variables have a positive effect "
        f"on the SalePrice \n"
        f"* YearBuilt was the least important of the 6. \n"
        f"* TotalBsmtSF was just about the most important of the 6. \n"
        f"* Other than year built, the other factors are all pretty"
        f" important to increasing the SalePrice. \n"
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Code copied from "HousePriceStudy" notebook - "EDA on selected variables"
    if st.checkbox("Inspect Correlation Study"):

        target_var = 'SalePrice'

        # Plots to show the effect on Sale Price each variable has.S
        def plot_regress(df, col, target_var):
            fig, axes = plt.subplots(figsize=(12, 5))
            sns.regplot(data=df, x=col, y=target_var,
                        line_kws={"color": "red"})
            plt.title(f"{col}", fontsize=20, y=1.05)
            st.pyplot(fig)

        for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_regress(df_eda, col, target_var)

    # Plotting Heatmap
    if st.checkbox("Show Correlation Heatmap"):
        plot_heatmap(df_eda, vars_to_study)

    st.success(
        f"**Finding:**\n\n"
        f"Based on correlation and plot analysis, the following observations"
        f" have been made. They address the first business question about the"
        f"  correlation between house features and Sale Price:\n"
        f"* The *Sale Price* of a house tends to be higher for properties"
        f" with certain features. \n"
        f"* *Overall Quality* of the house has the strongest "
        f"correlation with Sale Price, showing us that houses with higher "
        f"quality usually sell for a higher price. \n"
        f"* Variables such as *Above Ground Living Area*, *Garage Area*, "
        f"*Total Basement Square Footage*, and *First Floor Square "
        f"Footage* also show strong positive correlations with"
        f" *Sale Price.* \n"
        f"* Other variables, such as *Year Built*, exhibit moderate "
        f"positive correlations with *Sale Price*."
    )


def plot_heatmap(df_eda, relevant_variables):

    # Create a new DataFrame with the selected variables
    heatmap_vars = df_eda.copy()

    # Calculate the correlation matrix
    correlation_matrix = heatmap_vars.corr()

    # Plot the heat map
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title("Correlation Matrix", fontsize=20)
    st.pyplot(fig)
