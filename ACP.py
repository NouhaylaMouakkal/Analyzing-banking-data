import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

# Lire les données des fichiers CSV
client_data = pd.read_csv('./datasets/Client.csv')
compte_data = pd.read_csv('./datasets/Compte.csv')

# Concaténer les données des clients et des comptes en une seule dataframe
data = pd.merge(client_data, compte_data, on='Id_client')

# Prétraitement des données
data['Amount'] = data['Amount'].str.replace(' dhs', '').astype(float)

# Traitement des données catégorielles
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
# Sélectionner les colonnes numériques pour le graphique avant PCA
numeric_columns = ['Amount', 'Age', 'Gender']
numeric_data = data[numeric_columns]
# Effectuer l'ACP
pca = PCA(n_components=3)
pca_result = pca.fit_transform(numeric_data)

# Calculer la corrélation
regression_acp = numeric_data.corr()
print("Corrélation \n",regression_acp)
# Calculer la moyenne
mean_acp = numeric_data.mean()
print("La moyenne \n",mean_acp)
# Calculer l'écart-type
std_dev_acp = numeric_data.std()
print("Ecart-type \n",std_dev_acp)