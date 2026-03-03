# Mayusculas - numeros - caracteres esp. - longitud 8 caracteres

"""mayusculas = False
numeros = False
caracteres = False
simbolos = "@$_"
print("Crea una contraseña con mayusculas - numeros - caracteres esp. - longitud 8 caracteres")

while True:

    contraseña = str(input("INGRESE SU CONTRASEÑA: "))
    
    if len(contraseña) > 8:
        caracteres = True

    for c in contraseña:
        if c.isupper():
            mayusculas = True
        if c.isdigit():
            numeros = True
        if c in simbolos:
            simbolos = True
        

    if mayusculas == True :
        print("MAYUSCULAS = OK")
    else:
        print("MAYUSCULAS = NO")
    if numeros == True:
        print("NUMEROS = OK")
    else:
        print("NUMEROS = NO")
    if caracteres == True:
        print("CARACTERES = OK")
    else:
        print("CARACTERES = NO")
    if simbolos == True:
        print("SIMBOLOS = OK")
    else:
        print("SIMBOLOS = NO")

    if (simbolos and caracteres and numeros and mayusculas) == True:
        print("CREASTE UNA CONTRASEÑA CORRECTA")
        break
"""


while True:
    correo= str(input("Coloca tu correo: "))

    correo_valido = None

    partes = correo.split("@")    
    dominio = partes[1].split(".")

    if correo.startswith("@"):
        correo_valido = False
    if len(partes) != 2:
        correo_valido = False
    if len(dominio) < 2:
        correo_valido = False

    for part in partes + dominio:
        if not partes:
            correo_valido = False


    if correo_valido == False:
        print("Correo invalido, intente de nuevo") 
    else:
        print("Correo valido")
        break

