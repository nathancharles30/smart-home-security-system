from tensorflow.keras.models import load_model
import pandas as pd
import io
import sys

from Smart_Home_Security_System.src.preprocess import X_train_scaled

model = load_model("../models/mlp_model.h5")

# Capture model.summary() text
stream = io.StringIO()
model.summary(print_fn=lambda x: stream.write(x + "\n"))
summary_str = stream.getvalue()

# Store as single column row-by-row
lines = summary_str.split("\n")
df = pd.DataFrame(lines, columns=["Model Summary"])

# Save to Excel
df.to_excel("../results/model_summary.xlsx", index=False)

print("Model summary exported to model_summary.xlsx")

import pandas as pd
from tensorflow.keras.models import load_model

model = load_model("../models/mlp_model.h5")

writer = pd.ExcelWriter("../results/model_weights.xlsx", engine='openpyxl')

for i, layer in enumerate(model.layers):
    weights = layer.get_weights()

    if len(weights) > 0:
        w, b = weights

        df_w = pd.DataFrame(w)
        df_b = pd.DataFrame(b)

        df_w.to_excel(writer, sheet_name=f"Layer_{i}_weights", index=False)
        df_b.to_excel(writer, sheet_name=f"Layer_{i}_biases", index=False)

writer.close()

print("Model weights exported to model_weights.xlsx")

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

model = load_model("../models/mlp_model.h5")

y_pred = model.predict(X_train_scaled).flatten()
df = pd.DataFrame({"Prediction": y_pred})

df.to_excel("../results/predictions.xlsx", index=False)

print("Predictions exported to predictions.xlsx")
