def Ex3(file1,l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',60,'Python',10,'DataBases',40]],{'Java': 'Carlo', 'Python': 'Flavia', 'DataBases': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',20,'MachineLearning',10]],{'Java': 'Flavia', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze1.csv',['Java',20,'Python',60,'MachineLearning',10]],{'Java': 'Flavia', 'Python': 'Nessuno', 'MachineLearning': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['competenze2.csv',['Java',20,'Python',10]],{'Java': 'Flavia', 'Python': 'Flavia'})
    counter_test_positivi += tester_fun(Ex3, ['competenze2.csv',['Java',20,'Python',50,'DataBases',40,'MachineLearning',10]],{'Java': 'Flavia', 'Python': 'Flavia', 'DataBases': 'Nessuno', 'MachineLearning': 'Gianni'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
