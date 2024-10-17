def Ex2(file,s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
##    f = open(file,'r',encoding='UTF-8')
##    sinv = s[::-1]
##    count = 0
##    colonne = []
##    for riga in f:
##        riga = riga.strip()
##        if s in riga or sinv in riga:
##            count += 1
##        if len(colonne) == 0:
##            for i in range(len(riga)):
##                colonne.append('')
##        for i in range(len(riga)):
##            colonne[i] = colonne[i] + riga[i]
##    f.close()
##    for elem in colonne:
##        if s in elem or sinv in elem:
##            count += 1
##    return count


    m = []
    f = open(file,'r',encoding='UTF-8')
    sinv = s[::-1]
    count = 0
    for riga in f:
        if s in riga or sinv in riga:
            count += 1
        riga = riga.strip()
        riga = list(riga)
        m.append(riga)
    f.close()
    
    righe = len(m)
    colonne = len(m[0])
    for j in range(colonne):
        col = ''
        for i in range(righe):
            col += m[i][j]
        if s in col or sinv in col:
            count += 1
    return count     
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','PORO'],3)
    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','ATO'],1)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','PORTO'],2)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','PO'],6)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','ROT'],2)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
