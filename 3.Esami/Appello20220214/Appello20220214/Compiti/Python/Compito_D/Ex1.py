def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""       

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione
    
    counter_test_positivi += tester_fun(Ex1, [[7,3,10,2,5,7,12,3]],4)
    counter_test_positivi += tester_fun(Ex1, [[1,1,1,2,2,3,1,4,5,9]],5)
    counter_test_positivi += tester_fun(Ex1, [[1,3,5,7,11,19]],0)
    counter_test_positivi += tester_fun(Ex1, [[1,3,4,7,11,18,2,3,5,1]],6)
    counter_test_positivi += tester_fun(Ex1, [[10,1,2,3,1,4,2,9]],3)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
