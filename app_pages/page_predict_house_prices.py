import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.regression_evaluation import (
    regression_performance, regression_evaluation, regression_plots
)


def predict_house_price_body():

    # load pipeline files.
    version = 'v1'
    best_regressor_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_sale_price/" +
        f"{version}/best_regressor_pipeline.pkl"
    )
    sale_price_importance = plt.imread(
        "outputs/ml_pipeline/predict_sale_price/" +
        f"{version}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    st.write("### ML: Predicting House Prices")
    # display pipeline conclusions.
    st.info(
        f"* The ML pipeline was developed to accurately predict the sale price"
        f"of houses. \n"
        f"* We aimed to achieve an R2 score of at least **0.75** on both "
        f"the train set and test set to ensure accuracy in the predictions. \n"
        f"* We evaluated four models and found that the "
        f"**ExtraTreesRegressor** showed the most consistent performance."
        f" It achieved an **R2 score** of **0.822** on the train set and "
        f"**0.762** on the test set. \n"
        f"* Based on this, we refined the pipeline and trained it on "
        f"the best features, ensuring accurate and reliable predictions of "
        f"house sale prices."
    )
    st.write("---")

    # Show pipelines.
    st.write("* **ML pipeline to predict house sale price**")
    st.write(best_regressor_pipeline)
    st.write("---")

    # Show best features.
    st.write("* **The features that the model was trained and their importance:**")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # Evaluate the performance on train and test sets.
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=best_regressor_pipeline)
    st.write("---")

    # Plot predicted versus actual sale price for train and test sets.
    st.write("**Regression Evaluation plots:**")
    st.write(
        f"* Comparing Predicted and Actual Sale Prices on Train & Test Sets:"
        f"\n \n(*Please note that the plots can take time to load*)"
    )
    regression_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test,
                                pipeline=best_regressor_pipeline,
                                alpha_scatter=0.5)

    st.write(
        f"* The blue dots represent the actual prices, while the horizontal"
        f" position of each dot represents the corresponding predicted "
        f"prices from the ML pipeline. "
        f"The red line represents perfect alignment, where the predicted"
        f" and actual prices are equal. \n"
        f"* Upon analyzing the plot, the evidence shows that the majority of "
        f"the blue dots closely align with the red line. This indicates "
        f"that the ML pipeline's predictions closely match the actual "
        f"values, demonstrating a strong correlation between the predicted"
        f" and actual sale prices. This suggests that the ML pipeline is"
        f" performing well in accurately predicting the sale prices of houses."
    )
