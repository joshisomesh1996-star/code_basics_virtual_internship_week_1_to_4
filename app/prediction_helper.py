import pandas as pd
import joblib

# --- Load saved artifacts ---
artifacts = joblib.load("artifacts/final_bundle.joblib")
le_dict = artifacts["label_encoders"]
final_columns = artifacts["final_columns"]
model = artifacts["model"]

# --- Ordinal mappings ---
zone_map = {"Rural": 0, "Semi-Urban": 1, "Urban": 2, "Metro": 3}
income_levels_map = {
    "<10L": 1, "10L - 15L": 2, "16L - 25L": 3, "26L - 35L": 4, "> 35L": 5, "Not Reported": 0
}
consume_frequency_map = {"0-2 times": 1, "3-4 times": 2, "5-7 times": 3}
awareness_map = {"0 to 1": 1, "2 to 4": 2, "above 4": 3}

# --- Derived Feature Formulas ---
def compute_zas(zone, income_level):
    return zone_map[zone] * income_levels_map[income_level]

def compute_cf_ab(consume_freq, awareness):
    cf_val = consume_frequency_map[consume_freq]
    aw_val = awareness_map[awareness]
    return round(cf_val / (cf_val + aw_val), 2)

def compute_bsi(zas, cf_ab):
    # Placeholder: modify if you had a specific notebook formula
    return round((zas + cf_ab) / 2, 3)

# --- Preprocessing for Model Inference ---
def preprocess_input(input_dict):
    # Add engineered numerical features
    zas = compute_zas(input_dict["zone"], input_dict["income_levels"])
    cf_ab = compute_cf_ab(input_dict["consume_frequency(weekly)"], input_dict["awareness_of_other_brands"])
    bsi = compute_bsi(zas, cf_ab)

    input_dict["zas_score"] = zas
    input_dict["cf_ab_score"] = cf_ab
    input_dict["bsi"] = bsi

    # Convert to DataFrame
    X_new = pd.DataFrame([input_dict])

    # Apply label encoders for ordinal columns
    for col, le in le_dict.items():
        if col != "price_range" and col in X_new.columns:
            X_new[col] = le.transform(X_new[col])

    # One-hot encode and align with training schema
    X_new = pd.get_dummies(X_new, drop_first=True)
    X_new = X_new.reindex(columns=final_columns, fill_value=0)

    return X_new

# --- Compute derived features for UI display ---
def compute_derived_features(input_dict):
    zas = compute_zas(input_dict["zone"], input_dict["income_levels"])
    cf_ab = compute_cf_ab(input_dict["consume_frequency(weekly)"], input_dict["awareness_of_other_brands"])
    bsi = compute_bsi(zas, cf_ab)
    return {"zas_score": zas, "cf_ab_score": cf_ab, "bsi": bsi}

# --- Prediction ---
def predict(input_dict):
    X_ready = preprocess_input(input_dict)
    y_pred = model.predict(X_ready)
    return le_dict["price_range"].inverse_transform(y_pred)[0]
