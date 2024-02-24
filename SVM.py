import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
import time
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# Read data from csv files
client_data = pd.read_csv("./datasets/Client.csv")
account_data = pd.read_csv('./datasets/Compte.csv')
data = pd.merge(client_data, account_data, on='Id_client')
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
data['Amount'] = data['Amount'].str.replace(' dhs', '').astype(float)

# Select the columns for the SVM model
variables = ['Amount', 'Age', 'Gender']
subset = data[variables]

# Create the data
X = subset[['Amount', 'Age', 'Gender']]
y = subset['Gender']

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)
X_pca_svm = pca.fit_transform(X_scaled)

# Split the scaled data into training and testing sets
X_train, X_test_svm, y_train, y_test = train_test_split(X_pca_svm, y, test_size=0.2, random_state=20)

# Perform oversampling for class imbalance
smote = SMOTE()
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Perform hyperparameter tuning using GridSearchCV
param_grid = {'C': [1,10,100], 'gamma': [1,10,100]}
clf_linear = SVC(kernel='linear')
grid_search = GridSearchCV(clf_linear, param_grid, cv=3)
grid_search.fit(X_train_resampled, y_train_resampled)

# Train the classifier with best hyperparameters
best_clf = grid_search.best_estimator_
best_clf.fit(X_train_resampled, y_train_resampled)

# Make predictions
start_time = time.time()
y_pred_svm = best_clf.predict(X_test_svm)
end_time = time.time()

# Evaluate the classifier
accuracy_svm = metrics.accuracy_score(y_test, y_pred_svm)
print("Accuracy:", round(accuracy_svm * 100, 2), "%")

# Prediction time
pred_time_svm = end_time - start_time
print(f"Prediction Time [s]: {(pred_time_svm):.3f}")

# Other evaluation metrics
print("Precision:", precision_score(y_test, y_pred_svm, average="weighted"))
print('Recall:', recall_score(y_test, y_pred_svm, average="weighted"))
print('F1 score:', f1_score(y_test, y_pred_svm, average="weighted"))

# Mean Accuracy
mean_accuracy_svm = np.mean(accuracy_score(y_test, y_pred_svm))
print("Mean Accuracy:", mean_accuracy_svm)

# Standard Deviation
variance = np.mean(pred_time_svm ** 2)
std_accuracy_svm = np.sqrt(variance)
print("Standard Deviation of Accuracy:", std_accuracy_svm)

unique_predictions = np.unique(y_pred_svm)
print("Unique Predictions:", unique_predictions)

