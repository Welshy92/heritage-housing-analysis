# Heritage Housing Analysis

[Github repo](https://github.com/Welshy92/heritage-housing-analysis)

[Live deployed project](https://heritagehousing-a55973708c5f.herokuapp.com/)

## Overview

As a good friend, I have been requested by a friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

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
- Although an acceptable accuracy has not been agreed upon for number 2, I have set myself a target of making sure the R2 score is above 0.75 on both train and test sets and try to ensure the model is not too under or over fitted.

## Hypothesis and how to validate?

we will conduct a correlation study for the following hypothesis:

- 1 - We suspect that larger houses will be more expensive.
- 2 - We expect newer houses to be more expensive.
- 3 - We expect that a house in good condition will increase in price.

## Dashboard Design (Streamlit Dashboard)

- Page 1:

  - Quick project summary.
  - Project Terms & Jargon.
  - Describe Project Dataset.
  - State Business Requirements.

- Page 2:

  - Project Hypothesis & Validation.
  - How I intended to solve them.
  - Success or failure?

- Page 3:

  - Sale Price Study.
  - Show 1st business requirement.
  - Tickbox to show a preview of dataset.
  - Explain correlation study and its conclusions.
  - Tickbox to show regression plots.
  - Tickbox to show correlation matrix.

- Page 4:

  - House Price Predictor.
  - User input of variables.
  - Displays a predicted price based on variables.

- Page 5:

  - ML: Predict House Prices.
  - Features that the model trained and importance.
  - Pipeline performance.

## Potential future improvements/ lessons learned

* Perhaps don't drop features at a stage as early as the first notebook like I did for 
* Maybe test an alterative method to fill in the missing data points and see if that improves ML pipeline performances.

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

## Main Data Analysis and Machine Learning Libraries

- numPy
- Pandas
- Plotly
- SciKit Learn
- Seaborn - Used in my data analysis correlation studies

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

- Custom functions used for data cleaning, feature engineering and correlation + PPS analysis from Churnometer walkthrough project by Code Institute, as well as adapting some of the code they used to make my predictive_analysis_ui.py and regression_evaluation.py files.

## Acknowledgements

- Nicola Hodby - My rock that has kept me motivated through the highs and lows.
- Travis Perkins - My employers who were very supportive in making sure I had the time to do this project.
