import numpy as np

def eff(y, y_pred):
    m = 0
    for (x,x_pred) in zip(y,y_pred):
        m += (x == x_pred)
    return m / len(y)

def flip(e, y_pred):
    if e>0.5:
        return e, y_pred
    else:
        return 1-e, [1-b for b in y_pred]

def sim(y1, y2):
    return 100 * (1 - np.mean(abs(y1 - y2)))

def ratio(y):
    ''' Entrée : y tableau de 0 si positif, 1 si négatif '''
    return 100 * np.mean(y)

def list_to_prompt(liste, lim=512):
    return "\n".join(liste[:lim])