import csv
from itertools import islice, tee


bases_noms = ["..//bases//" + x for x in ["Youtube01-Psy.csv", "Youtube02-KatyPerry.csv", "Youtube03-LMFAO.csv", "Youtube04-Eminem.csv", "Youtube05-Shakira.csv"]]

def rows(csvfile):
    reader = csv.DictReader(csvfile)
    for row in reader:
        yield row

def infos_csv(csvfile, n=2):
    with open(csvfile, 'r') as cf:
        enum_row, enum_row_copy = tee(rows(cf))
        print("FICHIER : ", csvfile)
        print("Type des données :", ', '.join([key for key in next(enum_row_copy).keys()]))
        print(f'Nombre de lignes : {1 + sum(1 for _ in enum_row_copy)}')
        enum_borne = islice(enum_row, n)
        for row in enum_borne:
            print("---")
            for k,v in row.items():
                print("    ", k, ":", v)

infos_csv(bases_noms[0])




