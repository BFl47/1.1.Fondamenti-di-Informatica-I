from tester import tester_fun

def A_Ex4(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d = {}
    f1 = open(file1,'r',encoding='UTF-8')
    header = f1.readline()
    for riga in f1:
        riga = riga.strip().split(',')
        utente = riga[0]
        somma = int(riga[1])
        d[utente] = [somma,0,0] #saldo,max inviato,max ricevuto
    f1.close()
    print(d)
    f2 = open(file2,'r',encoding='UTF-8')
    header = f2.readline()
    for riga in f2:
        riga = riga.strip().split(',')
        pagante = riga[0]
        ricevente = riga[1]
        trasf = int(riga[2])
        if trasf < d[pagante][0]:
            d[pagante][0] -= trasf
            d[ricevente][0] += trasf
            if trasf > d[pagante][1]:
                d[pagante][1] = trasf
            if trasf > d[ricevente][2]:
                d[ricevente][2] = trasf
    f2.close()
    return d

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['utenti1.csv','trasferimenti1.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1800, 700, 0]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti2.csv','trasferimenti2.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1700, 700, 0], 'Paolo': [200, 0, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti3.csv','trasferimenti3.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti4.csv','trasferimenti4.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1700, 200, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti5.csv','trasferimenti5.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [500, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200], 'Irene': [0, 0, 0]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
