def crear():
    lista=[]
    suma=0
    for x in range (1,100+1):
        lista.append(x)
    for x in lista:
     suma += x
    promedio=suma / len(lista)
    print(promedio)
    print(lista)
crear()

#-----------------------------------------------------------------------
