def Ex3(disp,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti1.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'NO', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti1.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Francesco': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [10000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'NO', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [15000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [12000,'prestiti2.csv'],{'Paola': 'SI', 'Flavio': 'SI', 'Gianna': 'SI', 'Paolo': 'SI', 'Piera': 'SI', 'Francesco': 'NO', 'Franca': 'SI'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
