def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie1.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie1.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie2.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie2.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','allergie3.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Caprese', 'Flavia': 'Tiramisu', 'Paolo': 'Focaccia'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
