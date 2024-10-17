from tester import tester_fun

def D_Ex4(file,ore,minuti):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""            
    arrivi = {}
    ris= []
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        if len(riga) == 3:
            treno = riga[0]
            h = int(riga[1])
            m = int(riga[2])
            mtot = m + 60*h
            arrivi[treno] = arrivi.get(treno, mtot)
        else:
            treno = riga[0]
            m = int(riga[1])
            arrivi[treno] += m       
    f.close()
    mintot = minuti + ore*60
    for treno in arrivi:
        if mintot >= arrivi[treno]:
            ris.append(treno)
    ris.sort()
    return ris
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',12,20] ,['54200','6310'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',12,20] ,['54200', '6310', '79001'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',10,20] ,[])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',11,40] ,['54200'] )
counter_test_positivi += tester_fun(D_Ex4, ['ritardi3.csv',14,20] ,['54200', '6310', '6550', '79001'])

print('La funzione',D_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
