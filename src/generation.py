import openai 
from lecture_csv import *
from custom_tools import list_to_prompt

openai.api_key = "Clé sur la fiche projet" # Attention, nombre limité d'appel
comments0, comments1 = extraction_comments_label([bases_noms[0]]) # Séparation des commentaires de la vidéo 1 (Psy) selon les étiquettes

gen_comment0 = openai.Completion.create(
    engine="text-davinci-002",
    prompt=list_to_prompt(comments0, lim=100),
    max_tokens=30, # Majoration du nombre de mots
    n=1, 
    stop=None, # Pas de condition d'arrêt particulière (la condition "\n" ne produit pas de résultat )
    temperature=0.8, # Sorte de taux d'aléatoire, à quel point le nouveau commentaire s'écarte du modèle
)

gen_comment1 = openai.Completion.create(
    engine="text-davinci-002",
    prompt=list_to_prompt(comments1, lim=100),
    max_tokens=50,
    n=1, 
    temperature=0.9,
)

print("----------")
print("Génération d'un commentaire normal : ", gen_comment0['choices'][0]['text'])
print("----------")
print("Génération d'un spam : ", gen_comment1['choices'][0]['text'])