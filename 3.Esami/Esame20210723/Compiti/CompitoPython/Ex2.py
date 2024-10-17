from tester import tester_fun

def Ex2(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    massimo = 0
##    num_a = 0
##    for car in s:
##        if car != 'a':
##            if num_a >= massimo:
##                massimo = num_a
##                num_a = 0
##        else:
##            num_a += 1
##            if num_a >= massimo:
##                massimo = num_a
##    return massimo

    s1 = ''
    massimo = 0
    for c in s:
        if c == 'a':
            s1 += c
        else:
            s1 = ''
        if len(s1) > massimo:
            massimo = len(s1)
    return massimo
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['dfgaadfaaaffgeaf'] ,3)
counter_test_positivi += tester_fun(Ex2, ['serftghno'] ,0)
counter_test_positivi += tester_fun(Ex2, ['portaala'] ,2)
counter_test_positivi += tester_fun(Ex2, ['aaaaaaaaaa'] ,10)
counter_test_positivi += tester_fun(Ex2, ['aaaabbaaaabba'] ,4)

print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

           
    
