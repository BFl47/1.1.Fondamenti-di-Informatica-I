##n1=int(input('inserire un numero intero: '))
##n2=int(input('inserire un numero intero: '))
##entrambineg=False
##if n1<0 and n2<0:
##    n1=-n1
##    n2=-n2
##    entrambineg=True
##n=min(n1,n2)
##salto=max(n1,n2)
##somma=0
##i=0
##
##while i<salto:
##    somma=somma+n
##    i+=1
##if entrambineg:
##    print(-somma)
##else:
##    print(somma)


##n1=int(input('inserire un numero intero: '))
##n2=int(input('inserire un numero intero: '))
##
##abs1=abs(n1)
##abs2=abs(n2)
##prodotto=0
##i=0
##
##while i<abs1:
##    prodotto += abs2
##
##if ((n1>0) and (n2>0)) or ((n1<0) and (n2<0)):
##    print(prodotto)
##else:
##    print(-prodotto)

n1=int(input('intero 1: '))
n2=int(input('intero 2: '))

abs1=abs(n1)
abs2=abs(n2)
prodotto=0
i=0
while i<abs1:
    prodotto+=abs2
    i+=1
if (n1*n2)>0:
    print(prodotto)
else:
    print(-prodotto)
















