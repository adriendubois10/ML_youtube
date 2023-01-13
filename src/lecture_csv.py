import csv
from itertools import islice, tee
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

bases_noms = ["..//bases//" + x for x in ["Youtube01-Psy.csv", "Youtube02-KatyPerry.csv", "Youtube03-LMFAO.csv", "Youtube04-Eminem.csv", "Youtube05-Shakira.csv"]]

def rows(csvfile):
    ''' Enumérateur des données du fichier csv
        Chaque élément est un dictionnaire '''
    reader = csv.DictReader(csvfile)
    for row in reader:
        yield row

def infos_csv(csvfile, n=1):
    ''' Affichage du nombre de données, des classes, des n premières lignes du fichiers csv '''
    with open(csvfile, 'r') as cf:
        enum_row, enum_row_copy = tee(rows(cf)) # Les itérateurs sont ainsi indépendant 
        print("FICHIER : ", csvfile)
        print("Type des données :", ', '.join([key for key in next(enum_row_copy).keys()]))
        print(f'Nombre de lignes : {1 + sum(1 for _ in enum_row_copy)}')
        enum_borne = islice(enum_row, n)
        for row in enum_borne:
            print("---")
            for k,v in row.items():
                print("    ", k, ":", v)

def enlever_ponctuation(texte):
    ''' Enleve les caractères génants pour la lecture d'un mot seul '''
    for ch in ":?!,\"[]().":
        texte = texte.replace(ch, '')
    return texte

def extraction_mots(csvfiles):
    ''' Entrée : liste de chemins vers des fichiers csv correctement formatés pour les commentaires
        Sortie : Matrice d'occurence des mots par commentaire, pour tous les commentaires '''
    data, labels_ = [], []
    for csvfile in csvfiles:
        with open(csvfile, 'r') as cf:
            for comment in rows(cf):
                data.append(comment['CONTENT'])
                labels_.append(int(comment['CLASS']))
    cv = CountVectorizer()
    # Matrice dont les lignes sont les commentaires, les colonnes les mots, et les valeurs leur occurence dans le commentaire
    mat_count = cv.fit_transform(data).toarray()
    # Ordre des mots dans le tableau
    mots = cv.get_feature_names_out()
    return mat_count, mots, labels_

def extraction_partielle_mots(csvfile, mots):
    ''' Entrée : liste de chemins vers des fichiers csv correctement formatés pour les commentaires et une liste blanche de mots
        car on filtre seulement les mots rencontrés dans le jeu d'entraînement.
        Sortie : Matrice d'occurence des mots uniquement présents dans la liste blanche par commentaire, pour tous les commentaires '''
    mat_count = []    
    with open(csvfile, 'r') as cf:
        for comment in rows(cf):
            mat_count.append([comment['CONTENT'].count(mot) for mot in mots])
    return mat_count

def extraction_comments_label(csvfiles):
    ''' Entrée : liste de chemins vers des fichiers csv correctement formatés pour les commentaires
        Sortie : liste des commentaires etiquetés 0 , liste des commentaires étiqutés 1 '''
    comments0, comments1, k = [], [], 0
    for csvfile in csvfiles:
        with open(csvfile, 'r') as cf:
            for comment in rows(cf):
                if int(comment['CLASS']) == 0: 
                    comments0.append(comment['CONTENT'])
                else:
                    comments1.append(comment['CONTENT'])
    return comments0, comments1
