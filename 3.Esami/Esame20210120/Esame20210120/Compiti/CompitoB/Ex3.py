def Ex3(l,file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    f = open(file,'r',encoding='UTF-8')
##    header = f.readline()
##    lista = []
##    for riga in f:
##        riga = riga.strip().split(',')
##        g1 = riga[0]
##        g2 = riga[1]
##        punto_g1 = riga[2]
##        punto_g2 = riga[3]
##        if l.index(punto_g1) > l.index(punto_g2):
##            lista.append(g1)
##        else:
##            lista.append(g2)
##    ris=[]
##    massimo = 0
##    for nome in lista:
##        if lista.count(nome) >= massimo:
##            massimo = lista.count(nome)
##    for nome in lista:
##        if lista.count(nome) == massimo and nome not in ris:
##            ris.append(nome)
##    ris.sort()
##    return ris

    d = {}
    ris = []
    f = open(file,'r',encoding='UTF-8')
    f.readline()
    for riga in f:
        riga = riga.strip().split(',')
        gioc1 = riga[0]
        gioc2 = riga[1]
        p1 = riga[2]
        p2 = riga[3]
        if l.index(p1) > l.index(p2):
            d[gioc1] = d.get(gioc1,0) + 1
        if l.index(p1) < l.index(p2):
            d[gioc2] = d.get(gioc2,0) + 1
    massimo = 0
    for gioc in d:
        if d[gioc] > massimo:
            massimo = d[gioc]
    for gioc in d:
        if d[gioc] == massimo:
            ris.append(gioc)
    ris.sort()
    return ris 
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file1.csv'],['Aldo','Marco'])
    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file2.csv'],['Anna'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file3.csv'],['Anna','Franco','Olga'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file4.csv'],['Matteo'])
    counter_test_positivi += tester_fun(Ex3, [['sballato','mezzo','uno','uno e mezzo','due','due e mezzo','tre','tre e mezzo','quattro', 'quattro e mezzo','cinque','cinque e mezzo','sei','sei e mezzo','sette','sette e mezzo'],'file5.csv'],['Frank','Olga'])

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
