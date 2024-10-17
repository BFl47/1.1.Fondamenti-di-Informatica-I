from tester import tester_fun
            
def Ex1(I):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
##    X = set()
##    trans = True
##    for t1 in I:
##        for t2 in I:
##            if t1[1] == t2[0] and (t1[0],t2[1]) not in I:
##                trans = False
##            X.add(t1[0])
##            X.add(t1[1])
##            X.add(t2[0])
##            X.add(t2[1])
##    return trans,len(X)

    X = set()
    trans = True
    for tupla1 in I:
        X.add(tupla1[0])
        X.add(tupla1[1])
        for tupla2 in I:
            if tupla1[1] == tupla2[0]:
                if (tupla1[0],tupla2[1]) not in I:
                    trans = False
    return (trans, len(X))


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,3),(1,3),(3,5),(1,5),(2,5)}],(True,4))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,6),(1,6),(2,1)}],(False,3))
counter_test_positivi += tester_fun(Ex1, [{(2,2),(5,5)}],(True,2))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,3),(3,4),(1,3),(2,4),(1,4),(4,5),(1,5),(2,5),(3,5),(1,5)}],(True,5))
counter_test_positivi += tester_fun(Ex1, [{(2,6),(6,2)}],(False,2))

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
