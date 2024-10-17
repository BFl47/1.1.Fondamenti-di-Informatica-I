from tester import tester_fun
            
def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    ris = []
##    if len(l) == 0:
##        return ris
##    
##    for i1 in range(len(l)):
##        minore = True
##        count = 0
##        
##        for i2 in range(i1+1,len(l)):
##            if l[i1] >= l[i2]:
##                count += 1
##        if count == len(l)-len(l[:i1+1]):
##            minore = False
##        if minore:
##            ris.append(l[i1])
##    ris.append(l[-1])
##    return ris
    ris = []
    if len(l) == 0:
        return ris
    
    for i in range(len(l)):
        count = 0
        minore = True        
        for j in range(i+1,len(l)):
            if l[i] >= l[j]:
                count += 1
        if count == len(l)-(i+1):
            minore = False
        if minore:
            ris.append(l[i])
    ris.append(l[-1])           
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [[10,3,4,7,5,6]],[3,4,5,6])
counter_test_positivi += tester_fun(Ex1, [[20,10,0,-2,-4]],[-4])
counter_test_positivi += tester_fun(Ex1, [[]],[])
counter_test_positivi += tester_fun(Ex1, [[14,12,11,12,20]],[14,12,11,12,20])
counter_test_positivi += tester_fun(Ex1, [[1,10,-3,1,-4]],[1,-3,-4])

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


