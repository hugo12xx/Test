import random




menu=0

    
print ("1.- generar numeros aleatorios \n")
    
print ("2.-ordenar el archivo \n")
print ("3.-buscar un numero \n")
print ("4.-mostrar numeros \n")
print ("0.-para salir \n")
    
    
menu = int(input("elija una opcion del menu: "))


while menu != 0:



    
    if menu==1:
        # se llena prueba.txt con valores random
        f=open ("C:/Users/Hugo/Desktop/name/test/prueba.txt","w")
        cantidad = int(input("cuantos numeros desea generar "))

        x=range(0,cantidad)
    
        ar = [None] * cantidad
    
        for n in x:
            num = random.randint(1, 90)
            texto=str(num)
            f.write(texto+'\n')
            ar[n]=num
       
        
        f.close()
    
    
    
    
    
    if menu==2:
        f2=open ("C:/Users/Hugo/Desktop/name/test/orden.txt","w")

        #ordena los numeros con QuickSort

        def QuickSort(ar, izq, der):
        
            pivote = ar[izq]
            i = izq
            j = der
            aux = 0
        
            while i < j:
                while ar[i] <= pivote and i < j:
                    i += 1
        
                while ar[j] > pivote:
                    j -= 1
        
                if i < j:
                    aux = ar[i]
                    ar[i] = ar[j]
                    ar[j] = aux
        
            ar[izq] = ar[j]
            ar[j] = pivote
        
            if izq < j-1:
                QuickSort(ar,izq,j-1)
        
            if j+1 < der:
                QuickSort(ar,j+1,der)
        
        QuickSort(ar,0,len(ar) - 1)
    
    
        
        #pasa los numeros ordenados a orden.txt
        
        
        
        for n2 in x:
            num = ar[n2]
            texto=str(num)
            f2.write(texto+'\n')
            
    
    
        
    #f.write("hola mundo")
        
       
        f2.close()
       
    
    if menu==3:
        f3=open ("C:/Users/Hugo/Desktop/name/test/busqueda.txt","w")

        #busca un numero
        pregunta=0
        
        
        busqueda = input("Ingresa búsqueda: ")
        lineas_escribir = []
        
        with open("C:/Users/Hugo/Desktop/name/test/prueba.txt", "r") as archivo_lectura:
            numero_linea = 0
            for linea in archivo_lectura:
               
                numero_linea = numero_linea+1
                separado = linea.split('\n')
                
                if busqueda in separado:
                    lineas_escribir.append("en la linea: "+str(numero_linea) + " hay un: " + linea)
        
                    pregunta=1
        
        
        
        
        #escribe el resultado de la busqueda en busqueda.txt
        
        
        
        
        if pregunta==1:
        
            textobusqueda=str(lineas_escribir)
            f3.write(textobusqueda)
        else:
            f3.write('no se encontro el numero')
        
            
           
        
    
        f3.close()
    
    
    if menu==4:
        
        
        f4=open ("C:/Users/Hugo/Desktop/name/test/prueba.txt","r")

        #muestra los datos del archivo prueba.txt   
        

        for linea2 in f4:
               
            print(linea2)
                
           
            
        f4.close()
        
    print ("------------------------------------------- \n")
    print ("1.- generar numeros aleatorios \n")
        
    print ("2.-ordenar el archivo \n")
    print ("3.-buscar un numero \n")
    print ("4.-mostrar numeros \n")
    print ("0.-para salir \n")
        
        
    menu = int(input("elija una opcion del menu: "))
        
    
    
