import matplotlib.pyplot as plt
import pandas as pd
from ACP import pca_result , pca , numeric_data , numeric_columns  , regression_acp , mean_acp , std_dev_acp
from SVM import y_pred_svm , X_test_svm , X_pca_svm,y
from KNN import y_pred_knn , client_data , account_data , bins , labels
#_________________ACP VISUALIZATION__________________
# Créer un figure avec plusieurs sous-graphiques
fig, axes = plt.subplots(nrows=3, figsize=(8, 10))

# Graphique de régression
axes[0].bar(regression_acp.columns, regression_acp.iloc[0])
axes[0].set_ylabel('Correlation')

# Graphique de moyenne
axes[1].bar(mean_acp.index, mean_acp.values)
axes[1].set_ylabel('Mean')

# Graphique d'écart-type
axes[2].bar(std_dev_acp.index, std_dev_acp.values)
axes[2].set_ylabel('Standard Deviation')

# Ajuster l'espacement entre les sous-graphiques
plt.tight_layout()

# Afficher le premier graphique
plt.show()

# Créer le graphique avant PCA
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(numeric_data['Amount'], numeric_data['Age'], numeric_data['Gender'])
ax.set_xlabel('Amount')
ax.set_ylabel('Age')
ax.set_zlabel('Gender')
ax.set_title('Graphical representation before PCA')

# Afficher le deuxième graphique
plt.show()

# Créer le graphique après PCA
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_result[:, 0], pca_result[:, 1], pca_result[:, 2])
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.set_title('Graphical representation after PCA')

# Afficher le troisième graphique
plt.show()

#_________________SVM VISUALIZATION__________________

# Plotting the data
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle('Data Vizualisation before & after SVM')

# Visualisation avant SVM
axs[0].scatter(X_pca_svm[:, 0], X_pca_svm[:, 1], c=y, cmap='viridis')
axs[0].set_xlabel('PC1')
axs[0].set_ylabel('PC2')
axs[0].set_title('Before SVM')

# Visualisation après SVM
axs[1].scatter(X_test_svm[:, 0], X_test_svm[:, 1], c=y_pred_svm, cmap='viridis')
axs[1].set_xlabel('PC1')
axs[1].set_ylabel('PC2')
axs[1].set_title('After SVM')

# Ajustement de l'espacement entre les sous-graphiques
plt.tight_layout()

# Affichage du graphique
plt.show()


#_________________KNN VISUALIZATION__________________
#Visualiser les résultats
class_counts = pd.Series(y_pred_knn).value_counts(normalize=True) * 100
class_labels = ['Class 1: Amount < 3333.33', 'Class 2: 3333.33 <= Amount <= 6666.66', 'Class 3: Amount > 6666.66']
plt.pie(class_counts, labels=class_labels, autopct='%1.1f%%')
plt.title('Predicted Amount Class Percentages')
plt.show()


#============================ The whole Dataset ===========================================
# Diviser les âges en classes
client_data['Age Class'] = pd.cut(client_data['Age'], bins=[17, 24, 44, 59, 150], labels=['18-24', '25-44', '45-59', '+60'])

# Créer une table pivot pour compter le nombre de clients par genre et classe d'âge
pivot_table = pd.pivot_table(client_data, values='Id_client', index='Age Class', columns='Gender', aggfunc='count', fill_value=0)

# Tracer le graphique
pivot_table.plot(kind='bar')
plt.xlabel('Age class')
plt.ylabel('Number of clients')
plt.title('Gender by Age')
plt.legend(title='Gender')

# Afficher le graphique
plt.show()

#============================== Each Class =======================================
# Ajouter une colonne 'Amount Class' aux données du compte
account_data['Amount Class'] = pd.cut(account_data['Amount'], bins=bins, labels=labels, right=False)

# Diviser les âges en classes
client_data['Age Class'] = pd.cut(client_data['Age'], bins=[17, 24, 44, 59, 150], labels=['18-24', '25-44', '45-59', '+60'])

# Compter les occurrences de chaque paire (Gender, Age) pour chaque classe
class_counts = client_data.groupby(['Gender', 'Age Class', account_data['Amount Class']]).size().unstack()

# Visualisation des classes Gender par rapport à Age pour chaque classe
class_labels = ['Class 1', 'Class 2', 'Class 3']
fig, axes = plt.subplots(nrows=1, ncols=len(class_labels), figsize=(15, 6))

for i, class_label in enumerate(class_labels):
    counts = class_counts[i + 1].unstack()
    counts.plot(kind='bar', stacked=True, ax=axes[i])
    axes[i].set_xlabel('Gender ')
    axes[i].set_ylabel('Number')
    axes[i].set_title(f'{class_label} -Gender Distribution by Age ')

plt.tight_layout()
plt.show()


