carta = "Estos son los productos que tenemos:\n\
   1. Papas fritas (1200)\n\
   2. Sandwcih combinado (2500)\n\
   3. Pescadito (1800)\n\
   4. Empanada (1700)\n\
   5. Arepa (2000)\n\
   6. Gaseosa (1600)\n\
   7. Vaso de Te (1000)\n\
   8. Dulce (200)\n\
   si desea reembolsar su dinero oprima 9."
final = "dinero insuficiente o excedido, retornando el dinero ingresado.\n\
       Se han devuelto"
final9 = "Su dinero ha sido reembolsado.\n\
Valor:"
print "Buenos dias"
print "Solo se reciben monedas de 100, 200, 500"
print "Valor minimo: 200 Valor maximo:2500"
print"Insete su dinero"
a=int(raw_input("monedas de 100:  "))
b=int(raw_input("monedas de 200:  "))
c=int(raw_input("monedas de 500:  "))
a2=a*100
b2=b*200
c2=c*500
d=a2+b2+c2
if d >= 200 and d<=2500:
    print carta
    print "Su saldo es:", d
    p=int(raw_input("Que desea ordenar?"))
    if p>=1 and p<=9:
        if p ==1:
            print "A seleccionado Papas fritas"
            if d>=1200:
                v = d-1200
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p ==2:
            print "A seleccionado Sandwich combinado"
            if d>=2500:
                print "Tome su producto"
            else:print "su saldo es insuficiente"
        if p ==3:
            print "A seleccionado Pescadito"
            if d>=1800:
                v = d-1800
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 4:
            print "A seleccionado Empanada de Carne"
            if d>=1700:
                v = d-1700
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 5:
            print "A seleccionado Arepa"
            if d>=2000:
                v = d-2000
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 6:
            print "A seleccionado Gaseosa"
            if d>=1600:
                v = d-1600
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 7:
            print "A seleccionado Vaso de Te"
            if d>=1000:
                v = d-1000
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 8:
            print "A seleccionado Dulce"
            if d>=200:
                v = d-200
                print "Tome su producto"
                print "Su cambio es:", v
            else:print "su saldo es insuficiente"
        if p == 9:
            print final9, d
    else:print"opcion invalida"
else: print final, d
