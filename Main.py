from json import loads
from igraph import *

with open('beef house.json') as of: #se abren los archivos .json de ambas paginas
    data1 = loads(of.readline( ))

with open('fellini.json') as of:
    data2 = loads(of.readline( ))


date="2015-10-01T00:00:00+0000" #fecha de restriccion(20-09-2015) a las 00:00
year=2015
mes=9

posts1=[0,0,0,0,0,0,0,0,0,0,0,0]  #listas que contendran el numero de post al mes
posts2=[0,0,0,0,0,0,0,0,0,0,0,0]   #check

#lista de listas que tendra los datos likes y coments por cada mes
lkncom1=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
lkncom2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

ppl1=[0,0,0,0,0,0,0,0,0,0,0,0]
ppl2=[0,0,0,0,0,0,0,0,0,0,0,0]

g = Graph()

g.add_vertex("A mano")   #se crean los vertices de las paginas
g.add_vertex("3er tiempo")


for post in data1:
    nombre = str(data1.index(post))  #el nombre del vertice sera su indice
    if post["created_time"]>date:
        year1,mes1=int(post["created_time"].split("-")[0]),int(post["created_time"].split("-")[1])
        year2=year1-year
        if year2==0:     #aqui se calculan los meses de diferencia entre el post y la fecha de hace un anho
            meses_dif=mes1-mes
        if year2==1:
            meses_dif=mes1+2
        posts1[meses_dif]+=1   #se suma 1 al nro de posts segun el mes que corresponde
        g.add_vertex(nombre)        #se crean los vertices y los unen a sus respectivas paginas
        g.add_edge("A mano",nombre)
        lkncom1[meses_dif][0]+=int(post["likes"]["sumary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
        lkncom1[meses_dif][1]+=int(post["comments"]["sumary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
    else:
        pass
    
for post in data2:
    nombre = str(data2.index(post))   #el nombre del vertice sera su indice
    if post["created_time"]>date:
        year1,mes1=int(post["created_time"].split("-")[0]),int(post["created_time"].split("-")[1])
        year2=year1-year
        if year2==0:        #aqui se calculan los meses de diferencia entre el post y la fecha de hace un anho
            meses_dif=mes1-mes
        if year2==1:
            meses_dif=mes1+2
        posts2[meses_dif]+=1   #se suma 1 al nro de posts segun el mes que corresponde
        g.add_vertex(nombre)   #se crean los vertices y los unen a sus respectivas paginas
        g.add_edge("3er tiempo",nombre)
        lkncom2[meses_dif][0]+=int(post["likes"]["sumary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
        lkncom2[meses_dif][1]+=int(post["comments"]["sumary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
    else:
        pass

# por cada post hay un key de ["likes"] y ["comments"]









#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


