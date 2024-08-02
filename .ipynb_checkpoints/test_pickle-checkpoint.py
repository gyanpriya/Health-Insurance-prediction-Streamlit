import pickle

# Test loading Gradient Boosting model
try:
    with open('gb_model', 'rb') as f:
        gradient_model = pickle.load(f)
    print("Gradient Boosting model loaded successfully.")
except Exception as e:
    print(f"Error loading Gradient Boosting model: {e}")

# Test loading Random Forest model
try:
    with open('rf_model', 'rb') as f:
        random_forest_model = pickle.load(f)
    print("Random Forest model loaded successfully.")
except Exception as e:
    print(f"Error loading Random Forest model: {e}")
