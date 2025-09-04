import pandas as pd

# Load the datasets
safe_df = pd.read_csv("malicious_apps.csv")  # Update with your actual file name
malicious_df = pd.read_csv("safe_apps.csv")  # Update with your actual file name

# Add labels (0 = Safe, 1 = Malicious)
safe_df["Malicious"] = 0
malicious_df["Malicious"] = 1

# Combine both datasets
df = pd.concat([safe_df, malicious_df], ignore_index=True)

# Remove unnecessary columns (e.g., 'App Name' if it's not useful for ML)
df.drop(columns=["App Name"], inplace=True, errors="ignore")

# Handle missing values
df.fillna(0, inplace=True)  # Replace missing values with 0

# Convert categorical features to numerical (One-Hot Encoding)
df = pd.get_dummies(df, drop_first=True)

# Save the cleaned dataset
df.to_csv("cleaned_facebook_apps.csv", index=False)

print("Data preprocessing complete. Cleaned data saved as 'cleaned_facebook_apps.csv'.")
