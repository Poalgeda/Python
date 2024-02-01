
listanom=[]
listaedad=[]
listapes=[]
listaaltu=[]

respuesta="s"

while respuesta=="s":
    nom=input("Introduce el nombre una persona: ")
    edad=int(input("Introduce la edad de la persona en años: "))
    peso=float(input("Introduce el peso de la persona en kilos: "))
    altura=float(input("Introduce la altura en metros: "))

    listanom.append(nom)
    listaedad.append(edad)
    listapes.append(peso)
    listaaltu.append(altura)

    respuesta=input("Deseas añadir otra persona? s/n ")


respuesta=input("Deseas buscar a una persona? s/n ")
while respuesta=="s":
    buscar=input("Introduce el nombre de la persona: ")
    encontrado=listanom.count(buscar)
    if encontrado>0:
        indice=listanom.index(buscar)
        print(f"la edad de {listanom[indice]} es ",listaedad[indice])
        print(f"{buscar} no esta en la lista.")
    else:
        print("Esta persona no esta en la lista.")
        respuesta=input("Quieres buscar a otra persona? s/n ")


