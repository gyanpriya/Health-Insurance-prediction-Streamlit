# Insurance Price Prediction Project

This project aims to predict insurance prices using various machine learning models and visualize the results using Streamlit and Tableau.

## Files and Folders

- **`visualization.ipynb`**: Jupyter notebook containing data visualization and exploratory data analysis (EDA) for the insurance dataset.
- **`streamlit_insurance.py`**: Python script that sets up a Streamlit web application for interactive insurance price prediction.
- **`rf_model.pkl`**: Pickle file containing the trained Random Forest model.
- **`gb_model.pkl`**: Pickle file containing the trained Gradient Boosting model.
- **`tableau_dashboard`**: Folder containing Tableau dashboard files and related visualizations.

## Getting Started

### Prerequisites

Ensure you have the following packages installed:

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `tableau-api-lib` (if you are interacting with Tableau's API)

## Problem Statement

Accurately predicting insurance costs can help insurance companies to price their policies more effectively and enable customers to get better insights into their insurance costs.

## Steps Taken to Solve the Problem

### 1. Exploratory Data Analysis (EDA)

- **Data Loading:** Loaded the dataset from `.csv` files in the `DATA` folder.
- **Data Cleaning:** Handled missing values, outliers, and incorrect data types.
- **Visualization:** Used various plots and charts to understand the distribution of features and their relationships with the target variable (insurance cost).

### 2. Hypothesis Testing

- **Feature Relationships:** Conducted hypothesis tests to determine the statistical significance of the relationships between features and the target variable.
- **Correlation Analysis:** Analyzed correlations to identify important features for the prediction model.

### 3. Machine Learning Modeling

- **Pre-processing:** Applied data pre-processing steps including scaling, encoding categorical variables, and feature engineering.
- **Model Training:** Trained multiple models including Linear Regression, Random Forest, and Gradient Boosting.
- **Model Evaluation:** Evaluated models using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. Selected the best model based on performance metrics.

### Target Metric and Scores

The primary target metric for this project is the Mean Absolute Error (MAE), as it provides a straightforward interpretation of the average error in the predicted insurance costs.

### 4. Deployment

- **Streamlit App:** Developed a Streamlit application (`streamlit_insurance.py`) to serve the model and provide an interface for users to input their data and get predictions.
- **Web Interface:** Streamlit provides an easy-to-use web interface for real-time predictions.
- **Model Integration:** Integrated the trained models (`rf_model.pkl` and `gb_model.pkl`) into the Streamlit app for real-time predictions.

## Why This Approach Was Chosen

The combination of EDA, hypothesis testing, and machine learning modeling ensures a comprehensive approach to solving the problem:

- **EDA:** Helps in understanding the data and uncovering patterns and relationships.
- **Hypothesis Testing:** Provides statistical validation of the relationships between features and the target variable.
- **Machine Learning Models:** Enable accurate predictions by capturing complex relationships in the data.
- **Streamlit Deployment:** Makes the solution accessible and user-friendly, allowing for real-time predictions through a web interface.
- **Tableau Dashboards:** Offer interactive and visual summaries that enhance understanding and communication of the results.

You can install these packages using pip:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn tableau-api-lib
```

## Running the Streamlit App

Navigate to the directory containing streamlit_insurance.py:

```bash
cd path/to/your/project
```

## Run the Streamlit app:

```bash
streamlit run streamlit_insurance.py
```

Open your web browser and go to the address provided by Streamlit (usually http://localhost:8501) to interact with the application.

## Using the Models

The trained models are saved as pickle files (rf_model.pkl and gb_model.pkl). These can be loaded in your Python scripts to make predictions on new data.

## Tableau Dashboard

The Tableau dashboard images are stored in the tableau_dashboard folder. Please refer to the Tableau links:

- **`Statistics Summary Dashboard`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/Stats_Dashboard/StatisticsSummaryDashboard
- **`Premium Price Analysis`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/PremiumPrice_17215660938630/PremiumPriceAnalysis
- **`Risk Factor Analysis`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/PremiumCost/RiskFactorAnalysis


## LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.