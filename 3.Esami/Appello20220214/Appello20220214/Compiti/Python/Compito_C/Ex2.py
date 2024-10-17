def Ex2(m):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[[1,10,4,5],[10,7,8,9],[7,8,7,6]]],{10:{(0,1),(1,0)},8:{(2,1)},7:{(2,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[0,1,2,3],[4,5,6,7]]],{})
    counter_test_positivi += tester_fun(Ex2, [[[3,2,1,0],[3,2,1,0]]],{3:{(1,0),(0,0)},2:{(0,1),(1,1)},1:{(0,2),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[[3,2,3,2,3,2]]],{3:{(0,4)}})
    counter_test_positivi += tester_fun(Ex2, [[[5,5],[5,4],[5,3],[3,2]]],{5:{(1,0),(2,0)},3:{(3,0)}})    
 
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
