import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Load dataset
df = pd.read_csv("../dataset/smart_security_dataset.csv")

# Split features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save processed data
os.makedirs("../dataset/processed", exist_ok=True)

pd.DataFrame(X_train_scaled).to_csv("../dataset/processed/X_train_scaled.csv", index=False)
pd.DataFrame(X_test_scaled).to_csv("../dataset/processed/X_test_scaled.csv", index=False)
pd.DataFrame(y_train).to_csv("../dataset/processed/y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("../dataset/processed/y_test.csv", index=False)

print("Preprocessing complete! Files saved inside dataset/processed/")

