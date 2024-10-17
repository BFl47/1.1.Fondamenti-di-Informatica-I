def Ex2(m):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[[3,2,3,4],[2,2,1,4],[6,1,2,3],[1,1,1,1]]],12)
    counter_test_positivi += tester_fun(Ex2, [[[2,3,1],[1,2,2],[2,2,2]]],8)
    counter_test_positivi += tester_fun(Ex2, [[[-2,-3,-1],[-1,-2,-2],[-2,-2,2]]],-4)
    counter_test_positivi += tester_fun(Ex2, [[[3]]],3)
    counter_test_positivi += tester_fun(Ex2, [[]],0)
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
