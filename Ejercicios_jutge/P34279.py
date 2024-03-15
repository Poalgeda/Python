var=input().split()
hora=int(var[0])
minuto=int(var[1])
segundo=int(var[2])
segundo+=1

if segundo>=60:
    minuto+=1
    segundo="00"
if minuto>=60:
    hora+=1
    minuto="00"
if hora>=24:
    hora="00"
if int(segundo)<10 and segundo!="00": 
    segundo=f"0{segundo}"
if int(minuto)<10 and minuto!="00": 
    minuto=f"0{minuto}"
if int(hora)<10 and hora!="00": 
    hora=f"0{hora}"
print(f"{hora}:{minuto}:{segundo}")