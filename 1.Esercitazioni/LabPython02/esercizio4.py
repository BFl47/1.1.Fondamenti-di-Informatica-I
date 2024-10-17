##n=int(input('Inserisci il numeratore: '))
##d=int(input('Inserisci il denominatore: '))
##
##if n<d:
##    print('Frazione propria')
##elif n%d==0:
##    print('Funzione apparente')
###elif n>d and n%d!=0:
##else:
##    print('Funzione impropria')

n=int(input('numeratore: '))
d=int(input('denominatore: '))

if n<d:
    print('funzione propria')
elif n%d==0:
    print('funzione apparente')
else:
    print('funzione impropria')
