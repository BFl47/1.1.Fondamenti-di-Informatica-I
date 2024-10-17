##n=int(input('inserire un numero intero maggiore di 0: '))
##i=0
##n1=1
##print(n1)
##n2=1
##
##if n>=0:
##    print(n1)
##while i<n-2:
##    somma=n1+n2
##    print(somma)
##    n1=n2
##    n2=somma
##    i+=1

##n=int(input('Inserisci un numero intero positivo: '))
##
##prec=1
##print(prec)
##if n>1:
##    ultimo=1
##    print(ultimo)
##
##i=3
##while (i<=n):
##    nuovo=prec+ultimo
##    prec=ultimo
##    ultimo=nuovo
##    i+=1
##    print(nuovo)

n=int(input('intero: '))
n1=1
print(n1)
n2=1
i=0
if n>=0:
    print(n1)
while i<n-2:
    somma=n1+n2
    print(somma)
    n1=n2
    n2=somma
    i+=1
