from tester import tester_fun

def B_Ex4(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(file,'r',encoding='UTF-8')
    f.readline()
    volo1 = {}
    volo2 = {}
    for riga in f:
        riga = riga.strip().split(',')
        partenza = riga[0]
        arrivo = riga[1]
        h_partenza = int(riga[2])
        h_arrivo = int(riga[3])
        if partenza == 'City1':
            volo1[(partenza,arrivo)] = h_arrivo
        if arrivo == 'City2':
            volo2[(partenza,arrivo)] = h_partenza
    f.close()
    ris = []
    for key in volo1:
        citta = key[1]
        if volo1[('City1',citta)] < volo2[(citta,'City2')]:
            ris.append(citta)
    return ris
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['voli1.csv'],['Londra','Parigi'])
counter_test_positivi += tester_fun(B_Ex4, ['voli2.csv'],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex4, ['voli3.csv'],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex4, ['voli4.csv'],['Parigi'])
counter_test_positivi += tester_fun(B_Ex4, ['voli5.csv'],[])

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
