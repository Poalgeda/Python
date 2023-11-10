

var="2rt4W"
var_num=0
var_letra=0

for var_recorrer in var:
    if var_recorrer.isnumeric():
        var_num+=1
    else:
        var_letra+=1


print("numeros: ", var_num)
print("letras",var_letra)