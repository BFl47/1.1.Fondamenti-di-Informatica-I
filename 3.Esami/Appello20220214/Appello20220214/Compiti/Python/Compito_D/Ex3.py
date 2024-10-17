def Ex3(maxSpesa,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, [200,'offerte1.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte1.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [200,'offerte2.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Guanti': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'SI'})
    counter_test_positivi += tester_fun(Ex3, [260,'offerte2.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'SI', 'Guanti': 'NO', 'Maglione': 'NO', 'Scarpe': 'SI', 'Sci': 'NO'})
    counter_test_positivi += tester_fun(Ex3, [180,'offerte3.csv'],{'Moto': 'SI', 'Casco': 'SI', 'Cappotto': 'NO', 'Pantaloni': 'SI', 'Guanti': 'SI', 'Maglione': 'SI', 'Scarpe': 'SI', 'Sci': 'NO'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
