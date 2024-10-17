##s=input('inserire un numero intero: ')
##somma=0
##while s!='*':
##    n=int(s)
##    if n<0:
##        somma=somma+n
##    s=input('inserire un numero intero: ')
##print(somma)

n=input('intero: ')
somma=0
while n!='*':
    n=int(n)
    if n<0:
        somma+=n
    n=input('intero: ')
print(somma)
