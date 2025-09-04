import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("Loading dataset...")  # Debugging message
df = pd.read_csv("cleaned_facebook_apps.csv")
print("Dataset loaded successfully!")

print("Preparing features and labels...")  # Debugging message
X = df.drop(columns=["Malicious","target"])  # Features
y = df["Malicious"]  # Target (0 = Safe, 1 = Malicious)

print("Splitting dataset...")  # Debugging message
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")  # Debugging message
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Making predictions...")  # Debugging message
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

print("Saving model...")
joblib.dump(model, "malicious_app_model.pkl")
print("Model saved as 'malicious_app_model.pkl'.")
print("Training Features:", list(df.columns))
print("Columns in dataset:", list(df.columns))  # Shows all columns
print("Shape of X before dropping 'Malicious':", df.shape)
