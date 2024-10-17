def Ex1(n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""        

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [76672172322],4)
    counter_test_positivi += tester_fun(Ex1, [32210],3)
    counter_test_positivi += tester_fun(Ex1, [272323],6)
    counter_test_positivi += tester_fun(Ex1, [77777],1)
    counter_test_positivi += tester_fun(Ex1, [223344],2)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
