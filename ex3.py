from numpy import *
from pandas import *
import json
from matplotlib import pyplot

fichier=input("Fichier pour générer graph: " )
if fichier[-3:] == 'csv':
    df = read_csv(fichier, index_col=0)
    df.plot.bar(stacked=True, legend=None)
    pyplot.show()
elif fichier[-9:-5] == 'prop':
    with open (fichier, "r") as f:
        y = json.loads(f.readline())
        x = json.loads(f.readline())
    df = DataFrame()
    df['Proportion infecté']=Series(x, index=y)
    df.plot.bar()
    pyplot.legend()
    pyplot.show()
else:
    with open (fichier, "r") as f:
        y = json.loads(f.readline())
        x = json.loads(f.readline())
    df = DataFrame()
    df["Durée de l'épidémie"]=Series(x, index=y)
    df.plot()
    pyplot.legend()
    pyplot.show()
