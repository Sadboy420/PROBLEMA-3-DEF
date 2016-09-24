from json import loads
from igraph import *

with open('beef house.json') as of: #se abren los archivos .json de ambas paginas
    data1 = loads(of.readline( ))

with open('fellini.json') as of:
    data2 = loads(of.readline( ))


date=2015-09-24T00:00:00+0000 #fecha de restriccion(20-09-2015) a las 00:00
posts1=[0,0,0,0,0,0,0,0,0,0,0,0]  #listas que contendran el numero de post al mes
posts2=[0,0,0,0,0,0,0,0,0,0,0,0]
#lista de listas que tendra los datos likes y coments por cada mes
lkncom1=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
lkncom2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
ppl1=[0,0,0,0,0,0,0,0,0,0,0,0]
ppl2=[0,0,0,0,0,0,0,0,0,0,0,0]


for post in data1:
    if post["created_time"]>date:
        for likes in post.items()[2]: #aca accede directamente a los likes
        print likes
    
for post in data2:
    if post["created_time"]>date:
        











#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


