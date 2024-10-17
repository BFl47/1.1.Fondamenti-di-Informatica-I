##a=int(input('Inserisci un anno: '))
##if a%100==0:
##    if a%400==0:
##        print('Anno bisestile')
##    else:
##        print('Anno non bisestile')
##elif a%4==0:
##    print('Anno bisestile')
##else:
##    print('Anno non bisestile')
##
##
##anno=int(input('Inserisci un anno: '))
##if ((anno%4==0) and (anno%100)!=0)) or anno%400==0:
##    print('anno bisestile')
##else:
##    print('anno non bisestile')

anno=int(input('anno: '))
if (anno%4 == 0 and anno%100 != 0) or anno%400 ==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
