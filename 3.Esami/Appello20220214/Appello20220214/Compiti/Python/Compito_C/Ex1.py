def Ex1(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, ['cavallo pazzo'],6)
    counter_test_positivi += tester_fun(Ex1, ['arciere ponte'],7)
    counter_test_positivi += tester_fun(Ex1, ['parte di una casa'],8)
    counter_test_positivi += tester_fun(Ex1, ['ponte bassuz, tunnel lungo'],9)
    counter_test_positivi += tester_fun(Ex1, ['aaaaabbbbb'],2)
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
