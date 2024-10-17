def Ex3(file1,file2):
    competenze = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        dati = riga.strip().split(',')
        nome = dati[0]
        disp = int(dati[1])
        comp = dati[2]
        competenze[comp] = [nome,disp]
    f1.close()
    ris = {}
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        dati = riga.strip().split(',')
        ditta = dati[0]
        ore = dati[1::2]
        comp = dati[2::2]
        diz = {}
        for i in range(len(ore)):
            if comp[i] not in competenze:
                diz[comp[i]] = 'Competenza Assente'
            elif int(ore[i]) > competenze[comp[i]][1]:
                diz[comp[i]] = 'Indisponibile'
            else:
                diz[comp[i]] = competenze[comp[i]][0]
                competenze[comp[i]][1] -= int(ore[i])
        ris[ditta] = diz
    f2.close()
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['dipendenti1.csv','commesse1.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti1.csv','commesse2.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Ditta3': {'Python': 'Flavia'}, 'Ditta4': {'Python': 'Flavia'}, 'Ditta5': {'Java': 'Carlo', 'DataBases': 'Giulia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse1.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse2.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Python': 'Flavia'}, 'Ditta4': {'Python': 'Flavia'}, 'Ditta5': {'Java': 'Carlo', 'DataBases': 'Giulia'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti2.csv','commesse3.csv'],{'Ditta1': {'Python': 'Flavia', 'Java': 'Carlo'}, 'Ditta2': {'DataBases': 'Giulia', 'MachineLearning': 'Angela'}, 'Ditta3': {'Java': 'Carlo', 'DataBases': 'Giulia', 'Python': 'Flavia'}, 'Ditta4': {'Python': 'Indisponibile'}, 'Ditta5': {'Python': 'Flavia', 'MachineLearning': 'Angela'}, 'Ditta6': {'Java': 'Carlo', 'DataBases': 'Indisponibile'}})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['dipendenti3.csv','commesse4.csv'],{'Azienda1': {'Python': 'Marta', 'C++': 'Piero'}, 'Azienda2': {'SistemiOperativi': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Azienda3': {'C++': 'Piero', 'SistemiOperativi': 'Giulia', 'Python': 'Marta'}, 'Azienda4': {'Python': 'Indisponibile'}, 'Azienda5': {'Python': 'Marta'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti3.csv','commesse5.csv'],{'Azienda1': {'Python': 'Marta', 'C++': 'Piero'}, 'Azienda2': {'SistemiOperativi': 'Giulia', 'MachineLearning': 'Competenza Assente'}, 'Azienda3': {'C++': 'Piero', 'SistemiOperativi': 'Giulia', 'Python': 'Marta'}, 'Azienda4': {'Python': 'Indisponibile'}, 'Azienda5': {'Python': 'Marta'}, 'Azienda6': {'C++': 'Piero', 'SistemiOperativi': 'Indisponibile'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti4.csv','commesse4.csv'],{'Azienda1': {'Python': 'Marta', 'C++': 'Piero'}, 'Azienda2': {'SistemiOperativi': 'Giulia', 'MachineLearning': 'Angela'}, 'Azienda3': {'C++': 'Piero', 'SistemiOperativi': 'Giulia', 'Python': 'Marta'}, 'Azienda4': {'Python': 'Indisponibile'}, 'Azienda5': {'Python': 'Marta'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti4.csv','commesse5.csv'],{'Azienda1': {'Python': 'Marta', 'C++': 'Piero'}, 'Azienda2': {'SistemiOperativi': 'Giulia', 'MachineLearning': 'Angela'}, 'Azienda3': {'C++': 'Piero', 'SistemiOperativi': 'Giulia', 'Python': 'Marta'}, 'Azienda4': {'Python': 'Indisponibile'}, 'Azienda5': {'Python': 'Marta'}, 'Azienda6': {'C++': 'Piero', 'SistemiOperativi': 'Indisponibile'}})
    counter_test_positivi += tester_fun(Ex3, ['dipendenti4.csv','commesse6.csv'],{'Azienda1': {'Python': 'Marta', 'C++': 'Piero'}, 'Azienda2': {'SistemiOperativi': 'Giulia', 'MachineLearning': 'Angela'}, 'Azienda3': {'C++': 'Piero', 'SistemiOperativi': 'Giulia', 'Python': 'Marta'}, 'Azienda4': {'Python': 'Indisponibile'}, 'Azienda5': {'Python': 'Marta', 'MachineLearning': 'Angela'}, 'Azienda6': {'C++': 'Piero', 'SistemiOperativi': 'Indisponibile'}})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
