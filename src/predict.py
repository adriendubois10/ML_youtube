from train_bases import X, y, words, logistic_regression, decision_tree # Importation de modèles entraînés sur les données initiale
from lecture_csv import *
from custom_tools import eff, sim, ratio
from yt_comments_recup import yt_mat_occ

yt_url = "https://www.youtube.com/watch?v=d9MyW72ELq0" # Bande annonce de Avatar 2 (environ 40k commentaires)
X_test = yt_mat_occ(yt_url, words)

# Prédiction des modèles entraînés sur les 5 vidéos du dossier bases
print()
y_reg = logistic_regression.predict(X_test)
y_tree = decision_tree.predict(X_test)

print(f"La régression logistique et l'arbre de décision donnent des résultats {sim(y_reg,y_tree) :.1f}% similaires.")
print(f"Taux de commentaires positifs :\n   * {100-ratio(y_reg): .3f}% pour la régression\n   * {100-ratio(y_tree): .3f}% pour l'arbre")








