import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Code copied from Modeling and Evaluation - Predict Sale Price notebook,
# Evaluate on Train and Test Sets section


# Evaluate the performance of a regression model on train and test sets
def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.write("**Model Evaluation**")
    st.write("* **Train Set**")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("* **Test Set**")
    regression_evaluation(X_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write(
        'R2 Score:', r2_score(y, prediction).round(3))
    st.write(
        'Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
    st.write(
        'Mean Squared Error:', mean_squared_error(y, prediction).round(3))
    st.write(
        'Root Mean Squared Error:', np.sqrt(
            mean_squared_error(y, prediction)).round(3))
    st.write("\n")


# Plot evaluation of regression model
def regression_plots(X_train, y_train, X_test, y_test, pipeline,
                                alpha_scatter=0.5):

    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    sns.scatterplot(x=y_train.values.ravel(), y=pred_train,
                    alpha=alpha_scatter, ax=axes[0])
    sns.lineplot(x=y_train.values.ravel(),
                 y=y_train.values.ravel(), color='red', ax=axes[0])
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predictions")
    axes[0].set_title("Train Set")

    sns.scatterplot(x=y_test.values.ravel(), y=pred_test,
                    alpha=alpha_scatter, ax=axes[1])
    sns.lineplot(x=y_test.values.ravel(),
                 y=y_test.values.ravel(), color='red', ax=axes[1])
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predictions")
    axes[1].set_title("Test Set")

    st.pyplot(fig)
