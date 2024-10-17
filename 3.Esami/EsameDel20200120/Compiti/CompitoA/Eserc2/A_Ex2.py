from tester import tester_fun

def A_Ex2(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d_oggetti = {}
    f1 = open(file1,'r',encoding='UTF-8')
    header = f1.readline()
    for riga in f1:
        riga = riga.strip().split(',')
        oggetto = riga[0]
        prezzo = int(riga[1])
        d_oggetti[oggetto] = prezzo
    f1.close()

    d = {}
    f2 = open(file2,'r',encoding='UTF-8')
    header = f2.readline()
    for riga in f2:
        riga = riga.strip().split(',')
        aquirente = riga[0]
        oggetto = riga[1]
        offerta = int(riga[2])
        if d_oggetti[oggetto] <= offerta and oggetto not in d:
            d[oggetto] = [aquirente,offerta]
        if d_oggetti[oggetto] <= offerta and oggetto in d and offerta > d[oggetto][1]:
            d[oggetto] = [aquirente,offerta]
    f2.close()

    return d
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['oggetti1.csv','offerte1.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti2.csv','offerte2.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti3.csv','offerte3.csv'] ,{'Vaso': ['Giorgio', 120], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti4.csv','offerte4.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti5.csv','offerte5.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500], 'Tavolo': ['Mario', 210]})

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
