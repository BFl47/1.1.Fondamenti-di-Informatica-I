from tester import tester_fun

def A_Ex6(a,b):
##        ins=set()
##        lA=[]
##        lB=[]
##        lista=[]
##        for insieme in a:
##                lA.append(list(insieme))
##        for insieme in b:
##                lB.append(list(insieme))
##        for i in range(len(lA)):
##                for j in range(len(lA[i])):
##                        if lA[i][j] in lB[i][0]:
##                                lista=[lA[i][0],lB[i][1]]
##                                ins.add(tuple(lista))
##        return ins


        ins=set()
        for t1 in a:
                for t2 in b:
                        if t1[1]==t2[0]:
                                t=(t1[0],t2[1])
                                ins.add(t)
        return ins
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Giuseppe', 'Rieti'), ('Aldo', 'Torino')}, {('Napoli', 'Campania'), ('Benevento', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio'), ('Genova', 'Liguria')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio'), ('Giuseppe', 'Lazio')})
    counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli')}, {('Roma', 'Lazio')}] , set())
    counter_test_positivi += tester_fun(A_Ex6, [set(), {('Napoli', 'Campania')}] , set())
    counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), }, {('Napoli', 'Campania')}] , {('Giovanni', 'Campania')})
    counter_test_positivi += tester_fun(A_Ex6, [{('Giovanni', 'Napoli'), ('Marco', 'Roma')}, {('Napoli', 'Campania'), ('Roma', 'Lazio'), ('Rieti', 'Lazio')}] , {('Giovanni', 'Campania'), ('Marco', 'Lazio')})

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
