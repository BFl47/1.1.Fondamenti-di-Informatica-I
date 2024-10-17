def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv'],{'Iphone': [16, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [5, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv'],{'Iphone': [16, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti3.csv'],{'Iphone': [4, 0, 505], 'Ipad': [10, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv'],{'Iphone': [11, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [3, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv'],{'Iphone': [11, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [5, 0, 400]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
