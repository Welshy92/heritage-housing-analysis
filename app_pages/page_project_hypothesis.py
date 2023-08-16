import streamlit as st


def project_hypothesis_body():

    st.write("## Project Hypothesis & Validation")

    # Some basic inormation on the dataset used
    st.success(
        f"* We suspect the size of the house is a big factor in it's "
        f"sale price. - Correct. \n"
        f"* We suspect that the newer houses are more expensive. - Correct \n"
        f"* We suspect that a higher quality house will increase the price."
        f" - Correct. \n \n"

        f"The correlation study at House Price Study supports all "
        f"of this. This insight can be used by the client to make "
        f"a few actionable changes that will maximise the sale price."
    )
