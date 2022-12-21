def eff(y, y_pred):
    m = 0
    for (x,x_pred) in zip(y,y_pred):
        m += (x == x_pred)
    return m / len(y)

def flip(e, y_pred):
    if e>0.5:
        e, y_pred
    else:
        return 1-e, [1-b for b in y_pred]