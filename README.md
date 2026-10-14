# AI-Driven Smart Home Security System

## Overview

This project investigates the use of machine learning to improve smart home security by identifying suspicious activity and reducing false alarms. A Multi-Layer Perceptron (MLP) neural network is trained using structured IoT-style sensor data to classify normal household activity and potential security anomalies.

The project focuses on developing a lightweight, privacy-aware approach that could support future edge-based smart home security systems.

## Research Aim

To investigate whether a machine learning-based intrusion detection system can distinguish between normal household activity and potential security threats while reducing false positives.

## Objectives

- Review existing smart home security systems and machine learning-based intrusion detection approaches.
- Develop and preprocess a synthetic dataset representing household sensor activity.
- Implement and train an MLP classification model.
- Evaluate model performance using appropriate classification metrics.
- Investigate false positives, privacy considerations, and the potential for edge deployment.
- Identify limitations and recommend future improvements.

## Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook / Python scripts

*The libraries listed above should be checked against the actual implementation before publication.*

## Methodology

The project follows a machine learning workflow:

1. **Dataset creation:** Generate synthetic data representing normal and potentially suspicious household activity.
2. **Preprocessing:** Clean the data, prepare input features, encode labels where necessary, and scale numerical variables.
3. **Model development:** Implement a Multi-Layer Perceptron (MLP) for binary classification.
4. **Training:** Train the model using the prepared dataset and selected hyperparameters.
5. **Evaluation:** Assess predictions using suitable classification metrics, including precision, recall, F1-score, and the confusion matrix where available.
6. **Analysis:** Examine false positives, model limitations, privacy implications, and potential edge deployment.

## Dataset

The project uses a synthetic dataset to simulate smart home security activity. Synthetic data avoids the need to collect sensitive information from real households during initial experimentation.

However, synthetic data may not fully represent real household behaviour, sensor noise, or environmental variability. The results should therefore be interpreted as experimental findings rather than proof of real-world security effectiveness.

## Results and Evaluation

The model's performance is assessed using the exported experimental outputs, including:

- `model_summary.xlsx` — model architecture information.
- `model_weights.xlsx` — exported model weights.
- `predictions.xlsx` — model prediction outputs.

Visualisations can be included to illustrate prediction distributions, learned weight distributions, training performance, and classification errors, where the corresponding data is available.

Quantitative claims about accuracy, precision, recall, and false-positive rates should be added only when supported by the actual experimental results.

## Ethical Considerations

Privacy and responsible AI are important considerations in smart home security. The use of synthetic data reduces exposure to personal household information. Potential limitations include dataset bias, limited representativeness, and uncertainty about performance in real environments.

The system is an experimental research prototype and should not be treated as a validated residential security product.

## Limitations

- Reliance on synthetic rather than real-world household data.
- Potential bias in the generated data and its labels.
- Limited evidence of performance across different household environments.
- No real-world deployment or user evaluation.
- Further testing is required to establish edge-device performance and practical false-alarm reduction.

## Future Work

Potential extensions include testing with suitable real-world datasets, comparing the MLP against alternative classification algorithms, improving feature engineering, tuning alert thresholds, and evaluating model compression for edge devices.

Further work could also investigate combining sensor-based detection with computer vision, provided privacy and computational requirements are addressed.

## Repository Structure

```text
smart-home-security/
├── dataset/
│   ├── raw/
│   └── processed/
├── notebooks/
├── models/
├── results/
│   ├── model_summary.xlsx
│   ├── model_weights.xlsx
│   └── predictions.xlsx
├── README.md
└── requirements.txt
```

*This is a suggested structure. Adjust it to match the files and folders actually present in your repository.*

## Disclaimer

This project was developed for academic research and educational purposes. Its results do not establish that the model is suitable for operational security systems without further validation.

## Author

Computer Science research project investigating machine learning for smart home security, anomaly detection, and false-positive reduction.
