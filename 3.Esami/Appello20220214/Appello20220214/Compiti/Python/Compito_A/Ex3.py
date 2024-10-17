def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['dipendenti1.csv','commesse1.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti1.csv','commesse2.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Ditta3': {'Python': 'Flavia'}, 'Ditta4': {'Python': 'Flavia'}, 'Ditta5': {'Java': 'Carlo', 'DataBases': 'Giulia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse1.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse2.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Python': 'Flavia'}, 'Ditta4': {'Python': 'Flavia'}, 'Ditta5': {'Java': 'Carlo', 'DataBases': 'Giulia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse3.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia', 'MachineLearning': 'Angela'}, 'Ditta6': {'Java': 'Carlo', 'DataBases': 'Indisponibile'}})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
