#Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones:
print("Debe tener una longitud entre 8 y 10 caracteres. ")
print("Debe contener como mínimo: ")
print("2 números mayores o iguales que 1 y menor o igual que 5 ")
print("2 letras minúsculas ")
print("1 letra mayúscula ")
print("2 símbolos (*, _, @, &,/,#) ")
print("1 número mayor o igual que 6 y menor o igual que 5")

password=input("Introduce una palabra clave de entre 8 a 10 palabras: ")
req1=0
req2=0
req3=0
req4=0
req5=0
ver_password=True
if len(password) <=10 and len(password) >=8:
    print()
    if len(password) == 8:
        for var_recorrer in password:
            if var_recorrer.isnumeric():
                if int(var_recorrer) >=1 or int(var_recorrer) <=5:
                    req1+=1
                    req5+=1
                elif var_recorrer >=6 or var_recorrer <=5:
                    req5 +=1
            elif var_recorrer.isalpha():
                if var_recorrer.islower():
                    req2+=1
                elif var_recorrer.isupper():
                    req3 +=1
            elif var_recorrer.isascii():
                req4+=1
        if req1 >=2 and req2 >=2 and req3 >=1 and req4 >=2 and req5 >= 1:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
    elif len(password) == 9:
        for var_recorrer in password:
            if var_recorrer.isnumeric():
                if int(var_recorrer) >=1 or int(var_recorrer) <=5:
                    req1+=1
                    req5+=1
                elif var_recorrer >=6 or var_recorrer <=5:
                    req5 +=1
            elif var_recorrer.isalpha():
                if var_recorrer.islower():
                    req2+=1
                elif var_recorrer.isupper():
                    req3 +=1
            elif var_recorrer.isascii():
                req4+=1
        if req1 >=2 and req2 >=2 and req3 >=1 and req4 >=2 and req5 >= 1:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
    elif len(password) ==10:
        for var_recorrer in password:
            if var_recorrer.isnumeric():
                if int(var_recorrer) >=1 or int(var_recorrer) <=5:
                    req1+=1
                    req5+=1
                elif var_recorrer >=6 or var_recorrer <=5:
                    req5 +=1
            elif var_recorrer.isalpha():
                if var_recorrer.islower():
                    req2+=1
                elif var_recorrer.isupper():
                    req3 +=1
            elif var_recorrer.isascii():
                req4+=1
        if req1 >=2 and req2 >=2 and req3 >=1 and req4 >=2 and req5 >= 1:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
         
else:
    print(f"La palabra clave tiene una longitud de {len(password)} y no cumple con los requisitos.")