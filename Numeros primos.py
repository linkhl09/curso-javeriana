print "Calcular si un numero es primo"
num=int(raw_input("Digite el numero que desea analizar   "))
if num !=0:
    for x in range (2, num):
        if num%x == 0:
            print num, "es igual a", x, "*", num/x
            break
        else:
            print num, "es un numero primo"
            break
else: print "Numero no valido"
