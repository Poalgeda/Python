#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos

alumno="s"
cata=[]
caste=[]
ingles=[]
media_cata=0
media_caste=0
media_ingles=0
alumnos=0
media_cata2=0
media_caste2=0
media_ingles2=0
#con este while introduzco los valores de cada alumno.63.
while alumno=="s":
    nombre=input("Introduce usuario: ")
    x1=int(input("Nota Catalán: "))
    cata+=str(x1).split()
    media_cata+=x1
    media_cata2+=1
    x2=int(input("Nota Castellano: "))
    caste+=str(x2).split()
    media_caste+=x2
    media_caste2+=1
    x3=int(input("Nota Inglés: "))
    ingles+=str(x3).split()
    media_ingles+=x3
    media_ingles2+=1
    alumno=input("Quieres introducir otro alumno? s/n ")
    #la siguiente variable es para que cuando solo se ha registrado un alumno (y por tanto una nota de cada asignatura), no haga la media aritmetica ya que solo hay una nota.
    alumnos+=1
#------------medianas------------
#catalan
cata.sort()
if len(cata) >1:
    mitad = len(cata)/2
    if len(cata) % 2 == 0:
        mediana_cata = (int(cata[int(mitad) - 1])+int(cata[int(mitad)])) / 2
    else:
        mediana_cata = cata[int(mitad)]
else:
    mediana_cata=cata[0]
#castellano
caste.sort()
if len(caste) >1:
    mitad = len(caste)/2
    if len(caste) % 2 == 0:
        mediana_caste = (int(caste[int(mitad) - 1])+int(caste[int(mitad)])) / 2
    else:
        mediana_caste = caste[int(mitad)]
else:
    mediana_caste=caste[0]
#ingles
ingles.sort()
if len(ingles) >1:
    mitad = len(ingles)/2
    if len(ingles) % 2 == 0:
        mediana_ingles = (int(ingles[int(mitad) - 1])+int(ingles[int(mitad)])) / 2
    else:
        mediana_ingles = ingles[int(mitad)]
else:
    mediana_ingles=ingles[0]
#----------medias----------
if alumnos!=1:
    media_cata=round(media_cata/media_cata2, 1)
    media_caste=round(media_caste/media_caste2, 1)
    media_ingles=round(media_ingles/media_ingles2, 1)
else:
    None


print(f"Catalán: {cata}")
print(f"Castellano: {caste}")
print(f"Inglés: {ingles}")
print(f"La Media en catalán es: {media_cata}")
print(f"La Media en castellano es: {media_caste}")
print(f"La Media en ingles es: {media_ingles}")
print(f"La Mediana en catalan es: {mediana_cata}")
print(f"La Mediana en castellano es: {mediana_caste}")
print(f"La Mediana en ingles es: {mediana_ingles}")
