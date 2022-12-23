from train_bases import X, y, words, logistic_regression, decision_tree # Importation de modèles entraînés sur les données initiale
from sklearn.cluster import KMeans
from lecture_csv import *
from custom_tools import eff, sim, ratio
from yt_comments_recup import yt_mat_occ

url_reynoldstonightshow = "https://www.youtube.com/watch?v=5AA2yMgoeS0"
url_avatar2 = "https://www.youtube.com/watch?v=d9MyW72ELq0"
url_topgun = "https://www.youtube.com/watch?v=qSqVVswa420" 
url_greenlantern = "https://www.youtube.com/watch?v=7-GO9fo9DtM"

yt_url = url_greenlantern # <- Entrer url ici
X_test = yt_mat_occ(yt_url, words)

print(f"Prédictions à partir des modèles avec {len(words)} mots connus : ")

# Prédiction
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X_test)
y_clust = kmeans.labels_

# Prédiction des modèles entraînés sur les 5 vidéos du dossier bases
y_reg = logistic_regression.predict(X_test)
y_tree = decision_tree.predict(X_test)

print(f"La régression logistique et l'arbre de décision donnent des résultats {sim(y_reg,y_tree) :.1f}% similaires.")
print(f"Taux de commentaires positifs :\n   *  {max(ratio(y_clust), 100-ratio(y_clust)):.1f}% pour le clustering (non supervisé) \n   * {100-ratio(y_reg): .1f}% pour la régression\n   * {100-ratio(y_tree): .1f}% pour l'arbre")








