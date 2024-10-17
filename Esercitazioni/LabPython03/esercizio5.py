##s=input()
##while not (s.isalpha() and s.islower()):
##    print(s[0]+s[-1])
##    s=input()
##print(s[0]+s[-1])
##    

s=input('stringa: ')
while not (s.isalpha() and s.islower()):
    print(s[0]+s[-1])
    s=input('stringa: ')
print(s[0]+s[-1])
