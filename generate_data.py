
import pandas as pd
import numpy as np

# Fixer la graine aléatoire pour reproduire les mêmes données
np.random.seed(42)

# Nombre de clients fictifs
n = 500

# Générer les données des clients
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "salaire": np.random.randint(1200, 8000, n),
    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),
    "anciennete": np.random.randint(0, 15, n),
    "consommation": np.random.randint(0, 100, n)
})

# Définir la variable cible : churn
# 1 = client qui part, 0 = client qui reste
data["churn"] = (
    (data["consommation"] < 30)
    & (data["anciennete"] < 2)
).astype(int)

# Enregistrer les données dans un fichier CSV
data.to_csv("churn_data.csv", index=False)

# Afficher les premières lignes
print("Les 5 premiers clients :")
print(data.head())

# Afficher le nombre de lignes et de colonnes
print("\nDimensions du dataset :", data.shape)

# Afficher le taux de churn
print(f"Taux de churn : {data['churn'].mean():.1%}")

print("\nDataset créé avec succès : churn_data.csv")
