from json import loads
##from igraph import *

with open('beef house.json') as of:
    data1 = loads(of.readline( ))

with open('fellini.json') as of:
    data2 = loads(of.readline( ))


##date=2015-09-20T00:00:00+0000 #fecha de restriccion(20-09-2015) a las 00:00

lista1=list()
lista2=list()
c=0

for post in data1:
    for likes in post.items()[2]: 
        lista1.append(likes) #se almacenan las personas que le dan like al post en una lista
        
for post in data2:
    for likes in post.items()[2]:#lo mismo de arriba
        lista.append(likes)

        

print "los likes se esta pagina son",len(lista1)-1#entrega el len de la lisa-1 ya que el ultimo dato es innecesario, lo hago de esta forma porque no se me ocurre otra
print "los likes de la segunda pagina son",len(lista2)-1









#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)










#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


