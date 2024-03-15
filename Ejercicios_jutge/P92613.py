import math

var=float(input(""))

ceil=math.ceil(var)
floor=math.floor(var)
if str(var).split(".")[1]=="5":
    var+=0.1
redondeo=int(round(var,0))
print(floor,ceil,redondeo)