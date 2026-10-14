# Smart Home Security System Using Machine Learning

## Overview

This project explores the use of machine learning for classifying sensor data in a simulated smart home security environment. It uses a Multi-Layer Perceptron (MLP) neural network to classify observations from five sensor features: motion, door activity, sound level, temperature and light level.

The project was developed as an initial machine learning prototype. It provides a foundation for further research into classification performance, class imbalance and the reliability of detecting rare events in smart home sensor data.

## Project Aim

The initial aim is to investigate how a neural network can classify simulated smart home sensor observations and to establish a foundation for evaluating machine learning methods in security-related applications.

## Dataset

The project includes a synthetic dataset stored at:

`Smart_Home_Security_System/Dataset/smart_security_dataset.csv`

The dataset contains 2,000 observations and six columns:

| Feature | Description |
|---|---|
| `motion_sensor` | Motion sensor reading |
| `door_sensor` | Door sensor reading |
| `sound_level` | Sound level measurement |
| `temperature` | Temperature measurement |
| `light_level` | Light level measurement |
| `label` | Target class used for classification |

The target contains three numerical classes:

| Class label | Number of observations | Percentage |
|---|---:|---:|
| 0 | 1,932 | 96.6% |
| 1 | 62 | 3.1% |
| 2 | 6 | 0.3% |

The meaning of each class should be confirmed from the dataset-generation process before assigning specific security interpretations to the labels.

The dataset is highly imbalanced, particularly because class 2 contains only six observations. This is an important limitation when assessing the model's ability to identify rare classes.

The data is synthetic and should not be assumed to represent the full range of behaviour, noise or anomalies found in real smart home environments.

## Technologies Used

- Python
- TensorFlow and Keras
- pandas
- NumPy
- scikit-learn
- openpyxl
- Excel-compatible result files

## Methodology

### 1. Data preprocessing

The preprocessing script separates the sensor features from the target labels and uses an 80/20 stratified train-test split with a fixed random state of 42.

A `StandardScaler` is fitted to the training features and then applied to the test features. The resulting feature arrays and target labels are exported as CSV files.

### 2. MLP model

The neural network is implemented using TensorFlow/Keras and contains the following layers:

- Input layer accepting the five sensor features.
- Dense hidden layer with 32 units and ReLU activation.
- Dense hidden layer with 16 units and ReLU activation.
- Output layer with three units and softmax activation.

The model is compiled using the Adam optimiser, sparse categorical cross-entropy loss and accuracy as a training metric.

Training is configured for up to 20 epochs with a batch size of 32 and a validation split of 20% of the training data.

### 3. Evaluation

The training script evaluates the model on the held-out test set and generates a classification report.

Accuracy alone is insufficient for this dataset because the majority class dominates the observations. Future evaluation should therefore include class-specific precision, recall, F1-scores and a confusion matrix.

Results for the rare classes must be interpreted cautiously because the small number of examples limits the reliability of the evaluation.

## Repository Structure

```text
smart-home-security-system-main/
├── README.md
└── Smart_Home_Security_System/
    ├── Dataset/
    │   ├── smart_security_dataset.csv
    │   └── processed/
    │       ├── X_train_scaled.csv
    │       ├── X_test_scaled.csv
    │       ├── y_train.csv
    │       └── y_test.csv
    ├── Models/
    │   └── mlp_model.h5
    ├── Results/
    │   ├── model_summary.xlsx
    │   ├── model_weights.xlsx
    │   └── predictions.xlsx
    └── src/
        ├── preprocess.py
        ├── train_mlp.py
        └── Excel.py
```

The repository also contains Python bytecode generated during previous execution. This is not required as source code for the project.

## Limitations

- The dataset is synthetic and may not represent real household sensor behaviour.
- The target classes are highly imbalanced.
- Only a single MLP architecture is currently implemented in the main training script.
- Accuracy may provide a misleading impression of performance on rare classes.
- The existing implementation requires further testing to confirm that the preprocessing, training and result-export scripts work together correctly.
- No real-world deployment or residential security effectiveness has been established.

## Planned Master's Research Extension

The project will be extended as part of a Master's Machine Learning Algorithms study. The proposed research will investigate how class imbalance affects the performance of three classifiers:

1. Multi-Layer Perceptron (MLP).
2. Logistic Regression.
3. Random Forest.

The study will investigate both the existing synthetic dataset and a suitable public smart home or IoT anomaly-detection dataset.

The models will be compared using appropriate classification metrics, including macro-F1, per-class precision and recall, confusion matrices and false-positive rates where applicable. A class-imbalance intervention may also be evaluated.

The datasets will initially be analysed separately because their sensor features and target definitions may differ. The public dataset, final experimental procedures and any additional preprocessing will be confirmed after inspecting the available data.

These extensions are proposed research activities and should not be interpreted as completed experiments.

## Ethical Considerations

The use of synthetic data avoids the need to collect personal household sensor information for the initial prototype. Any public dataset used in future experiments will be checked for its source, licence and appropriate use conditions.

The model is an academic prototype and has not been validated for use as an operational home security system.

## Author

Computer Science project exploring machine learning classification using simulated smart home sensor data.
