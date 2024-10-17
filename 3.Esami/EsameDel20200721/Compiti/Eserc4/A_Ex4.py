from tester import tester_fun

def A_Ex4(file1,file2):
    """inserisci qui la tua soluzione"""
    oggetti = {}
    prezzi = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        riga = riga.strip().split(',')
        nome = riga[0]
        oggetto = riga[1]
        prezzo = int(riga[2])
        oggetti[oggetto] = nome
        prezzi[oggetto] = prezzo
    f1.close
    ris = {}
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        riga = riga.strip().split(',')
        acquirente = riga[0]
        oggetto = riga[1]
        offerta = int(riga[2])
        venditore = oggetti[oggetto]
        if offerta >= prezzi[oggetto]:
            prezzi[oggetto] = offerta + 1
            oggetti[oggetto] = acquirente
            if acquirente not in ris:
                ris[acquirente] = [1,-offerta]
            else:
                ris[acquirente] = [ris[acquirente][0]+1,ris[acquirente][1]-offerta]
            if venditore not in ris:
                ris[venditore] = [-1,offerta]
            else:
                ris[venditore] = [ris[venditore][0]-1,ris[venditore][1]+offerta]
    f2.close()
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte1.csv'],{'Paolo': [-1, 21], 'Francesco': [0, 4], 'Gianni': [1, -25]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte2.csv'],{'Paolo': [-2, 51], 'Francesco': [0, 4], 'Gianni': [2, -55]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte3.csv'],{'Paolo': [-2, 50], 'Francesco': [0, 4], 'Gianni': [2, -54]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte4.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [1, -51]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti3.csv','offerte5.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [0, 1], 'Giovanna': [1, -52]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
