def Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
##    f=open(file,'r',encoding='UTF-8')
##    d={}
##    for riga in f:
##        riga=riga.strip().split(',')
##        nome=riga[0]
##        nomeCar=riga[1]
##        valCar=int(riga[2])
##        d[nome,nomeCar]=d.get((nome,nomeCar),0)+valCar
##    f.close()
##    massimo=0
##    for key in d:
##        if d[key]>massimo:
##            massimo=d[key]
##            ris=key
##    return ris

    d = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split(',')
        nome = riga[0]
        caratt = riga[1]
        valore = int(riga[2])
        d[(nome,caratt)] = d.get((nome,caratt),0) + valore
    f.close()
    massimo = 0
    for tupla in d:
        if d[tupla] > massimo:
            massimo = d[tupla]
            ris = tupla
    return ris
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['file1.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file2.csv'],('Paolo', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file3.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file4.csv'],('Anna', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file5.csv'],('Paolo', 'punti'))

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
