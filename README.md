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