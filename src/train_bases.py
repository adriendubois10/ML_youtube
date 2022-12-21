from sklearn.cluster import KMeans
from lecture_csv import *
from custom_tools import eff, flip

X_full, words, y_full = extraction_mots(bases_noms) # bases_noms contient 5 sets de commentaires
# X,y jeu d'entrainement et X_test,y_test jeu de validation
# On procède ainsi pour que d le nombre de mots existants ne varie pas entre le jeu d'entraînement (4 premières vidéos) et de validation (dernière vidéo)
n = len(extraction_mots(bases_noms[:4])[0])
X, X_test, y, y_test = X_full[:n], X_full[n:], y_full[:n], y_full[n:] 
print(f"{len(X)} commentaires sur le jeu d'entraînement et {len(X_test)} sur le jeu de validation")

# Classifieur 1 : KMeans algo de clustering (non supervisé)

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
y_pred1 = kmeans.labels_
e = eff(y, y_pred1)
e, y_pred1 = flip(e, y_pred1) # si besoin les clusters peuvent être inversés, du fait de l'apprentissage non supervisé les 0 et 1 peuvent être inversés
print("\nEfficacité clustering (non supervisé) :", e)

# Classifieur 2 : Régression Logistique (supervisé)

from sklearn.linear_model import LogisticRegression

logistic_regression = LogisticRegression().fit(X, y)
y_test_regpred = logistic_regression.predict(X_test)
print("\nEfficacité régression logistique sur le modèle d'entraînement (supervisé): ", logistic_regression.score(X, y))
print("Efficacité régression logistique sur le modèle de validation (supervisé): ", eff(y_test,y_test_regpred))

# Classifieur 3 : Arbre de décision (supervisé)

from sklearn.tree import DecisionTreeClassifier

decision_tree = DecisionTreeClassifier().fit(X, y)
y_test_treepred = decision_tree.predict(X_test)
print("\nEfficacité régression logistique sur le modèle d'entraînement (supervisé): ", decision_tree.score(X, y))
print("Efficacité régression logistique sur le modèle de validation (supervisé): ", eff(y_test,y_test_treepred)) 




    






