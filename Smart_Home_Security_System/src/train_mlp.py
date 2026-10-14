import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import classification_report, confusion_matrix



# Load processed data
X_train = pd.read_csv("../dataset/processed/X_train_scaled.csv").values
X_test = pd.read_csv("../dataset/processed/X_test_scaled.csv").values
y_train = pd.read_csv("../dataset/processed/y_train.csv").values.ravel()
y_test = pd.read_csv("../dataset/processed/y_test.csv").values.ravel()

# Build model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=20,
    batch_size=32
)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", acc)

# Predictions
y_pred = np.argmax(model.predict(X_test), axis=1)
print(classification_report(y_test, y_pred))

# Save
model.save("../models/mlp_model.h5")
print("Model saved to models/")



