##def distanza(s1,s2):
##    dist = abs(len(s1)-len(s2))
##    for i in range(min(len(s1),len(s2))):
##        if s1[i]!=s2[i]:
##            dist += 1
##    return dist
##
##def Ex2(i,file):
##    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""   
##    f = open(file,'r',encoding='UTF-8')
##    parole = f.read().split()
##    f.close()
##    d = {}
##    for elem in i:
##        d[elem] = set()
##        if len(parole) != 0:
##            distmin = distanza(elem, parole[0])
##            for parola in parole:
##                dist = distanza(elem, parola)
##                if dist < distmin:
##                    d[elem] = {parola}
##                    distmin = dist
##                elif dist == distmin:
##                    d[elem].add(parola)
##    return d

def dis(s1,s2):
    diff = abs(len(s1)-len(s2))
    lung = min(len(s1),len(s2))
    count = 0
    for j in range(lung):
        if s1[j] != s2[j]:
            count += 1
    ris = diff + count
    return ris        

def Ex2(i,file):
    d = {}
    f = open(file,'r',encoding='UTF-8')
    testo = f.read().split()
    f.close()
    
    for parola in i:
        d[parola] = set()
        minimo = 539480358
        for parola1 in testo:
            if dis(parola1,parola) < minimo:
                minimo = dis(parola1,parola)
        for parola1 in testo:
            if dis(parola1,parola) == minimo:
                d[parola].add(parola1)
    return d
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [{'casa','palla','mela'},'testo1.txt'],{'mela': {'nel'}, 'casa': {'la', 'casina'}, 'palla': {'molla', 'bella'}})
    counter_test_positivi += tester_fun(Ex2, [{'cassa','palline','malta'},'testo1.txt'],{'palline': {'pallone'}, 'malta': {'molla'}, 'cassa': {'casina'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo1.txt'],{'pelle': {'bella'}, 'casale': {'casina'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo2.txt'],{'pelle': {'bella'}, 'casale': {'casina', 'carine', 'case'}})
    counter_test_positivi += tester_fun(Ex2, [{'cena'},'testo2.txt'],{'cena': {'le', 'sono', 'case', 'nel', 'non'}})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
