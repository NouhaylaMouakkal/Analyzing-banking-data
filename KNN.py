import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import time
from sklearn.metrics import precision_score,\
recall_score, f1_score, accuracy_score

#Charger les données du compte à partir du fichier CSV
account_data = pd.read_csv("./datasets/Compte.csv")
client_data = pd.read_csv("./datasets/Client.csv")
#Retirer le suffixe 'dhs' de la colonne 'Amount'
account_data['Amount'] = account_data['Amount'].str.replace(' dhs', '').astype(float)
#Définir les classes d'amount
bins = [0, 3333.33, 6666.66, float('inf')]
labels = [1, 2, 3]
#Ajouter une colonne 'Amount Class' aux données du compte
account_data['Amount Class'] = pd.cut(account_data['Amount'], bins=bins, labels=labels, right=False)
#Diviser les données en ensemble d'apprentissage (80%) et ensemble de test (20%)
X = account_data[['Amount']]
y = account_data['Amount Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
#Créer et entraîner le modèle KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

start_time = time.time()
#Prédire les classes des données de test
y_pred_knn = knn.predict(X_test)
end_time = time.time()
#Calculer la précision du modèle
accuracy = knn.score(X_test, y_test)
print("Accuracy1:", accuracy)
accuracy_knn = accuracy_score(y_test,y_pred_knn)
print("Accuracy:", accuracy_knn *100)
pred_time_knn = end_time-start_time
print(f"Prediction Time [s]: {(pred_time_knn):.3f}")
print("Precision:", precision_score(y_test,y_pred_knn,average="weighted"))
print('Recall:', recall_score(y_test, y_pred_knn, average="weighted"))
# calculating f1 score
print('F1 score:', f1_score(y_test, y_pred_knn, average="weighted"))
# calculating mean
mean_accuracy_knn = np.mean(accuracy_score(y_test, y_pred_knn))
print("Mean Accuracy:", mean_accuracy_knn)
# calculating standard deviation
std_accuracy_knn = np.sqrt(np.mean(pred_time_knn **2))
print("Standard Deviation of Accuracy:", std_accuracy_knn)
unique_predictions = np.unique(y_pred_knn)
print("Unique Predictions:", unique_predictions)





