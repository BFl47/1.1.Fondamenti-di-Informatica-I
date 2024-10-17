from tester import tester_fun

def Ex3(lista,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    d = {}
##    f = open(file, 'r', encoding='UTF-8')
##    for riga in f:
##        riga = riga.strip().split(',')
##        nome = riga[0]
##        riga.remove(nome)
##        numeri = []
##        for n in riga:
##            numeri.append(int(n))
##        d[nome] = numeri
##    f.close()
##    vincitore = []
##    fin = False
##    for elem in lista:
##        for nome in d:
##            if elem in d[nome]:
##                d[nome].remove(elem)
##            if len(d[nome]) == 0:
##                vincitore.append(nome)
##                vincitore.sort()
##                fin = True
##        if fin:
##            return vincitore[0]
##    if not fin:
##        minimo = 666666
##        for nome in d:
##            if len(d[nome]) <= minimo:
##                minimo = len(d[nome])
##        for nome in d:
##            if len(d[nome]) == minimo:
##                vincitore.append(nome)
##                vincitore.sort()
##    return vincitore[0]

    d = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        nome = riga[0]
        num = riga[1:]
        for i in range(len(num)):
            num[i] = int(num[i])
        d[nome] = num
    f.close()
    win = []
    for estratto in lista:
        for nome in d:
            if estratto in d[nome]:
                d[nome].remove(estratto)
        for nome in d:
            if len(d[nome]) == 0:
                win.append(nome)
        if len(win) != 0:
            win.sort()
            return win[0]
    minimo = 666666
    menonum = []
    for nome in d:
        if len(d[nome]) < minimo:
            minimo = len(d[nome])
    for nome in d:
        if len(d[nome]) == minimo:
            menonum.append(nome)
    menonum.sort()
    return menonum[0]
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, [[5,7,11,3,8],'cartelle1.csv'] ,'Anna')
counter_test_positivi += tester_fun(Ex3, [[8,7,11,3,5],'cartelle1.csv'] ,'Marco')
counter_test_positivi += tester_fun(Ex3, [[8,7,11,3,5],'cartelle2.csv'] ,'Giorgia')
counter_test_positivi += tester_fun(Ex3, [[7,12,3,5,11],'cartelle2.csv'] ,'Anna')
counter_test_positivi += tester_fun(Ex3, [[11,3,5],'cartelle2.csv'] ,'Giorgia')

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
