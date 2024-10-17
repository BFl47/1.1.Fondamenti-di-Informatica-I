##n=int(input('inserire un numero intero: '))
##somma=0
##while n!=0:
##    if n%3==0:
##        somma=somma+n
##    n=int(input('inserire un numero intero: '))
##print(somma)

n=int(input('intero: '))
somma=0
while n!=0:
    if n%3==0:
        somma+=n
    n=int(input('intero: '))
print(somma)
