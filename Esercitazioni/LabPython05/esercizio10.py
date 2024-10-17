##lato=int(input('inserire la dimensione del lato del quadrato: '))
##
##for i in range(lato):
##    for j in range(lato):
##        if i==0 or i==lato-1 or j==0 or j==lato-1 or j==i or j==lato-1-i:
##            print('*', end='')
##        else:
##            print(' ', end='')
##    print()

l=int(input('lato: '))

for i in range(l):
    for j in range(l):
        if i==0 or i==l-1 or j==0 or j==l-1 or j==i or j+i==l-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
