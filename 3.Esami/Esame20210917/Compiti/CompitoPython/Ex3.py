from tester import tester_fun

def Ex3(p,a,file):        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    d = {}
##    f = open(file,'r',encoding='UTF-8')
##    l_citta = []
##    for riga in f:
##        riga = riga.strip().split(',')
##        citta_p = riga[0]
##        citta_a = riga[1]
##        tempo = int(riga[2])
##        if citta_p not in l_citta:
##            l_citta.append(citta_p)
##        if citta_a not in l_citta:
##            l_citta.append(citta_a)
##        if (citta_p,citta_a) not in d:
##            d[(citta_p,citta_a)] = tempo
##        else:
##            if tempo < d[(citta_p,citta_a)]:
##                d[(citta_p,citta_a)] = tempo
##    l_citta.remove(a)
##    l_citta.remove(p)
##    f.close()
##    if (p,a) in d:
##        return d[(p,a)]
##    minimo = 8573489
##    tempotot = 0
##    for citta in l_citta:
##        if (p,citta) in d and (citta,a) in d:
##            tempotot = d[(p,citta)] + d[(citta,a)]
##            if tempotot < minimo:
##                minimo = tempotot   
##    if tempotot == 0:
##        return 'Impossibile'
##    return minimo

    d = {}
    f = open(file,'r',encoding='UTF-8')
    l_citta = []
    for riga in f:
        riga = riga.strip().split(',')
        partenza = riga[0]
        arrivo = riga[1]
        tempo = int(riga[2])
        if partenza not in l_citta:
            l_citta.append(partenza)
        if arrivo not in l_citta:
            l_citta.append(arrivo)
        if (partenza,arrivo) not in d:
            d[(partenza,arrivo)] = tempo
        else:
            if tempo < d[(partenza,arrivo)]:
                d[(partenza,arrivo)] = tempo
    l_citta.remove(a)
    l_citta.remove(p)
    f.close()
    if (p,a) in d:
        return d[(p,a)]
    minimo = 66666576567
    tempotot = 0
    for citta in l_citta:
        if (p,citta) in d and (citta,a) in d:
            tempotot = d[(p,citta)] + d[(citta,a)]
            if tempotot < minimo:
                minimo = tempotot
    if tempotot == 0:
        return 'Impossibile'
    return minimo

  
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli1.csv'] ,180)
counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli2.csv'] ,170)
counter_test_positivi += tester_fun(Ex3, ['Londra','Madrid','voli2.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Londra','Roma','voli2.csv'] ,80)
counter_test_positivi += tester_fun(Ex3, ['Roma','Madrid','voli2.csv'] ,90)

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
            
    

