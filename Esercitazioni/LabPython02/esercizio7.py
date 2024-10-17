##m=int(input('Inserisci il mese: '))
##a=int(input('Inserisci l\'anno: '))
##
##if 1<=m<=12:
##    if m<=11:
##        print(m+1,a)
##    elif m==12:
##        print('1',a+1)
##else:
##    print('Input non valido')

m=int(input('mese: '))
a=int(input('anno: '))

if 1 <= m <= 12:
    if m == 12:
        print('1',a+1)
    else:
        print(m+1,a)
else:
    print('input non valido')
