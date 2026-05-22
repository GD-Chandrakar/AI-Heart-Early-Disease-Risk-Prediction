import joblib
import numpy as np

# Load model
model = joblib.load("heart_model.pkl")

print("Model type:", type(model))
print("Model:", model)

# Check if it's a VotingClassifier
if hasattr(model, 'estimators_'):
    print("\nEstimators in VotingClassifier:")
    for name, est in model.estimators_:
        print(f"  - {name}: {type(est)}")
        if hasattr(est, 'n_features_in_'):
            print(f"    n_features_in_: {est.n_features_in_}")

# Check main model attributes
if hasattr(model, 'n_features_in_'):
    print(f"\nModel expects {model.n_features_in_} features")

# Try with different feature counts
print("\nTesting feature counts:")
for n_features in [8, 12, 13, 14, 15, 16, 17, 18, 20]:
    try:
        test_data = np.zeros((1, n_features))
        model.predict(test_data)
        print(f"  ✓ {n_features} features: SUCCESS")
    except ValueError as e:
        print(f"  ✗ {n_features} features: {str(e)[:60]}...")
