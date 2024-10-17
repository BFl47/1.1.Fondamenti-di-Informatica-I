from tester import tester_fun

def A_Ex4(file):
    d1 = {}
    d2 = {}
    dX = {}
    ris = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        partita = int(riga[0])
        tipo = riga[1]
        cifra = int(riga[2])
        quota = int(riga[3])
        if partita not in ris:
            ris[partita] = [0,0,0,0] #totspeso,ris1,risX,ris2
        ris[partita][0] += cifra
        if tipo == '1':
            d1[partita] = d1.get(partita,0) + (cifra*quota)
        if tipo == 'X':
            dX[partita] = dX.get(partita,0) + (cifra*quota)
        if tipo == '2':
            d2[partita] = d2.get(partita,0) + (cifra*quota)
    f.close()
    for partita in ris:
        ris[partita][1] = d1[partita]
        ris[partita][2] = dX[partita]
        ris[partita][3] = d2[partita]
    return ris
    
        
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{12: [27, 20, 10, 36]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{12: [27, 20, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{12: [37, 50, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{12: [49, 50, 34, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{12: [69, 110, 34, 36], 10: [37, 20, 24, 45]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
