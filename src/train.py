from sklearn.cluster import KMeans
from lecture_csv import *

csvfiles = bases_noms

X, words, y = extraction_mots(csvfiles)
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
y_pred = kmeans.labels_

# Mesurons l'efficacité de la prédiction et on inverse les 0 et les 1 si besoin : les clusters peuvent être inversés
def eff(y, y_pred):
    m = 0
    for (x,x_pred) in zip(y,y_pred):
        m += (x == x_pred)
    return m / len(y)

e = eff(y, y_pred)
e, y_pred = (e, y_pred) if (e>0.5) else (1-e, [1-b for b in y])
print(e)
    






