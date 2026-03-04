
try:
    print("==============================")
    print("=====Tabla de multiplicar=====")
    print("==============================")

    numero = int(input("Coloque el numero a multuplicar: "))
    numero_tabla = int(input("Coloque el numero hasta donde quieres que se muestre la tabla de multiplicar: "))

    for i in range (1, numero_tabla+1):
        print(f"{numero} x {i} = {numero*i}")
        
except ValueError:
    print("solo puedes colocar numeros")