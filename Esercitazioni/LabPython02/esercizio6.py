##a=int(input('Inserisci lato a: '))
##b=int(input('Inserisci lato b: '))
##c=int(input('Inserisci lato c: '))
##
##if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<b+a:
##    if (a==b) and (b==c):
##        print('Triangolo equilatero')
##    elif (a==b) or (a==c ) or (b==c):
##        print ('Triangolo isoscele')
##    else:
##        print('Triangolo scaleno')
##else:
##    print('Input non valido')
        
a=int(input('lato: '))
b=int(input('lato: '))
c=int(input('lato: '))

if a*b*c>0 and a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print('equilatero')
    elif a == b or a == c or b == c:
        print('isoscele')
    else:
        print('scaleno')
else:
    print('input non valido')
