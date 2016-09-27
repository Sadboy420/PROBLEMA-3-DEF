from tkFileDialog import *    #Diego Troncoso, Gabriel Gonzalez, Gonzalo Oberreuter
from Tkinter import *
from json import loads
from igraph import *

global posts1,posts2,lkncom1,lkncom2,ppl1,ppl2,share1,share2,best1,best2,uno,dos,tre,cuatro,cinco #####

uno = Graph()  #se crean 4 grafos, uno por cada metrica
dos = Graph()
tre = Graph()
cuatro = Graph()
cinco = Graph()

def estadistica(nombre1,nombre2):
    with open(nombre1) as of: #se abren los archivos .json de ambas paginas
        data1 = loads(of.readline( ))

    with open(nombre2) as of:
        data2 = loads(of.readline( ))


    date="2015-10-01T00:00:00+0000" #fecha de restriccion(20-09-2015) a las 00:00
    year=2015
    mes=9

    posts1=[0,0,0,0,0,0,0,0,0,0,0,0]  #listas que contendran el numero de post al mes
    posts2=[0,0,0,0,0,0,0,0,0,0,0,0]   #check

    #lista de listas que tendra los datos likes y coments por cada mes
    lkncom1=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    lkncom2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    #lista que contiene el numero de personas por mes, que comentan y dan like a otra publicacion
    ppl1=[0,0,0,0,0,0,0,0,0,0,0,0]
    ppl2=[0,0,0,0,0,0,0,0,0,0,0,0]
    #lista que contendra los share por mes de los post de la pagina
    share1=[0,0,0,0,0,0,0,0,0,0,0,0]
    share2=[0,0,0,0,0,0,0,0,0,0,0,0]

    uno.add_vertex(nombre1,color="blue")   #se crean los vertices de las paginas
    uno.add_vertex(nombre2,color="blue") #metrica 1

    dos.add_vertex(nombre1)    #se crean los vertices de las paginas
    dos.add_vertex(nombre2) #metrica 2

    tre.add_vertex(nombre1)   #se crean los vertices de las paginas
    tre.add_vertex(nombre2) #metrica 3

    cuatro.add_vertex(nombre1)   #se crean los vertices de las paginas
    cuatro.add_vertex(nombre2) #metrica 4
    
    cinco.add_vertex(nombre1,color="blue")  # se crean los vertices de las paginas
    cinco.add_vertex(nombre2,color="blue")   #metrica 5

    bst_post1=dict() #se crean diccionarios de las distintas paginas
    bst_post2=dict() 

    for num in range(12):   #aqui se agregan los vertices por mes a cada pagina de facebook
	uno.add_vertex(str(num),color="green")
	uno.add_edge(str(num),nombre1,color="green",size=10)
	dos.add_vertex(str(num))
	dos.add_edge(str(num),nombre1)
	tre.add_vertex(str(num))
	tre.add_edge(str(num),nombre1)
	cuatro.add_vertex(str(num))
	cuatro.add_edge(str(num),nombre1)

    for num in range(12,24):
	uno.add_vertex(str(num),color="green")
	uno.add_edge(str(num),nombre2,color="green",size=10)
	dos.add_vertex(str(num))
	dos.add_edge(str(num),nombre2)
	tre.add_vertex(str(num))
	tre.add_edge(str(num),nombre2)
	cuatro.add_vertex(str(num))
	cuatro.add_edge(str(num),nombre2)


    for post in data1:
        nombre = str(data1.index(post))  #el nombre del vertice sera su indice
        if post["created_time"]>date:# aqui se pide si hay mensaje o no
	    if "message" in post.keys():
	        bst_post1[post["id"]]=[0,post["type"],post["message"]]
	    if "message" not in post.keys():
	        bst_post1[post["id"]]=[0,post["type"],"Sin mensaje"]
            year1,mes1=int(post["created_time"].split("-")[0]),int(post["created_time"].split("-")[1])
            year2=year1-year
            if year2==0:     #aqui se calculan los meses de diferencia entre el post y la fecha de hace un anho
                meses_dif=mes1-mes
            if year2==1:
                meses_dif=mes1+2
            posts1[meses_dif]+=1   #se suma 1 al nro de posts segun el mes que corresponde
            uno.add_vertex(post["id"],color="red")        #se crean los vertices y los unen a sus respectivas paginas
	    uno.add_edge(post["id"],str(meses_dif),color="red",size=50)
	    ppl_lk=set()
            ppl_cmt=set()
	    if "shares" in post.keys():
	        share1[meses_dif]+=post["shares"]["count"]
	        cuatro.add_vertex(post["id"],color="blue") #falta agregar peso a los vertices de shares
	        cuatro.add_edge(post["id"],str(meses_dif),color="blue")
	    if "likes" in post.keys():
	        if "total_count" in post["likes"]["summary"].keys():
		    dos.add_vertex("l"+post["id"],size=int(post["likes"]["summary"]["total_count"]/10),color="yellow")
		    dos.add_edge("l"+post["id"],str(meses_dif),color="yellow")
		    bst_post1[post["id"]][0]+=int(post["likes"]["summary"]["total_count"])
                    lkncom1[meses_dif][0]+=int(post["likes"]["summary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
	        for likes in post["likes"]["data"]:
                    ppl_lk.add(likes["id"])    #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
	    if "comments" in post.keys():
	        if "total_count" in post["comments"]["summary"].keys():
		    dos.add_vertex("c"+post["id"],size=int(post["comments"]["summary"]["total_count"]/10),color="green")
		    dos.add_edge("c"+post["id"],str(meses_dif),color="green")
                    lkncom1[meses_dif][1]+=int(post["comments"]["summary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
	        for comment in post["comments"]["data"]:
                    ppl_cmt.add(comment["from"]["id"])     #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
            ppl1[meses_dif]+=len(ppl_lk&ppl_cmt)
	    for personas in ppl_lk&ppl_cmt:
	        tre.add_vertex(personas,color="red")
	        tre.add_edge(personas,str(meses_dif,),color="red")
        
        else:
            pass
    for post in data2:
        nombre = str(data2.index(post))  #el nombre del vertice sera su indice
        if post["created_time"]>date:
	    if "message" in post.keys():
	        bst_post2[post["id"]]=[0,post["type"],post["message"]]
	    if "message" not in post.keys():
	        bst_post2[post["id"]]=[0,post["type"],"Sin mensaje"]
            year1,mes1=int(post["created_time"].split("-")[0]),int(post["created_time"].split("-")[1])
            year2=year1-year
            if year2==0:     #aqui se calculan los meses de diferencia entre el post y la fecha de hace un anho
                meses_dif=mes1-mes
            if year2==1:
                meses_dif=mes1+2
            posts2[meses_dif]+=1   #se suma 1 al nro de posts segun el mes que corresponde
            uno.add_vertex(post["id"],color="red")        #se crean los vertices y los unen a sus respectivas paginas
	    uno.add_edge(post["id"],str(meses_dif+12),color="red",size=50)
	    ppl_lk=set()
            ppl_cmt=set()
	    if "shares" in post.keys():
	        share2[meses_dif]+=post["shares"]["count"]
	        cuatro.add_vertex(post["id"],color="blue")		#falta agregar peso a los vertices de shares
	        cuatro.add_edge(post["id"],str(meses_dif+12),color="blue")
	    if "likes" in post.keys():
	        if "total_count" in post["likes"]["summary"].keys():
		    dos.add_vertex("l"+post["id"],size=int(post["likes"]["summary"]["total_count"]/10),color="yellow")
		    dos.add_edge("l"+post["id"],str(meses_dif+12),color="yellow")
		    bst_post2[post["id"]][0]+=int(post["likes"]["summary"]["total_count"])
                    lkncom2[meses_dif][0]+=int(post["likes"]["summary"]["total_count"])  #aca accede directamente a los likes y los agrega al contador
	        for likes in post["likes"]["data"]:
                    ppl_lk.add(likes["id"])  #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
	    if "comments" in post.keys():
	        if "total_count" in post["comments"]["summary"].keys():
		    dos.add_vertex("c"+post["id"],size=int(post["comments"]["summary"]["total_count"])/10,color="green")
		    dos.add_edge("c"+post["id"],str(meses_dif+12),color="green")
                    lkncom2[meses_dif][1]+=int(post["comments"]["summary"]["total_count"])  #aca accede directamente a los comments y los agrega al contador
	        for comment in post["comments"]["data"]:
                    ppl_cmt.add(comment["from"]["id"])      #se ocupa el id por que en la tercera metrica hay nombres que tiene letras no ascii 
            ppl2[meses_dif]+=len(ppl_lk&ppl_cmt)    #se obtiene la interseccion de la gente que comento y dio like al mismo tiempo
            for personas in ppl_lk&ppl_cmt:
	        tre.add_vertex(personas,color="green")
	        tre.add_edge(personas,str(meses_dif+12),color="green")
        else:
            pass
    best1=[0,"",""]
    best2=[0,"",""]
    for ident,lista in bst_post1.items():    #aqui a partir del diccionario de posts y sus likes, se obtienen los posts con mas likes en el año
        if lista[0]>best1[0]:
	    best1[0]=lista[0]
	    best1[1]=lista[1]
	    best1[2]=lista[2]
    for ident,lista in bst_post2.items():
        if lista[0]>best2[0]:
	    best2[0]=lista[0]
	    best2[1]=lista[1]
	    best2[2]=lista[2]
    cinco.add_vertex("post1",color="yellow")   # se crea el grafo de la metrica 5, que en realidad solo resalta el tamaño del numero de likes de los mejores posts por año
    cinco.add_vertex("post2",color="yellow")
    cinco.add_edge("post1",nombre1,size=int(best1[0]))
    cinco.add_edge("post2",nombre2,size=int(best2[0]))
    uno.write_gml("unom.gml")
    dos.write_gml("dos.gml")
    tre.write_gml("tre.gml")
    cuatro.write_gml("cuatro.gml")
    cinco.write_gml("cinco.gml")
    return posts1,posts2,lkncom1,lkncom2,ppl1,ppl2,share1,share2,best1,best2,uno,dos,tre,cuatro,cinco
    # por cada post hay un key de ["likes"] y ["comments"]
def ver(grafo):
    plot(grafo)
def ventana2(lista):    #crea una nueva ventana con los mejores posts del año, junto con sus respectivos likes al final
    mejor_post= Tk()
    mejor_post.geometry("800x800")
    display=""
    for letra in lista[2]:
        if ((lista[2].index(letra))%40)==0:
	    display+="\n"
        display+=letra
    texto = Label(mejor_post,text=display).pack()
    mg = Label(mejor_post,text=str(lista[0])).pack()

def Cargar_archivo():    # cada vez que se carga un archivo .json, rellena la tabla de datos con los respectivos datos que corresponden por mes y segun metrica
    global posts1,posts2,lkncom1,lkncom2,ppl1,ppl2,share1,share2,best1,best2,uno,dos,tre,cuatro,cinco
    archivo1= askopenfilename()
    archivo2= askopenfilename()
    posts1,posts2,lkncom1,lkncom2,ppl1,ppl2,share1,share2,best1,best2,uno,dos,tre,cuatro,cinco=estadistica(archivo1,archivo2)
    for x in range(12):
	label = Label(ventana, text=posts1[x]).grid(row=3,column=x+2)
	label = Label(ventana, text=posts2[x]).grid(row=4,column=x+2)
	label = Label(ventana, text=lkncom1[x]).grid(row=5,column=x+2)
	label = Label(ventana, text=lkncom2[x]).grid(row=6,column=x+2)
	label = Label(ventana, text=ppl1[x]).grid(row=7,column=x+2)
	label = Label(ventana, text=ppl2[x]).grid(row=8,column=x+2)
	label = Label(ventana, text=share1[x]).grid(row=9,column=x+2)
	label = Label(ventana, text=share2[x]).grid(row=10,column=x+2)
    mejor1= Button(ventana,text="Mejor post 1", command=ventana2(best1)).grid(row=12,column=5)
    mejor2= Button(ventana,text="Mejor post 2", command=ventana2(best2)).grid(row=12,column=6)

    plt1= Button(ventana,text="Grafo 1", command=ver(uno)).grid(row=11,column=5)
    plt2= Button(ventana,text="Grafo 2", command=ver(dos)).grid(row=11,column=6)
    plt3= Button(ventana,text="Grafo 3", command=ver(tre)).grid(row=11,column=7)
    plt4= Button(ventana,text="Grafo 4", command=ver(cuatro)).grid(row=11,column=8)
    plt5= Button(ventana,text="Grafo 5", command=ver(cinco)).grid(row=11,column=9)
    

    #bst1= Label(ventana, text=best1[2]).pack()
    #bst2= Label(ventana, text=best2[2]).pack()


ventana = Tk()
ventana.geometry("1000x800")
cargar = Button(ventana,text="Cargar", command=Cargar_archivo).grid(row=1,column=6)


blank = Label(ventana, text="      ").grid(row=2,column=1)   # estas son todas las labels que ayudan a identificar los datos en la tabla de datos 
mes1 = Label(ventana, text="Enero ").grid(row=2,column=2)
mes2 = Label(ventana, text="Febrero ").grid(row=2,column=3)
mes3 = Label(ventana, text="Marzo ").grid(row=2,column=4)
mes4 = Label(ventana, text="Abril ").grid(row=2,column=5)
mes5 = Label(ventana, text="Mayo ").grid(row=2,column=6)
mes6 = Label(ventana, text="Junio ").grid(row=2,column=7)
mes7 = Label(ventana, text="Julio ").grid(row=2,column=8)
mes8 = Label(ventana, text="Agosto ").grid(row=2,column=9)
mes9 = Label(ventana, text="Septiembre ").grid(row=2,column=10)
mes10 = Label(ventana, text="Octubre ").grid(row=2,column=11)
mes11 = Label(ventana, text="Noviembre ").grid(row=2,column=12)
mes12 = Label(ventana, text="Diciembre ").grid(row=2,column=13)
post1 = Label(ventana, text="Post 1 ").grid(row=3,column=1)
post2 = Label(ventana, text="Post 2 ").grid(row=4,column=1)
laik1 = Label(ventana, text="Likes y comentarios 1").grid(row=5,column=1)
laik2 = Label(ventana, text="Likes y comentarios 2").grid(row=6,column=1)
personas1 = Label(ventana, text="Personas activas 1").grid(row=7,column=1)
personas2 = Label(ventana, text="Personas activas 2").grid(row=8,column=1)
share1 = Label(ventana, text="Shares 1").grid(row=9,column=1)
share2 = Label(ventana, text="Shares 2").grid(row=10,column=1)





ventana.mainloop()







#para el grafo    
#g = Graph()
#g.add_vertex(nombre_vertice)
#g.add_vertex(nombre_vertice, tipo=tipo1)
#g.add_edge(vertice1,vertice2)
#g.add_edge(vertice1,vertice2,peso=2.5)


