from lecture_csv import *
from custom_tools import eff
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

X, words, y = extraction_mots(bases_noms) # bases_noms contient 5 sets de commentaires

logistic_regression = LogisticRegression().fit(X, y)
decision_tree = DecisionTreeClassifier().fit(X, y)

