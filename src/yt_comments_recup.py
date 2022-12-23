# Importation API google 
import googleapiclient.discovery as ggl

key_api = "AIzaSyDUs4iHJ3D7lR0TKiuCf40v3ZNYXOFopk8" # Obtention d'une clé sur le service développeur de google

def recup_comments(URL):
    ''' Entrée : URL d'une vidéo youtube
        Sortie : Liste des commentaires de la vidéo '''
    yt_video_id = URL.replace("https://www.youtube.com/watch?v=", "") # Extraction de l'identifiant de la vidéo depuis l'URL
    youtube = ggl.build("youtube", "v3", developerKey = key_api)  
    request = youtube.commentThreads().list( # Requête : lister 100 (chiffre max) commentaires
        part='snippet',
        videoId=yt_video_id, # Identifiant de la vidéo
        textFormat='plainText', # Choix entre HTML et texte brut
        key=key_api,
        maxResults=100, # Nombre de commentaires par page
    )
    request_titre = youtube.videos().list(
        part='snippet',
        id=yt_video_id,
        key=key_api
        )
    titre = request_titre.execute()['items'][0]['snippet']['title']
    comments = []

    print(f"Récupération des commentaires sur la vidéo <{titre}> ... (peut prendre du temps)")
    while request != None: # Tant qu'il reste des pages à défiler
        comments_currentpage = request.execute()
        comments += [ x['snippet']['topLevelComment']['snippet']['textOriginal'] for x in comments_currentpage['items']]
        request = youtube.commentThreads().list_next(request, comments_currentpage) # lister les 100 commentaires suivants
    print("Terminé!")

    return comments

def yt_mat_occ(URL, words_list):
    mat = []
    for comment in recup_comments(URL):
        mat.append([comment.count(word) for word in words_list])
    return mat


