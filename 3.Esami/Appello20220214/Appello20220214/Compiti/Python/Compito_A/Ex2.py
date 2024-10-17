def Ex2(m,s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','b','r']],'fredda'],{'a':{(0,0)},'r':{(0,1),(1,2)}})
    counter_test_positivi += tester_fun(Ex2, [[['a','r','d'],['d','b','r']],'zorro'],{})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','i'],['t','o','d'],['c','i','m']],'domenica'],{'o':{(1,1)},'i':{(0,2),(2,1)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','o']],'oxford'],{'x':{(0,0)}})
    counter_test_positivi += tester_fun(Ex2, [[['x','O','e'],['a','o','d'],['c','i','o']],'arcobaleno'],{'e':{(0,2)},'o':{(1,1),(2,2)}})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
