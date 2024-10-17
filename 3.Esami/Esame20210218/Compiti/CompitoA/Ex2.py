def Ex2(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    d = {}
##    ins = set()
##    if len(l) == 0:
##        return ins
##    for tupla in l:
##        t = list(tupla)
##        nome = t[0] 
##        t.remove(nome)
##        perf = sum(t)
##        d[nome] = perf
##    massimo = -666
##    for nome in d:
##        if d[nome] >= massimo:
##            massimo = d[nome]
##    for nome in d:
##        if d[nome] == massimo:
##            ins.add(nome)
##    return ins

    ris = set()
    d = {}
    for elem in l:
        l1 = []
        nome = elem[0]
        l1 = list(elem)
        l1.remove(nome)
        somma = sum(l1)
        d[nome] = somma
    massimo = -6666666
    for nome in d:
        if d[nome] > massimo:
            massimo = d[nome]
    for nome in d:
        if d[nome] == massimo:
            ris.add(nome)
    return ris     
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[('marco',-3,0,1),('aldo',2,3),('maria',-1,1,2,1,2)]],{'aldo','maria'})
    counter_test_positivi += tester_fun(Ex2, [[('sergio',11,2,13)]],{'sergio'})
    counter_test_positivi += tester_fun(Ex2, [[('monica',-3,-2,0),('marcello',-2,-3),('alessandra',-5,-5)]],{'monica','marcello'})
    counter_test_positivi += tester_fun(Ex2, [[('sandro',1,2,3),('sonia',25),('giorgia',-5,-5,-5,-5),('fabio',5,5,5,5,5)]],{'sonia','fabio'})
    counter_test_positivi += tester_fun(Ex2, [[('andrea',2,3,-2,-3),('giorgia',-2,-2,-3),('maria',-5)]],{'andrea'})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
