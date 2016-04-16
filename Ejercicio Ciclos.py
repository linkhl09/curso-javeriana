print "Ejercicio de ciclos -Granizada-"
def par(n):
    n=n/2
def impar(n):
    n=n*3+1
n=int(raw_input("digite numero   "))
while n>=1:
    if n%2==0:
        par(n)
        print n   
    else:
        impar(n)
        print n
