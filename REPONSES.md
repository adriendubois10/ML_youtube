# Fiche réponse

## Question 1
 a) `lecture_csv.py` : On importe le jeu de donées depuis le format csv vers une liste de dictionnaires (un pour chaque commentaire) dont les clés sont `CONTENT_ID, AUTHOR`, etc. On extrait `CONTENT` et `TAG` comme listes. \
b) `lecture_csv.py` : Comme suggéré, on met en forme le contenu des commentaires comme une matrice d'occurence des mots à l'aide du modèle *Bag of world*. \
c) `train_show.py` : `X` jeu d'entraînement et `X_test` jeu de validation. Même si les données sont séparées il faut que l'ensemble des mots soit commun et que la position de l'occurence d'un mot donné soit la même dans les matrices. \
d) `train_show.py` : Kmeans (clustering), LogisticRegression (régression logistique) et DecisionTreeClassifier (arbre de décision) modèles de scikit-learn. \
e) Lancer `train_show.py`.

## Question 2
**Features :** commentaire / label / mots du commentaire désordonnés \
**Classifieurs :** Parmi les classifieurs de scikit-learn, j'ai choisi la *régression logistique* et l'*arbre de décision* car ce sont deux modèles classiques de la classification mais aussi par curiosité le *clustering K-Means* qui est un modèle non supervisé et qui sera donc moins cohérent pour identifier un spam. \
Par défault, ces classifieurs sont binaires. Le choix de mise en forme des données est aussi important. Avec la perte de l'ordre, les mots vont avoir un certain poids "de spam" et avoir beaucoup de mots "à risques" ou certains mots toxiques va classifier un commentaire comme spam. \
Les classifieurs sont très faciles à utliser et rapides à apprendre. On comprend assez bien comment fonctionnent les modèles :
- le *clustering* va identifier les commentaires comme points dans $R^d$ (la coordonnées i est l'occurence du i-ème mots du commentaire) et les clusters sont deux points qui minimisent la distance, avec les spams pour le premier point et le reste pour l'autre. Un nouveau commentaire est ensuite classifié en fonction de la proximité aux clusters. 
- la *régression logistique* est un modèle où l'on associe une étquette à partir d'une fonction score linéaire en les coefficients, utile sur des petis jeu de données
- l'*arbre de décision* est un modèle d'arbre simple à utiliser, l'idée est de trouver de bonnes séquence de tri (séparationen deux à chaque noeud) pour la classification. 

**Hyperparamètres :** 
- *clustering* : nombre de clusters (n_clusters=2 car classifieur), choix aléatoires, nombre de modèles à lancer (n_init=10, on garde le meilleur)
- *régression logistique* : nombre maximal d'itération (de la descente de gradiennt) avant convergence du modèle 
- *arbre de décision* : profondeur maximale , gain minimum de performances pour split un noeud de l'arbre, nombre d'échantillon minimal pour split un noeud

## Question 3
Ajout de deux features (en plus du clustering) :
1. Récupération des commentaires d'une vidéo youtube à partir d'une URL.
2. Génération de nouveaux commentaires




