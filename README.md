# **Heritage Housing Analysis**

![Responsiveness image](/media/images/responsive.png)
Image generated using [Am I Responsive web app](https://ui.dev/amiresponsive)

[Github repository](https://github.com/Welshy92/heritage-housing-analysis)

[Live deployed project](https://heritagehousing-a55973708c5f.herokuapp.com/)

## **Contents**

- [Overview](#overview)
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and how to validate](#hypothesis-and-how-to-validate)
- [User Stories](#user-stories)
- [Rationale to map the business requirements to the Data Visualisations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design (Streamlit Dashboard)](#dashboard-design-streamlit-dashboard)
- [Deployment](#deployment)
- [Unfixed Bugs](#unfixed-bugs)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Other Technologies Used](#other-technologies-used)
- [Credits](#credits)
- [Potential future improvements/ lessons learned](#potential-future-improvements-lessons-learned)
- [Acknowledgements](#acknowledgements)

## Overview

I have been requested by a good friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for their inherited properties.

Although my friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

| Variable      | Meaning                                                                 | Units                                                                                                                                                                   |
| :------------ | :---------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1stFlrSF      | First Floor square feet                                                 | 334 - 4692                                                                                                                                                              |
| 2ndFlrSF      | Second-floor square feet                                                 | 0 - 2065                                                                                                                                                                |
| BedroomAbvGr  | Bedrooms above grade (does NOT include basement bedrooms)               | 0 - 8                                                                                                                                                                   |
| BsmtExposure  | Refers to walkout or garden level walls                                 | Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement                                                                       |
| BsmtFinType1  | Rating of basement finished area                                        | GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement |
| BsmtFinSF1    | Type 1 finished square feet                                             | 0 - 5644                                                                                                                                                                |
| BsmtUnfSF     | Unfinished square feet of basement area                                 | 0 - 2336                                                                                                                                                                |
| TotalBsmtSF   | Total square feet of basement area                                      | 0 - 6110                                                                                                                                                                |
| GarageArea    | Size of garage in square feet                                           | 0 - 1418                                                                                                                                                                |
| GarageFinish  | Interior finish of the garage                                           | Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage                                                                                                    |
| GarageYrBlt   | Year garage was built                                                   | 1900 - 2010                                                                                                                                                             |
| GrLivArea     | Above grade (ground) living area square feet                            | 334 - 5642                                                                                                                                                              |
| KitchenQual   | Kitchen quality                                                         | Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor                                                                                                        |
| LotArea       | Lot size in square feet                                                 | 1300 - 215245                                                                                                                                                           |
| LotFrontage   | Linear feet of street connected to property                             | 21 - 313                                                                                                                                                                |
| MasVnrArea    | Masonry veneer area in square feet                                      | 0 - 1600                                                                                                                                                                |
| EnclosedPorch | Enclosed porch area in square feet                                      | 0 - 286                                                                                                                                                                 |
| OpenPorchSF   | Open porch area in square feet                                          | 0 - 547                                                                                                                                                                 |
| OverallCond   | Rates the overall condition of the house                                | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor                                 |
| OverallQual   | Rates the overall material and finish of the house                      | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor                                 |
| WoodDeckSF    | Wood deck area in square feet                                           | 0 - 736                                                                                                                                                                 |
| YearBuilt     | Original construction date                                              | 1872 - 2010                                                                                                                                                             |
| YearRemodAdd  | Remodel date (same as construction date if no remodelling or additions) | 1950 - 2010                                                                                                                                                             |
| SalePrice     | Sale Price                                                              | 34900 - 755000                                                                                                                                                          |

## Business Requirements

- 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
- 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.
- An acceptable accuracy has been agreed upon for number 2, we have set a target of making sure the R2 score is above 0.75 on both train and test sets and try to ensure the model is not too under or over fitted.

## Hypothesis and how to validate

We know that we can use conventional data analysis to answer business requirement 1. We will conduct a correlation study for the following hypothesis:

- 1 - We suspect that larger houses will be more expensive.
- 2 - We expect newer houses to be more expensive.
- 3 - We expect that a house in good condition will increase in price.

We found all of these to be correct after completing a correlation study. More details can be found within the live app.

## User Stories

Information Gathering and Data Collection:

- As a Data Practitioner, I want to download the public dataset on house prices in Ames, Iowa, so that I can gather the necessary data for analysis.

    **How?** This will be done by obtaining the data from Kaggle using an API key.

- As a Data Practitioner, I want to gather information on the client's four inherited houses, so that I can analyse it.

    **How?** Collect relevant details and attributes of the client's four inherited houses, including features.

Data Visualization, Cleaning, and Preparation:

- As a Data Practitioner, I want to visualise the correlated variables against the sale price to identify relationships and gain some potential insight.

    **How?** Create scatter plots or heatmaps, to visualise the correlation between each variable and the sale price.

- As a Data Practitioner, I want to clean and preprocess the data to ensure its quality and suitability for analysis.

    **How?** Apply data cleaning techniques to handle missing values, outliers or other inconsistent things in the dataset, ensuring the data is accurate and ready for analysis.

- As a Data Practitioner, I want to identify the most correlated variables with the sale price so that I can focus my predictions on the most important variables.

    **How?** Calculate and analyse the correlation coefficients between each variable and the sale price, identifying the variables with the highest correlation values.

Model Training, Optimization, and Validation:

- As a Data Practitioner, I want to train, optimise, and validate a regression model using the collected data to predict house sale prices accurately.

    **How?** Use the cleaned and preprocessed data to train a regression model, optimise its hyperparameters, and evaluate its performance using appropriate metrics.

Dashboard Planning, Designing, and Development:

- As a user, I want to have access to an intuitive and user-friendly dashboard, so that I can easily explore the data, visualise predictions, and gain insights.

    **How?** The dashboard will be designed using Streamlit to ensure a clean and organised layout, intuitive navigation, and user-friendly interactions.

- As a user, I want the dashboard to incorporate interactive visualisations and predictive capabilities, allowing me to interact with the data and receive accurate predictions.

    **How?** A Streamlit dashboard will be used, allowing for interactive visualisations and seamless interaction with the data.

Dashboard Deployment and Release:

- As a user, I expect the dashboard to be deployed to a production environment, making it easily accessible for me and other users.

        How: The dashboard will be deployed to the hosting platform Heroku for convenient access through a web browser.

- As a user, I want the dashboard to undergo thorough testing and quality assurance to ensure its functionality and performance.

        How: The dashboard will be rigorously tested for functionality, responsiveness, and compatibility across different devices and browsers.

- As a Data Practitioner, I want to release the dashboard to the client and provide necessary documentation for its usage and maintenance.

        How: Provide the client with the deployed dashboard, along with clear documentation outlining its usage instructions, features, and any necessary maintenance tasks.

## Rationale to map the business requirements to the Data Visualisations and ML tasks

- ### Business Requirement 1: Correlation Study and Data Visualization

  The client's objective is to gain insights into the biggest factors of a sale price.

  - Review and Inspect Dataset: In order to gain an understanding of the dataset related to the houses, a thorough inspection and review of the collection data will occur.
  - Correlation Study: To understand how different variables relate to the "SalePrice" of houses, both Pearson and Spearman correlation coefficients will be calculated.
  - Select Most Correlated Variables: Based on the correlation study results, the highest correlated variables with the "SalePrice" will be identified. These variables will be the priority for further analysis.
  - Data Visualization: various visualisation methods such as scatter plots, heatmaps, and regression plots will be used to to represent the correlations between each variable and the "SalePrice."
  - Hypothesis Validation: Findings from the correlation study and data visualisations will be used to validate hypothesis about how strong of an effect some factors can have on the sale price of houses.

- ### Business Requirement 2: Predict House Prices

  The client's objective is to accurately predict house prices in Ames, Iowa.

  - Data Cleaning and Feature Engineering: To prepare the data for the machine learning model, the data will be cleaned and feature engineering will be used.
  - Regression Model Development: A regression model will be constructed using the best algorithm (ExtraTreesRegression) to predict the sale price of houses.
  - Hyperparameter Tuning: To optimise the performance of the regression model, hyperparameters will be adjusted.
  - Regression Evaluation: The trained model will be evaluated using appropriate evaluation metrics such as R2 score and Mean Absolute Error.
  - Predict house prices: Once the model is trained and evaluated, it will then be utilised to predict the prices of four inherited houses, as well as other houses in Ames, Iowa.

## ML Business Case

- Business Requirements:

  - Visualisations: Provide data visualisations showing the correlation between house attributes and sale prices.
  - Sale Price Prediction: Allow the prediction of sale prices for the client's inherited houses and any other houses in Ames, Iowa.

- Conventional Data Analysis:

  - Conventional data analysis will be used to study the correlation between house attributes and sale prices.

- Dashboard Requirement:

  - The client requires a dashboard to present the project outcomes. Streamlit will be used.

- Project Outcome:

  - The client considers the project successful if it achieves the following:

    - Relevant Variables: Identify and present the most relevant variables correlated with the sale price.
    - Sale Price Prediction: Develop a model capable of predicting the sale price for the client's four inherited houses and any other houses in Ames, Iowa.

- Ethical or Privacy Concerns:

  - No ethical or privacy concerns have been identified since the client has obtained the dataset from a public source.

- Model Selection:

  - Based on the available data, a regressor model will be used to predict the sale price. The regressor will take some of the house attributes information as inputs and generate the predicted sale price as the output.

- Performance Goal:

  - To hit the client's expectations, a target R2 score of at least 0.75 on both train and test sets must be met.

- Client Benefits:

  - By understanding the most relevant variables correlated with sale price, the client can make informed decisions to maximise the sale prices of the inherited properties.

## Dashboard Design (Streamlit Dashboard)

- Page 1:

  - Quick project summary.
  - Project Terms & Jargon.
  - Describe Project Dataset.
  - State Business Requirements.

![Summary Page Design](/media/images/SummaryPage.png)

- Page 2:

  - Project Hypothesis & Validation.
  - Success or failure?
  - How I came to the answer.

![Hypothesis Page Design](/media/images/HypothesisPage.png)

- Page 3:

  - Sale Price Study.
  - Show 1st business requirement.
  - Tickbox to show a preview of the dataset.
  - Explain correlation study and its conclusions.
  - Tickbox to show regression plots.
  - Tickbox to show correlation matrix.

![Correlation Page Design 1](/media/images/CorrelationPage1.png)

![Correlation Page Design 2](/media/images/CorrelationPage2.png)

![Correlation Page Design 3](/media/images/CorrelationPage3.png)

![Correlation Page Design 4](/media/images/CorrelationPage4.png)

- Page 4:

  - House Price Predictor.
  - User input of variables.
  - Displays a predicted price based on variables.

![Predict Page Design 1](/media/images/PredictPage1.png)

![Predict Page Design 2](/media/images/PredictPage2.png)

- Page 5:

  - ML: Predict House Prices.
  - Features that the model trained and importance.
  - Pipeline performance.

![ML Page Design 1](/media/images/MLPage1.png)

![ML Page Design 2](/media/images/MLPage2.png)

![ML Page Design 3](/media/images/MLPage3.png)

## Deployment

### Heroku

- The App live link is: [LIVE HERE!](<https://heritagehousing-a55973708c5f.herokuapp.com/>)
- I have Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps:

1. Login to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Typed in my heritage "heritage-housing-analysis" repository name and clicked Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. Once the deployment has succeeded, click the button "Open App" on the top of the page to see the live deployment.

## Unfixed Bugs

There are no remaining bugs left in the project. A few bugs cropped up over development, mainly due to inconsistant class names or general typing errors.

## Main Data Analysis and Machine Learning Libraries

- numPy - Used for my correlation studies to help produce things such as heatmaps.
- Pandas - Used to convert the raw data in data frames, as well as performing many operations on it.
- Plotly & matplotlib - Used to help visualise my studies into various plots for easier reading and analysis.
- SciKit Learn - Used for creating pipelines and feature selection.
- Seaborn - Used in my data analysis correlation studies.
- Feature-engine - Used to perform data engineering tasks

## Other Technologies Used

- Streamlit - Used to quickly create a webpage to display all of my results of my data analysis and machine learning.
- CodeAnywhere - Cloud based IDE used to code the project.
- Jupyter - Notebooks used in my data analysis and machine learning coding.
- Git - Source control.
- Heroku - Used to host my streamlit app.

### Credits

- Code Institute - Provided learning content and used some custom functions from the walkthrough projects.
- All library providers for their very detailed and easy to understand documentations.

### External Code

- Custom functions used for data cleaning, feature engineering and correlation + PPS analysis from Churnometer walkthrough project by Code Institute, as well as adapting some of the code they used to make my predictive_analysis_ui.py file.

## Potential future improvements/ lessons learned

- Perhaps don't drop features at a stage as early as the first notebook.
- Maybe test an alternative method to fill in the missing data points and see if that improves ML pipeline performances. However my pipeline was within acceptable parameters.

## Acknowledgements

- Nicola Hodby - My rock that has kept me motivated through the highs and lows.
- Travis Perkins - My employers who were very supportive in making sure I had the time to do this project.
