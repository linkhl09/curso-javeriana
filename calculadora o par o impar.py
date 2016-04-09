print "¿Que deseas el dia de hoy?"
r =     (raw_input("calculadora o, 2 para par o impar"))
if r == "calculadora" or r == "CALCULADORA" or r == "Calculadora":
    print "¿que operacion desea hacer?"
    r2 = (raw_input("suma, resta, multiplicacion o division"))
    if r2 == "suma" or r2 == "Suma" or r2 == "SUMA" or r2 == "+":
        num1 = int(raw_input("Inserte el primer numero"))
        num2 = int(raw_input("Inserte el segudo numero"))
        print "resultado", num1+num2
    if r2 == "resta" or r2 == "Resta" or r2 == "RESTA" or r2 == "-":
        num1 = int(raw_input("Inserte el primer numero"))
        num2 = int(raw_input("Inserte el segudo numero"))
        print "resultado", num1-num2
    if r2 == "multiplicacion" or r2 == "Multiplicacion" or r2 == "MULTIPLICACION" or r2 == "*":
        num1 = int(raw_input("Inserte el primer numero"))
        num2 = int(raw_input("Inserte el segudo numero"))
        print "resultado", num1*num2
    if r2 == "division" or r2 == "Division" or r2 == "divicion" or r2 == "Divicion" or r2 == "DIVISION" or r2 == "/" or r2 == "DIVICION":
        num1 = int(raw_input("Inserte el primer numero"))
        num2 = int(raw_input("Inserte el segudo numero"))
        if num2 != 0:
            print "resultado", num1/num2
        else: print"Indeterminado, preguntale a siri porque."
if r == "2":
    num1 = int(raw_input("Inserte el numero"))
    num2 = num1%2
    if num2 == 0:
        print "es par"
    else: print "es impar"
