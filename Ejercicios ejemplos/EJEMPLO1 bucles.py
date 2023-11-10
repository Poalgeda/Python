#Variable que almacena la suma
var_total=0
var_opcion=0

print("MENÚ")
print("1.SUMA")
print("2.RESTA")

for cont in range (0,3):
    var_opcion=int(input("Introduce una opción del menú:  "))
    if var_opcion <=0 or var_opcion >=3:
        print("error")
    else:
        var1=int(input("Introduce el primer numero:  "))
        var2=int(input("Introduce el primer numero:  "))
    
    if var_opcion==1:          
        var_total=var1+var2
        
    if var_opcion==2:
        var_total=var1-var2

        print(f"el resultado de la operación {var1} y {var2} es:",var_total)
    else:
        print("ERROR")
