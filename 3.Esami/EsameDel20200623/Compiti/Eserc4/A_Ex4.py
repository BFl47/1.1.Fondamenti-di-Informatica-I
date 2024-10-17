from tester import tester_fun

def A_Ex4(file1,file2):
    costi = {}
    f1 = open(file1,'r',encoding='UTF-8')
    f1.readline()
    for riga in f1:
        riga = riga.strip().split(',')
        prodotto = riga[0]
        costo = int(riga[1])
        costi[prodotto] = costo
    f1.close()

    l = []
    ricevute = {}
    f2 = open(file2,'r',encoding='UTF-8')
    f2.readline()
    for riga in f2:
        riga = riga.strip().split(',')
        ricev = riga[0]
        prodotto = riga[1]
        quant = int(riga[2])
        if prodotto not in l:
            l.append(prodotto)
            ricevute[ricev] = ricevute.get(ricev,0)+(quant*costi[prodotto])
    f2.close()

    return ricevute

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute1.csv'],{'R1': 13, 'R2': 12, 'R3': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute2.csv'],{'R1': 13, 'R2': 12, 'R3': 6} )
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute3.csv'] ,{'R4': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute4.csv'],{'R6': 8, 'R7': 410})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute1.csv'] ,{'R1': 8, 'R2': 14, 'R3': 12})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
