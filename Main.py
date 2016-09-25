from json import loads
from igraph import *

with open('A mano.json') as of: #se abren los archivos .json de ambas paginas
    data1 = loads(of.readline( ))

with open('3er tiempo.json') as of:
    data2 = loads(of.readline( ))


date="2015-10-01T00:00:00+0000" #fecha de restriccion(20-09-2015) a las 00:00
year=2015
mes=9

posts1=[0,0,0,0,0,0,0,0,0,0,0,0]  #listas que contendran el numero de post al mes
posts2=[0,0,0,0,0,0,0,0,0,0,0,0]   #check

#lista de listas que tendra los datos likes y coments por cada mes
lkncom1=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
lkncom2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#lista que contiene el numero de personas por mes, que comenan y dan like a otra publicacion
ppl1=[0,0,0,0,0,0,0,0,0,0,0,0]
ppl2=[0,0,0,0,0,0,0,0,0,0,0,0]
#lista que contendra los share por mes de los post de la pagina
share1=[0,0,0,0,0,0,0,0,0,0,0,0]
share2=[0,0,0,0,0,0,0,0,0,0,0,0]

uno = Graph()  #se crean 4 grafos, uno por cada metrica
dos = Graph()
tre = Graph()
cuatro = Graph()
#cinco = Graph()

uno.add_vertex("A mano")   #se crean los vertices de las paginas
uno.add_vertex("3er tiempo") #metrica 1

dos.add_vertex("A mano")    #metrica 2
dos.add_vertex("3er tiempo")

tre.add_vertex("A mano")   #metrica 3
tre.add_vertex("3er tiempo")

cuatro.add_vertex("A mano")    #metrica 4
cuatro.add_vertex("3er tiempo")

#cinco.add_vertex("A mano")   #metrica 5
#cinco.add_vertex("3er tiempo")

for num in range(12):
	uno.add_vertex(str(num))
	uno.add_edge(str(num),"A mano")
	dos.add_vertex(str(num))
	dos.add_edge(str(num),"A mano")
	tre.add_vertex(str(num))
	tre.add_edge(str(num),"A mano")
	cuatro.add_vertex(str(num))
	cuatro.add_edge(str(num),"A mano")

for num in range(12,24):
	uno.add_vertex(str(num))
	uno.add_edge(str(num),"3er tiempo")
	dos.add_vertex(str(num))
	dos.add_edge(str(num),"3er tiempo")
	tre.add_vertex(str(num))
	tre.add_edge(str(num),"3er tiempo")
	cuatro.add_vertex(str(num))
	cuatro.add_edge(str(num),"3er tiempo")


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
        uno.add_vertex(post["id"])        #se crean los vertices y los unen a sus respectivas paginas
	uno.add_edge(post["id"],str(meses_dif))
	ppl_lk=set()
        ppl_cmt=set()
	if "shares" in post.keys():
	    share1[meses_dif]+=post["shares"]["count"]
	    cuatro.add_vertex(post["id"]) #falta agregar peso a los vertices de shares
	    cuatro.add_edge(post["id"],str(meses_dif))
	if "likes" in post.keys():
	    if "total_count" in post["likes"]["summary"].keys():
                lkncom1[meses_dif][0]+=int(post["likes"]["summary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
	    for likes in post["likes"]["data"]:
                ppl_lk.add(likes["id"])    #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
	if "comments" in post.keys():
	    if "total_count" in post["comments"]["summary"].keys():
                lkncom1[meses_dif][1]+=int(post["comments"]["summary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
	    for comment in post["comments"]["data"]:
                ppl_cmt.add(comment["from"]["id"])     #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
        ppl1[meses_dif]+=len(ppl_lk&ppl_cmt)
	for personas in ppl_lk&ppl_cmt:
	    tre.add_vertex(personas)
	    tre.add_edge(personas,str(meses_dif))
        
    else:
        pass
for post in data2:
    nombre = str(data2.index(post))  #el nombre del vertice sera su indice
    if post["created_time"]>date:
        year1,mes1=int(post["created_time"].split("-")[0]),int(post["created_time"].split("-")[1])
        year2=year1-year
        if year2==0:     #aqui se calculan los meses de diferencia entre el post y la fecha de hace un anho
            meses_dif=mes1-mes
        if year2==1:
            meses_dif=mes1+2
        posts2[meses_dif]+=1   #se suma 1 al nro de posts segun el mes que corresponde
        uno.add_vertex(post["id"])        #se crean los vertices y los unen a sus respectivas paginas
	uno.add_edge(post["id"],str(meses_dif+12))
	ppl_lk=set()
        ppl_cmt=set()
	if "shares" in post.keys():
	    share2[meses_dif]+=post["shares"]["count"]
	    cuatro.add_vertex(post["id"])		#falta agregar peso a los vertices de shares
	    cuatro.add_edge(post["id"],str(meses_dif+12))
	if "likes" in post.keys():
	    if "total_count" in post["likes"]["summary"].keys():
                lkncom2[meses_dif][0]+=int(post["likes"]["summary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
	    for likes in post["likes"]["data"]:
                ppl_lk.add(likes["id"])  #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
	if "comments" in post.keys():
	    if "total_count" in post["comments"]["summary"].keys():
                lkncom2[meses_dif][1]+=int(post["comments"]["summary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
	    for comment in post["comments"]["data"]:
                ppl_cmt.add(comment["from"]["id"])      #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
        ppl2[meses_dif]+=len(ppl_lk&ppl_cmt)    #se obtiene la interseccion de la gente que comento y dio like al mismo tiempo
        for personas in ppl_lk&ppl_cmt:
	    tre.add_vertex(personas)
	    tre.add_edge(personas,str(meses_dif+12))
    else:
        pass
uno.write_gml("uno")
cuatro.write_gml("cuatro")
tre.write_gml("tre")


# por cada post hay un key de ["likes"] y ["comments"]









#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


