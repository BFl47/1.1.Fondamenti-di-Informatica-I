##d=float(input('Inserisci l\'età del cane: '))
##
##if 0<=d<=2:
##    dog=10.2*d
##    print(dog)
##elif d>2:
##    dog=(10.5)*2+(d-2)*4
##    print(dog)
##else:
##    print('Input non valido')
##
###if dog>=0:
##    #print('Corrispondente età umana:',dog)
###elif dog<0:
##    #print('Input non valido')

dog=float(input('età cane: '))

if 0 <= dog <=2:
    eta=10.2*dog
elif dog > 2:
    eta=(10.5*2)+(dog-2)*4
print(eta)
