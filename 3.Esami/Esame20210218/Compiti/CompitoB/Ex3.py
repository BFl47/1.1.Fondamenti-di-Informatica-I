def Ex3(file,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
##    f = open(file,'r',encoding='UTF-8')
##    d = {}
##    cancellazioni = []
##    for riga in f:
##        riga = riga.strip().split(',')
##        nome = riga[0]
##        tipo = riga[1]
##        if tipo == 'P':
##            nPosti = int(riga[2])
##            d[nome] = nPosti
##        else:
##            d[nome] = 0
##    f.close()
##    ris = {}
##    for nome in d:
##        if n >= d[nome] and d[nome] != 0:
##            n -= d[nome]
##            ris[nome] = d[nome]
##    return ris

    pren = {}
    lattesa = []
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        nome = riga[0]
        tipo = riga[1]
        if tipo == 'P':
            posti = int(riga[2])
            pren[nome] = posti
        else:
            pren[nome] = 0
    f.close()
    ris = {}
    for nome in pren:
        if n >= pren[nome] and pren[nome] != 0:
            n -= pren[nome]
            ris[nome] = pren[nome]
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',10],{'Marco': 4, 'Giorgio': 5})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',8],{'Marco': 4, 'Paola': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',12],{'Giorgio': 3, 'Andrea': 3, 'Paola': 6})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',8],{'Giorgio': 3, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni3.csv',12],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
