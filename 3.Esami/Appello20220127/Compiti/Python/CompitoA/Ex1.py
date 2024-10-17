def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[1,2,3,3,1,4,5,1,7]],3)
    counter_test_positivi += tester_fun(Ex1, [[1,2,1,4,3,4,3]],2)
    counter_test_positivi += tester_fun(Ex1, [[100,70,70,30,70,70,88]],2)
    counter_test_positivi += tester_fun(Ex1, [[4,3,3,2,1]],1)
    counter_test_positivi += tester_fun(Ex1, [[]],0)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
