##lato=int(input('inserire la misura del lato del quadrato: '))
##spazio=' '*(lato-2)
##
##for i in range(1, lato+1):
##    if i==1 or i==lato:
##        print('*'*lato)
##    else:
##        #print('*',spazio,'*',sep='')
##        print('*'+spazio+'*')

l=int(input('lato: '))

for i in range(l):
    for j in range(l):
        if i==0 or i==l-1 or j==0 or j==l-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
