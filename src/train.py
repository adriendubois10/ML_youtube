from sklearn.cluster import KMeans
from lecture_csv import *

csvfiles = bases_noms

X, words, y = extraction_mots(csvfiles)
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
y_pred = kmeans.labels_

# Mesurons l'efficacité de la prédiction et on inverse les 0 et les 1 si besoin : les clusters peuvent être inversés
from custom_tools import eff, flip

e = eff(y, y_pred) # Valeur entre 0 si y et y_pred sont inversés et 1 si sont les mêmes
e, y_pred = flip(y, y_pred)
print("Efficacité :", e)
    






