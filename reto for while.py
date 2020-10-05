#Creador: Monse Galvan A00344712
#Creador: Paola Gomez
#Creador: Lydia 
#Juego para practicar calculo mental
#Librerias
import random
#Funciones
def suma():
    print("Ejercicios de suma")
    puntaje  =0
    nivel2=5
    for i in range(0,nivel2):
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        suma = num1 +num2
        respuesta = int(input(f" el resultado de {num1} + {num2}:  "))
        if respuesta == suma: #Verifica si el resultado es correcto
            puntaje +=1
            print("Respuesta correcta")
            print("")
        else:
            print("respuesta incorrecta")
            print("")
        if puntaje >= 5:#Si alcanza 5 puntos avanza al nivel 2
            print("Nivel 2")
            for i in range(0,5):
                
                num1 = random.randint(1,9)
                num2 = random.randint(10,99)
                suma = num1 +num2
                respuesta = int(input(f"El resultado de sumar {num1} + {num2}: "))
                if respuesta == suma:
                    puntaje +=1
                    print("Respuesta correcta")
                    print("")
                else:
                    print("Respuesta inc0rrecta")
                    print("")
                if puntaje ==10: #Acierta 10 veces en total y psas al salon
                    print(f"Felicidades {nombre} acertaste 10 veces, estas en el salon de la fama")
                    print("")
                
def resta():
    print("Ejercicios de resta")
    for i in range(0,5):
        num1 = random.randint(1,99)
        num2 = random.randint(1,99)
        resta = num1-num2
        respuesta = int(input(f"El resultado de restar {num1} - {num2}:  "))
        while respuesta != resta:#No deja avanzar hasta que la respuesta sea correcta
            print("Respuesta incorrecta, intenta de nuevo")
            print("")
            respuesta = int(input(f"El resultado de restar {num1} - {num2}:  "))
            
def mult():
    print("Ejercicios de multiplicacion")
    aciertos = 0
    for h in range(0,10):
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        multi = num1* num2
        respuesta = int(input(f" el resultado de {num1} * {num2}: "))
        if respuesta == multi:
             print("Respuesta correcta")
             print("")
             aciertos+=1#Guarda el total de aciertos
        else:
            print("Respuesta incorrecta")
            print("")
    print(f"Total de aciertos {aciertos}")        
    
#Programa principal
nombre = input("Ingresa tu nombre: ")#Pide el nombre del uisuario
print("")
print(f"Bienvenido {nombre}")
menu = 0

while menu!="4":#Despliega el menu
    menu = input("""Escoge una opcion: 
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Salir
            """)
    if menu == "1":
        suma()
    elif menu =="2":
        resta()
    elif menu =="3":
        mult()
    elif menu == "4":
        print(f"Gracias por jugar {nombre}")
    else:
        print("Opcion no valida")
        
            
    


    
    
    