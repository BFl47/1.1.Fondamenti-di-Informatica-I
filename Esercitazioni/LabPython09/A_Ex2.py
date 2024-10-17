def A_Ex2(fileName):
##    fin=open(fileName,encoding='UTF-8')
##    riga=fin.readline()
##    l=[]
##    for riga in fin:
##        riga=riga.strip().split(',')
##        t=tuple()
##        if int(riga[1])>=18:
##            t=(riga[0],riga[2])
##            l.append(t)
##    fin.close()
##    return l
##            

    f=open(fileName,'r',encoding='UTF-8')
    header=f.readline()
    l=[]
    for riga in f:
        riga=riga.strip().split(',')
        if int(riga[1])>=18:
            t=(riga[0],riga[2])
            l.append(t)
    f.close()
    return l
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ["esami1.csv"], [('1345','Fisica'),('1346','Analisi'),('1896','Geometria'),('1753','Fisica')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami2.csv"], [('1346','Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami3.csv"], [('1347', 'Analisi'), ('1348', 'Analisi'), ('1347', 'Ricerca Operativa'), ('1349', 'Ricerca Operativa')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami4.csv"], [('1100', 'Basi di Dati'), ('1012', 'Basi di Dati'), ('1021', 'Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami5.csv"], [('1345','Fisica'),('1987','Fondamenti'),('1346','Analisi'),('1896','Geometria')])

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
