def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'PizzaMargherita'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Carbonara'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','golosi3.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
