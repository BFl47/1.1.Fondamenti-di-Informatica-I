##t=float(input('Inserisci un valore temperatura: '))
##s=input('Inserisci \'F\' o \'C\' a seconda della scala utilizzata: ')
##
##if s=='F':
##    t=(t-32)/1.8
##    
##if t>=100:
##    print('L\'acqua è allo stato gassoso')
##elif t>0:
##    print('L\'acqua è allo stato liquido')
##else:
##    print('L\'acqua è allo stato solido')
    
t=float(input('temperatura: '))
s=input('F o C?: ')

if s=='F':
    t=(t-32)/1.8

if t>=100:
    print('gassosa')
elif t>0:
    print('liquida')
else:
    print('solida')
