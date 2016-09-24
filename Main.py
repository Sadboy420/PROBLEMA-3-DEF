from json import loads
##from igraph import *

with open('beef house.json') as of:
    data1 = loads(of.readline( ))

with open('fellini.json') as of:
    data2 = loads(of.readline( ))


##date=2015-09-20T00:00:00+0000 #fecha de restriccion(20-09-2015) a las 00:00

c=0
for post in data1:
    for likes in post.items()[2]: #aca accede directamente a los likes
        print likes
    
for post in data2:
    pass











#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


