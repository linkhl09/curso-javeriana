n=int(raw_input("Cuantos datos necesita?"))
lista=[]
nombres=[]
for x in range (0,n):
    l=int(raw_input("años de la pesona"))
    lista.append(l)
for x in range (0,n):
    a=raw_input("Nombres de la persona")
    nombres.append(a)
p=0
y=0
for m in range (n):
    if lista[m]>y:
        y=lista[m]
        p=m
print nombres[p]
        


