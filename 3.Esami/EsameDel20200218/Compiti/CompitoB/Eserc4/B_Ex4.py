from tester import tester_fun

def B_Ex4(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d = {}
    ris = {}
    f = open(file,'r',encoding='UTF-8')
    f.readline()
    for riga in f:
        riga = riga.strip().split(',')
        prodotto = riga[0]
        quant = int(riga[1])
        if quant >= 0: #deposito
            d[prodotto] = d.get(prodotto,0) + quant
        else:          #prelievo
            if d.get(prodotto,0) >= abs(quant):
                d[prodotto] = d.get(prodotto,0) + quant
            else:
                ris[prodotto] = ris.get(prodotto,0) + abs(d.get(prodotto,0) + quant)
                d[prodotto] = 0
    f.close()
    return ris
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['file1.csv'],{'Lavatrice':3,'Televisore':1})
counter_test_positivi += tester_fun(B_Ex4, ['file2.csv'],{'Frigorifero':3,'PS4':3})
counter_test_positivi += tester_fun(B_Ex4, ['file3.csv'],{})
counter_test_positivi += tester_fun(B_Ex4, ['file4.csv'],{'Televisore':3,'Frigorifero':1})
counter_test_positivi += tester_fun(B_Ex4, ['file5.csv'],{'Decoder':50,'Frigorifero':1,'Forno':1})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
