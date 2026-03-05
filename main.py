"""
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
"""
    ##################################################
import time

print("""      ==========================================
      =======REGISTRO DE ESTUDIANTES RIWI=======
      ==========================================""")

try:


    cantidad_estudiantes= int(input("¿CUANTOS ESTUDIANTES HAY?: "))
    promedio_general = 0
    estudiantes_aprobados = 0
    estudiantes_reprobados = 0
    
    for estudiantes in (1, cantidad_estudiantes+1):

        estudiante = str(input("\nINGRESE SU NOMBRE: "))

        nota1 = float(input("INGRESE LA PRIMERA NOTA: "))
        nota2 = float(input("INGRESE LA SEGUNDA NOTA: "))
        nota3 = float(input("INGRESE LA TERCERA NOTA: "))

        while True:
            if nota1>5 or nota2>5 or nota3 >5:
                print("\n¡No se admiten notas mayores a 5!")
                nota1 = float(input("INGRESE LA PRIMERA NOTA: "))
                nota2 = float(input("INGRESE LA SEGUNDA NOTA: "))
                nota3 = float(input("INGRESE LA TERCERA NOTA: "))
                
            else:
                False
                break
            

        promedio_estudiante = round((nota1+nota2+nota3)/3 ,1)
        

        if promedio_estudiante>=3:
            print("Calculando promedio...")
            time.sleep(1)
            print(f"El estudiante {estudiante} tiene un promedio de {promedio_estudiante} - ¡Has aprobado!")
            estudiantes_aprobados += 1
            promedio_general += promedio_estudiante
            time.sleep(2)
            
            

        elif promedio_estudiante<3:
            print("Calculando promedio...")
            time.sleep(1)
            print(f"El estudiante {estudiante} tiene un promedio de {promedio_estudiante} - ¡Has reprobado!")
            estudiantes_reprobados += 1
            promedio_general += promedio_estudiante
            time.sleep(2)
    
    print(f"\nHay un total de {cantidad_estudiantes} estudiantes.")
    print(f"{estudiantes_aprobados} estudiantes aprobados y {estudiantes_reprobados} estudiantes reprobados")
    print(f"con un promedio general de {promedio_general/cantidad_estudiantes}")
    time.sleep(2)



except ValueError:
    print("Coloque el valor pedido, solo numeros o solo letras")




