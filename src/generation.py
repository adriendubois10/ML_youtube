import openai 
from lecture_csv import *
from custom_tools import list_to_prompt

openai.api_key = "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"
comments0, comments1 = extraction_comments_label([bases_noms[0]]) # Séparation des commentaires de la vidéo 1 (Psy) selon les étiquettes

gen_comment0 = openai.Completion.create(
    engine="text-davinci-002",
    prompt=list_to_prompt(comments0, lim=120), # On se limite à 150 lignes
    max_tokens=30,
    n=1, # Générer un seul commentaire
    stop=None, # Pas de condition d'arrêt particulière
    temperature=0.8, # Sorte de taux de créativité, à quel point le nouveau commentaire s'écarte du modèle
)

gen_comment1 = openai.Completion.create(
    engine="text-davinci-002",
    prompt=list_to_prompt(comments1, lim=120),
    max_tokens=50,
    n=1, 
    stop=None,
    temperature=0.8,
)

print("----------")
print("Texte similaire aux textes de l'étiquette 0 : ", gen_comment0['choices'][0]['text'])
print("----------")
print("Texte similaire aux textes de l'étiquette 1 : ", gen_comment1['choices'][0]['text'])