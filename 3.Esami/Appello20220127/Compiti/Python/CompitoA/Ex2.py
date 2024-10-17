def Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{11:[1],3:[3,2,1],1:[2],111:[3]})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{1:[2,1],2:[3]})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{1:[1],11:[3],22:[4]})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{22:[1],11:[3,2],1:[4],2:[4]})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{222:[5,4,1],1000:[4,3,2],22:[4]})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
