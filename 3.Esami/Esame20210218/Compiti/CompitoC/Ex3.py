def Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    f = open(file,'r',encoding='UTF-8')
##    diz_prel = {}
##    diz_cifra = {}
##    for riga in f:
##        riga = riga.strip().split(',')
##        nome = riga[0]
##        quota = int(riga[1])
##        if quota < 0:
##            diz_prel[nome] = diz_prel.get(nome,0) + 1
##        diz_cifra[nome] = diz_cifra.get(nome,0) + quota
##    f.close()
##    n_prel = 0
##    for nome in diz_prel:
##        if diz_prel[nome] > n_prel:
##            n_prel = diz_prel[nome]
##            nome_rosso = nome
##        if diz_prel[nome] == n_prel and n_prel != '0' and nome < nome_rosso:
##            nome_rosso = nome
##            n_prel = diz_prel[nome]
##    if diz_cifra[nome_rosso] > 0:
##        return 'nessun prelievo in rosso'
##    return nome_rosso, diz_cifra[nome_rosso]
    d = {}
    red = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        nome = riga[0]
        oper = int(riga[1])
        d[nome] = d.get(nome,0) + oper
        if d[nome] < 0:
            red[nome] = red.get(nome,0) + 1
    f.close()
    massimo = 0
    for nome in red:
        if red[nome] > massimo:
            massimo = red[nome]
    if massimo == 0:
        return 'nessun prelievo in rosso'
    l = []
    for nome in red:
        if red[nome] == massimo:
            l.append(nome)
    l.sort()
    nome = l[0]
    return nome,d[nome]
                      
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5
    
    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi1.csv'],('Antonio',-150))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi2.csv'],('Marco', 0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi3.csv'],'nessun prelievo in rosso')
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi4.csv'],('Gianni',0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi5.csv'],('Debora',20))
    

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
