import streamlit as st


def predict_house_price_body():

    st.write("## ML Pipeline: Predcting House Prices")

    st.info(
        f"* The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa."
    )
    st.write("---")

    # ML Pipeline
    st.write("---")

    # Training + importance
    st.write("The features the model has trained and their importance.")

    st.write("---")

    # Pipeline Performance
    st.write("### Pipeline Performance")

    # Train Set
    st.info("#### Train Set")

    st.write("#### Confusion Matrix")

    st.write("#### Classification Report")

    # Test Set
    st.info("#### Test Set")

    st.write("#### Confusion Matrix")

    st.write("#### Classification Report")
