segundos=int(input())
horas,min=0,0
if segundos>=3600:
    horas=segundos//3600
segundos-=horas*3600
if segundos>=60:
    min=segundos//60
segundos-=min*60
print(horas,min,segundos)