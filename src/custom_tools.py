import numpy as np
import random as rd

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

def list_to_prompt(liste, lim=100):
    new_liste = []
    for _ in range(min(len(liste),lim)):
        new_liste.append(rd.randint(len(liste)))
    return "\n".join(new_liste)