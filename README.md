# Projet Python_17E : Filtrage de spams par ML

/!\ : exécuter les fichiers depuis le dossier src et non racine.

## Modules

* random 
* numpy 
* scikit_learn 
* googleapiclient 
* openai
* csv 
* itertools

## Lecture des fichiers csv

Fichiers csv avec les informations COMMENT_ID, AUTHOR,DATE, CONTENT, CLASS pour chaque donnée. \
On extrait (CONTENT: contenu du commentaire) et (CLASS: 1 si spam et 0 sinon).
* mise en forme du contenu des commentaire pour former la matrice X dont chaque ligne représente un commentaire
et chaque colonne un mot, les valeurs sont l'occurence du mot dans le commentaire.
* mise en forme des classes pour former le tableau y de 0 et de 1 

Voir `lecture_csv.py`. 

## Entrainement

On effectue un entraînement sur le jeu de données à disposition. \
Voici les classifieurs : 
1. Clustering. La bilbiothèque KMeans de scikit learn s'entraîne sur le jeu de données sans les classifications (labels) mais trie simplement les commentaires en 2 parties. Une fois classés, on teste la précision des prédictions. Il peut y avoir un inversement entre les 0 et 1, on l'effectue si moins de la moitié des valeurs sont correctes.
2. Régression logistique. Modèle de machine learning supervisé.
3. Arbre de décision. Autre modèle de machine learning supervisé.

Voir le fichier `train.py`. 

## Prédictions sur les données de base

On entraîne les modèles sur les 4 premières vidéos et on fait des prédictions sur la 5e. \
Cette approche fonctionne bien pour les modèles supervisés car on connaît à l'avance l'ensemble des mots sur lesquels entraîner les modèles (on a pris en compte la 5e vidéo pour l'entraînement sur les 4 premières). \
Cependant, le clustering n'est pas très efficace.
Pour voir les efficacités et valeurs obtenues, lancer `train_show.py`.

## Prédiction sur de nouvelles vidéos

Dans le fichier `predict.py`, entrer une URL youtube pour la variable `yt_url` et lancer le fichier.
1. récupération des commentaires de la vidéo entrée grâce à l'API Youtube Data (cf `yt_comments_recup.py`)
2. calcul de la matrice d'occurence `X_test` des **mots présents dans les jeu d'entraînements** dans les nouveaux nouveaux commentaires (environ 4k mots)
3. Affichage et comparaison des prédictions des 3 classifieurs.

## Génération très basique de nouveaux commentaires

Générer du texte est autrement plus complexe que de classifier. 
En effet la sortie demandée n'est pas simplement 0 ou 1 mais beaucoup plus complexe. \
Basé sur le modèle pré-entraîné GPT-2 qui prédit la suite d'un texte donné. En fournissant comme texte d'entrée un nombre restreint de commentaires spam ou non (environ 100 car le modèle est limité), on en obtient de nouveaux. \
Voir `generation.py`.

