from tester import tester_fun

def A_Ex4(file,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""          
    f = open(file,'r',encoding='UTF-8')
    f.readline()
    partenze = {}
    arrivi = {}
    for riga in f:
        riga = riga.strip().split(',')
        partenza = riga[0]
        arrivo = riga[1]
        h_partenza = int(riga[2])
        h_arrivo = int(riga[3])
        if partenza == 'Anycity':
            if (partenza,arrivo) not in arrivi:
                arrivi[(partenza,arrivo)] = h_arrivo
            else:
                if arrivi[(partenza,arrivo)] > h_arrivo:
                    arrivi[(partenza,arrivo)] = h_arrivo
        if arrivo == 'Anycity':
            if (partenza,arrivo) not in partenze:
                partenze[(partenza,arrivo)] = h_partenza
            else:
                if partenze[(partenza,arrivo)] < h_partenza:
                    partenze[(partenza,arrivo)] = h_partenza
    f.close()
    l = []
    d = {}
    for key in arrivi:
        citta = key[1]
        acity = key[0]
        d[citta] = partenze[(citta,acity)] - arrivi[(acity,citta)]
        if d[citta] >= n:
            l.append(citta)
    l.sort()
    return l

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',3],['Londra','Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',5],['Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',4],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',7],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',11],[])

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
