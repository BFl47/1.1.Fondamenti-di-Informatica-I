from tester import tester_fun
            
def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    massimo = 0
##    for elem in l:
##        if l.count(elem) > massimo:
##            massimo = l.count(elem)
##            piufreq = elem
##    while piufreq in l:
##        l.remove(piufreq)
##    return l

    massimo = 0
    for elem in l:
        if l.count(elem) > massimo:
            massimo = l.count(elem)
            piufreq = elem
    while piufreq in l:
        l.remove(piufreq)
    return l

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [[1,2,'pippo',1,2,1,'a','a']],[2,'pippo',2,'a','a'])
counter_test_positivi += tester_fun(Ex1, [['a',1,2,'pippo',1,'a',2,1,'a','a']],[1,2,'pippo',1,2,1])
counter_test_positivi += tester_fun(Ex1, [[1,1,1,1,1,1]],[])
counter_test_positivi += tester_fun(Ex1, [['mamma',2,'pippo','mamma','pippo','mamma']],[2,'pippo','pippo'])
counter_test_positivi += tester_fun(Ex1, [[2,1,3,4,1,3,5,1,2]],[2,3,4,3,5,2])

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
