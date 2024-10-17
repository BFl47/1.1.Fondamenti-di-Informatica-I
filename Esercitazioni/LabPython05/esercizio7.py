##s=input('inserire una stringa: ')
##
##almenodue=False
##
##for c in s:
##    if s.count(c)>1:
##        almenodue=True
##        print(almenodue)
##        break
##if not almenodue:
##    print(almenodue)

s=input('stringa: ')
due=False
for c in s:
    if s.count(c)>1:
        due=True
print(due)
