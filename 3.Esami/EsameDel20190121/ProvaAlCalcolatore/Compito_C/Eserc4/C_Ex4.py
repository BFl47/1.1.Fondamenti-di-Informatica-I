from tester import tester_fun

def C_Ex4(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""            
    f= open(file,'r',encoding='UTF-8')
    ris = {}
    tipo = {} #[antipasto,pizza,bevanda,n_clienti]
    f.readline()
    for riga in f:
        riga = riga.strip().split(',')
        tavolo = int(riga[0])
        clienti = int(riga[1])
        portata = riga[2]
        quant = int(riga[3])
        prezzo = int(riga[4])
        ris[tavolo] = ris.get(tavolo,0) + quant*prezzo
        if tavolo not in tipo:
            tipo[tavolo] = [0,0,0,clienti]
        if portata == 'antipasto':
            tipo[tavolo][0] += quant
        if portata == 'pizza':
            tipo[tavolo][1] += quant
        if portata == 'bevanda':
            tipo[tavolo][2] += quant
    f.close()
    for tavolo in tipo:
        sconto = 0
        clienti = tipo[tavolo][3]
        for elem in tipo[tavolo]:
            if elem > clienti:
                sconto += (elem-clienti)
        ris[tavolo] -= sconto
    return ris
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex4, ['comande1.csv'],{1:9, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande2.csv'],{1:23, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande3.csv'],{1:23, 2:6, 3:2})
counter_test_positivi += tester_fun(C_Ex4, ['comande4.csv'],{1: 23, 2: 11, 3: 14})
counter_test_positivi += tester_fun(C_Ex4, ['comande5.csv'],{1: 23, 2: 11, 3: 14, 4: 17})

print('La funzione',C_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
