def Ex1(l,x,y):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[1,2,2,0,3,1,3,4,2,1,7,3],2,3],[2,0,3])
    counter_test_positivi += tester_fun(Ex1, [[4,5,2,3,6],2,5],[4, 5, 2, 3, 6])
    counter_test_positivi += tester_fun(Ex1, [[0,3,4,6,2,3,1,2,5],3,2],[3,1,2])
    counter_test_positivi += tester_fun(Ex1, [[3,2,1,3,6,2,3],2,3],[2,3])
    counter_test_positivi += tester_fun(Ex1, [[7,5,4,3,6,9,10],4,9],[4,3,6,9])
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
