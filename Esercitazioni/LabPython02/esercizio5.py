##n1=int(input('Inserisci n1: '))
##n2=int(input('Inserisci n2: '))
##n3=int(input('Inserisci n3: '))
##
##if n1<=min(n2,n3):
##    print('',max(n2,n3),'\n',min(n2,n3),'\n',n1)
##elif n2<=min(n1,n3):
##    print('',max(n1,n3),'\n',min(n1,n3),'\n',n2)
##elif n3<=min(n1,n2):
##    print('',max(n1,n2),'\n',min(n1,n2),'\n',n3)

n1=int(input('intero 1: '))
n2=int(input('intero 2: '))
n3=int(input('intero 3: '))
minimo=min(n1,n2,n3)
massimo=max(n1,n2,n3)
medio=(n1+n2+n3)-minimo-massimo
print(minimo,medio,massimo,sep='\n')
