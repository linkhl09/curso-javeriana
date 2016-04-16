print "calcular si un numero es primo"
num=int(raw_input("Hasta cual numero?"))
for num in range (2,num+1):
    for x in range (2, num):
        if num%x ==0:
            print num, "es igual a", x, "*", num/x
            break
    else:
        print num, "es primo"

