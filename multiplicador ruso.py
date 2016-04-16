print"Multiplicador Ruso"
multiplicador=int(raw_input("Digite el multiplicador    "))
multiplicando=int(raw_input("Digite el multiplicando    "))
R=0
a=multiplicador
b=multiplicando
if a%2!=0:
    R=R+b
    print a, b
while a!=1:
    a=a/2
    b=b*2
    a2=a%2
    print a, b
    if a2!=0:
        R=R+b
print "Resultado", R
