from tester import tester_fun

def C_Ex4(file):
    """Inserite qui la vostra soluzione"""
##    f = open(file,'r',encoding='UTF-8')
##    l = []
##    for riga in f:
##        if len(riga) == 0:
##            return l
##        riga = riga.strip().split(',')
##        for elem in riga:
##            l.append(int(elem))
##    f.close()
##    massimo = 0
##    for elem in l:
##        if l.count(elem) > massimo:
##            massimo = l.count(elem)
##    i = 0
##    while i < len(l):
##        if l.count(l[i]) != massimo:
##            l.remove(l[i])
##        else:
##            i += 1
##    ins = set(l)
##    l = list(ins)
##    l.sort()
##    return l

    f = open(file,'r',encoding='UTF-8')
    d = {}
    l = []
    for riga in f:
        riga = riga.strip().split(',')
        for elem in riga:
            d[elem] = d.get(elem,0)+1
    if d != {}:
        valori = d.values()
        massimo = max(valori)
    for key in d:
        if d[key] == massimo:
            l.append(int(key))
    l.sort()
    return l
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex4, ['ruota1.csv'],[14,50])
counter_test_positivi += tester_fun(C_Ex4, ['ruota2.csv'],[2,14])
counter_test_positivi += tester_fun(C_Ex4, ['ruota3.csv'],[2])
counter_test_positivi += tester_fun(C_Ex4, ['ruota4.csv'],[24,43,47,50])
counter_test_positivi += tester_fun(C_Ex4, ['ruota5.csv'],[])

print('La funzione',C_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
