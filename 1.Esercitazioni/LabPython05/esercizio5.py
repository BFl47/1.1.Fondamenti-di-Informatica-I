##s=input('inserire una stringa: ')
##n=int(input('inserire la distanza: '))
##
##uguali=False
##i=0
##for i in range(0,len(s)-n):
##    if s[i]==s[i+n]:
##        uguali=True
##        print(uguali)
##        break
##if not uguali:
##    print(uguali)
##       
##    


s=input('stringa: ')
n=int(input('intero: '))

uguali=False
i=0
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        uguali=True
        print(uguali)
        break
if not uguali:
    print(uguali)
