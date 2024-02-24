import matplotlib.pyplot as plt
import cs
from KNN import pred_time_knn, mean_accuracy_knn, accuracy_knn, std_accuracy_knn
from SVM import pred_time_svm, mean_accuracy_svm, accuracy_svm, std_accuracy_svm

# Temps de prédiction
prediction_time = [pred_time_knn, pred_time_svm]

# Moyenne
mean_accuracy = [mean_accuracy_knn, mean_accuracy_svm]

# Exactitude
accuracy = [accuracy_knn, accuracy_svm]

# Écart-type
std = [std_accuracy_knn, std_accuracy_svm]

# Labels des modèles
models = ['KNN', 'SVM']

csv_file = "Comparaison.csv"

# Write data to CSV file
data = [{'Models': models[i], 'Prediction Time': prediction_time[i], 'Mean Accuracy': mean_accuracy[i],
         'Accuracy': accuracy[i], 'Standard Deviation': std[i]} for i in range(len(models))]

with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['Models', 'Prediction Time', 'Mean Accuracy', 'Accuracy', 'Standard Deviation']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

    print("Data has been written to the CSV file:", csv_file)

# Comparaison des critères
fig, axs = plt.subplots(2, 2, figsize=(10, 4))
fig.suptitle('Comparaison des critères entre KNN et SVM')

# Temps de prédiction
axs[0, 0].bar(models, prediction_time, color=['blue', 'red'])
axs[0, 0].set_title('Temps de prédiction')
axs[0, 0].set_ylabel('Temps (s)')

# Exactitude
axs[0, 1].bar(models, accuracy, color=['blue', 'red'])
axs[0, 1].set_title('Exactitude')
axs[0, 1].set_ylabel('Exactitude')

# Moyenne
axs[1, 0].bar(models, mean_accuracy, color=['blue', 'red'])
axs[1, 0].set_title('Moyenne')
axs[1, 0].set_ylabel('Moyenne')

# Écart-type
axs[1, 1].bar(models, std, color=['blue', 'red'])
axs[1, 1].set_title('Écart-type')
axs[1, 1].set_ylabel('Écart-type')

# Ajustement de l'espacement entre les sous-graphiques
plt.tight_layout()

# Affichage du graphique
plt.show()