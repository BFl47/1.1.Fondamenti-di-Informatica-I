def Ex1(l,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
##    ins=set()
##
##    for parola1 in l:
##        for parola2 in l:
##            s=''
##            for c in parola1:
##                if c in parola2 and c not in s:
##                    s+=c
##            if len(s)>=n and parola1 != parola2:
##                ins.add(parola1)
##                ins.add(parola2)
##    return ins

    ins = set()
    for parola1 in l:
        for parola2 in l:
            s = ''
            for c in parola1:
                if c in parola2 and c not in s:
                    s += c
            if len(s) >= n and parola1 != parola2:
                ins.add(parola1)
                ins.add(parola2)
    return ins
        
        

    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],2],{'accordare', 'arciere'})
    counter_test_positivi += tester_fun(Ex1, [["arciere","pippo","pluto"],1],{'arciere', 'pluto', 'pippo'})
    counter_test_positivi += tester_fun(Ex1, [["arciere","pompiere","bere"],3],{'arciere', 'pompiere'})
    counter_test_positivi += tester_fun(Ex1, [["mare","amare","mammare",""],3],{'mammare', 'mare', 'amare'})
    counter_test_positivi += tester_fun(Ex1, [["mento","casa","cero"],2],{'mento', 'cero'})

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
