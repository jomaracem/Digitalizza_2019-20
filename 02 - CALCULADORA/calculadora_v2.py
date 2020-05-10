#!"C:\Users\CISCO\AppData\Local\Programs\Python\Python38-32\python.exe"
#!/usr/bin/env python3

########################################################################
##  Proyecto: Calculadora para curso DEVNET - Beca CISCO              ##
##  Alumno: José Manuel Martín Acemel  - jomaracem@gmail.com          ##
##  Fecha: 20/01/20                                                   ##
########################################################################
"""
FUNCIONES OBLIGATORIAS DE ESTE SCRIPT (CALCULADORA):
    - Calculadora (es una tarea a la que le añadiremos más funcionalidades)
    - Crear un menú que indique las opciones que hay 
    - Como mínimo, incluir: 
        OK - suma, 
        OK - resta, 
        OK - multiplicación, 
        OK - división, 
        OK - exponenciales
        OK - raíces cuadradas. 
        OK - Se pueden añadir más funcionalidades.
        OK - Podéis usar las funciones y técnicas vistas en las sesiones, o implementar otras que consideréis oportunas. Obviamente, ser eficientes tendrá más nota.
"""
## TITULO:
print("\n")
print("     "+70*"*")
print("     **   ","C","A","L","C","U","L","A","D","O","R","A","    **",sep="    ")
print("     "+70*"*")
## DESCRIPCIÓN:
print("\n     - Este script realiza operaciones de calculo. Elija una opción y siga las instrucciones.\n")
## TABLA DE OPCIONES POR PANTALLA:
print("\n\n     OPERACIONES :\n\n     1-SUMAR\n     2-MULTIPLICAR\n     3-RESTAR\n     4-DIVIDIR\n     5-RAIZ CUADRADA\n     6-CONVERSOR DECIMAL/BINARIO\n     7-EXPONENCIAL\n     0-FIN CALCULADORA")
print("     "+70*"_"+"\n")
# OPERACIONES:
def suma():
    innum1=input("     Introduzca el primer número para sumar: ")
    num1=innum1.replace(",",".")
    innum2=input("     Introduzca el segundo número para sumar: ")
    num2=innum2.replace(",",".")
    print("     El resultado de sumar",num1,"mas",num2,"es", float(num1)+float(num2))
    print("     "+50*"_"+"\n")
    return
def multiplicacion():
    innum1=input("     Introduzca el primer número para multiplicar: ")
    num1=innum1.replace(",",".")
    innum2=input("     Introduzca el segundo número para multiplicar: ")
    num2=innum2.replace(",",".")
    print("     El resultado de multiplicar",num1,"por",num2,"es", float(num1)*float(num2))
    print("     "+50*"_"+"\n")
    return
def exponencial():
    innum1=input("     Introduzca la base: ")
    num1=innum1.replace(",",".")
    innum2=input("     Introduzca el exponente: ")
    num2=innum2.replace(",",".")
    print("     El resultado de elevar",num1,"al exponente",num2,"es", float(num1)**float(num2))
    print("     "+50*"_"+"\n")
    return
def raiz_cuadrada():
    innum=input("     Raíz cuadrada de: ")
    num=innum.replace(",",".")
    n2= float(num)**(0,5)
    print("     La raiz cuadrada de "+str(num)+" es: "+str(n2))
    print("     "+50*"_"+"\n")
    return
def resta():
    innum1=input("     Introduzca el primer número para restar: ")
    num1=innum1.replace(",",".")
    innum2=input("     Introduzca el segundo número para restar: ")
    num2=innum2.replace(",",".")
    print("     El resultado de restar ",num1,"menos",num2,"es", float(num1)-float(num2))
    print("     "+50*"_"+"\n")
    return
def division():
    innum1=input("     Introduzca el primer número para dividir: ")
    num1=innum1.replace(",",".")
    innum2=input("     Introduzca el segundo número para dividir: ")
    num2=innum2.replace(",",".")
    try: 
        print("     El resultado de dividir",num1,"entre",num2,"es", float(num1)/float(num2))
        print("     "+50*"_"+"\n")
    except ZeroDivisionError:
        print("\n"+"     No se puede divivir entre 0, vuelve a intentarlo")
        division()
    return
def conv_binary():
    print("     1 - Convertir un número decimal a binario.\n     2 - Convertir un número binario a decimal.")
    conv=input("     Intrduzca el número de la opción que desea realizar y pulse enter: ")
    if conv==("1"):
        num1=int(input("     Introduzca un número decimal: "))
        print("     El número", num1, "en binario es: ", str(bin(num1)[2:]))
        print("     "+50*"_"+"\n")
    elif conv==("2"):
        num1=str(input("     Introduzca un número binario: "))
        print("     El número", num1, "en decimal es: ", int(num1,2))
        print("     "+50*"_"+"\n")
    else:
        print("\n     Tiene que elegir entre las opciones 1 y 2\n     Vuelva a intentarlo")
        conv_binary()
    return
# OPCIONES CABECERA:
def cabecera():
    operador=int(input("     Elija el número de la operación con la que desea operar y pulse intro: "))
    if(operador==0):
       exit
       print("Calculadora finalizada\nSAYONARA BABY")
    elif(operador==1):
        suma()
        cabecera()
    elif(operador==2):
        multiplicacion()
        cabecera()
    elif(operador==3):
        resta()
        cabecera()
    elif(operador==4):
        division()
        cabecera()
    elif(operador==5):
        raiz_cuadrada()
        cabecera()
    elif(operador==6):
        conv_binary()
        cabecera()
    elif(operador==7):
        exponencial()
        cabecera()
cabecera()
