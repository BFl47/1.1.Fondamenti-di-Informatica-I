def A_Ex3(fileName):
##    fin=open(fileName,encoding='UTF-8')
##    riga=fin.readline()
##    l=[]
##    for riga in fin:
##        riga=riga.strip().split(',')
##        if int(riga[1])>=29:
##            l.append(riga[2])
##    fin.close()
##    
##    ins=set()
##    for i in range(len(l)):
##        if l.count(l[i])>=2:
##            ins.add(l[i])
##    
##    return ins
    
    f=open(fileName,'r',encoding='UTF-8')
    header=f.readline()
    l=[]
    for riga in f:
        riga=riga.strip().split(',')
        if int(riga[1])>=29:
            l.append(riga[2])
    f.close()
    ins=set()
    for materia in l:
        if l.count(materia)>1:
            ins.add(materia)
    return ins
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
