from train_bases import X, y, words, logistic_regression, decision_tree # Importation de modèles entraînés sur les données initiale
from lecture_csv import *
from custom_tools import eff, sim, ratio

csvfile = ""
X_test = extraction_partielle_mots(csvfile, words) # restriction aux mots sur les données d'entraînement

y_reg = logistic_regression.predict(X_test)
y_tree = decision_tree.predict(X_test)

print(f"La régression logistique et l'arbre de décision donnent des résultats {sim(y_reg,y_tree) :.3f} similaires.")
print(f"Taux de spams {ratio(y_reg): .3f} pur la régression et {ratio(y_tree): .3f} pour l'arbre")






