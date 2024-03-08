temperature=input("")
if int(temperature)>30:
    print("it's hot")
elif int(temperature)<10:
    print("it's cold")
else:
    print("it's ok")
if int(temperature)>=100:
    print("water would boil")
elif int(temperature)<=0:
    print("water would freeze")