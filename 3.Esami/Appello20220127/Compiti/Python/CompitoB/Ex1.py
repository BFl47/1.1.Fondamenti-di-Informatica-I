def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['ora','aldo','gioca','una','carta','e','antonio','prende','tre','danari']],3)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','la','gatta','al','lardo','che','ci','c','ci']],4)
    counter_test_positivi += tester_fun(Ex1, [['b','aa','ccc','dddd']],1)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','lardo','zampino','che']],2)
    counter_test_positivi += tester_fun(Ex1, [['nemo','profeta','in','patria','alea','iacta','est','']],3)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
