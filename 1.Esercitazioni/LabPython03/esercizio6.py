##s=input()
##x=chr(100)
##p=0
##corretto=True
##while p<len(s) and corretto:
##    if ord(s[p])<=ord(x):
##        p+=1
##    else:
##        corretto=False
##if p==len(s):
##    print('stringa consumata e carattere non trovato')
##else:
##    print('il primo carettere con codice Unicode maggiore di 100 è',s[p])

s=input('stringa: ')
corretto=True
i=0
while i<len(s) and corretto:
    if ord(s[i])<=100:
        i+=1
    else:
        corretto=False
if i==len(s):
    print('stringa consumata e carattere non trovato')
else:
    print('il primo carettere con codice Unicode maggiore di 100 è',s[i])
