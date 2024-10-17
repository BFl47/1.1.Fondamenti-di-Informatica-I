def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    ins = set()
##    for parola in l:
##        if parola == parola[::-1]:
##            ins.add(parola)
##    if ins == set():
##        ins = set(l)
##        return ins
##    n = 0
##    massimo = ''
##    for elem in ins:
##        if len(elem) > n:
##            n = len(elem)
##            massimo = elem
##    ris = set()
##    ris.add(massimo)
##    for parola in l:
##        if len(parola) >= n*2:
##            count = 0
##            for i in range(n):
##                if parola[i] == parola[-(i+1)]:
##                    count += 1
##            if count == n:
##                ris.add(parola)
##    
##    return ris

    ris = set()
    massimo = 0
    for s in l:
        invs = s[::-1]
        i = 0
        uguali = True
        while uguali and i < len(s):
            if s[i] == invs[i]:
                i += 1
            else:
                uguali = False
        if i > massimo:
            massimo = i
            ris = {s}
        elif i == massimo:
            ris.add(s)
    return ris
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda']],{'plutoulp', 'ava'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna']],{'anna'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna','pattamoattap']],{'pattamoattap'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','antoitna']],{'ava', 'antoitna', 'plutoulp'})
    counter_test_positivi += tester_fun(Ex1, [['avoli','avo','pluto','corda']],{'corda', 'avoli', 'pluto', 'avo'})
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
