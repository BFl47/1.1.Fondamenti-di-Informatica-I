def Ex3(file1,file2,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',10],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',11],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv',9],{'Ipad': [5600, 0], 'Iphone': [5000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv',7],{'Ipad': [1200, 2000], 'Iphone': [4000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv',17],{'Ipad': [2000, 1200], 'Iphone': [7000, 5000], 'Ps5': [2500, 1000]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
