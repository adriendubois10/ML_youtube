# Projet Python_17E : Filtrage de spams par ML

## Plan 

1. Lecture des fichiers csv OK
2. Traitement du texte OK
3. Introduction des notions et scikit-learn OK
4. Entrainement OK
5. Tests sur les jeux de validation du projet OK
6. Récupération des commentaires sur une page YT pour effectuer d'autres tests

## Lecture des fichiers csv

## Entrainement

Voir le fichier `train.py`. On effectue un entraînement sur le jeu de données à disposition.
La bilbiothèque KMeans de scikit learn s'entraîne sur le jeu de données sans les classifications (labels) mais donne classe simplement les commentaires en 2 parties. Une fois classée, on teste la précision des prédictions. Il peut y avoir un inversement entre les 0 et 1, on l'effectue si moins de la moitié des valeurs sont correctes.

