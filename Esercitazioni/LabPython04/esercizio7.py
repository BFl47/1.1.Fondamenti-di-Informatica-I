##s=input('inserire una stringa: ')
##i=0
##piùdiffuso=0
##while i<len(s)-1:
##    c1=s.count(s[i])
##    c2=s.count(s[i+1])
##    piùdiffuso=max(c1,c2,piùdiffuso)
##    if c1<c2:
##        n=s[i+1]
##    elif c2<c1:
##        n=s[i]
##    elif c1==c2:
##        n=s[i+1]
##    i+=1
##    
##print(n)

    
##s=input()
##
##i=0
##massimo=0
##
##while i<len(s):
##    if s.count(s[i])>=massimo:
##        massimo=s.count(s[i])
##        freq=s[i]
##    i+=1
##
##print(freq)

s=input('stringa: ')
i=0
massimo=0
while i<len(s):
    if s.count(s[i])>=massimo:
        massimo=s.count(s[i])
        freq=s[i]
    i+=1
print(freq)































