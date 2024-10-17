from tester import tester_fun

def A_Ex7(l):
##        ins=set()
##        lista=[]
##        l1=[]
##        for insieme in l:
##                lista.append(list(insieme))
##        for i in range(len(lista)):
##                for j in range(len(lista[i])):
##                        if lista[i].count(lista[i][j])==1:
##                               l1.append(lista[i][j])
##        i=0
##        while i < len(l1):
##                if l1.count(l1[i])==1:
##                        ins.add(l1[i])
##                i+=1
##        return ins

        ris=set()
        l1=[]
        
        for ins in l:
                l1.append(list(ins))
        l2=[]
        for i in range(len(l1)):
                for j in range(len(l1[i])):
                        if l1[i].count(l1[i][j])==1:
                               l2.append(l1[i][j])
        i=0
        while i<len(l2):
                if l2.count(l2[i])==1:
                        ris.add(l2[i])
                i+=1
        return ris
                               
                

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
    counter_test_positivi += tester_fun(A_Ex7, [[set(),{-10},{2}]] , {-10,2})
    counter_test_positivi += tester_fun(A_Ex7, [[set()]] , set())
    counter_test_positivi += tester_fun(A_Ex7, [[set(),{10,-2},{10},{-2}]] , set())
    counter_test_positivi += tester_fun(A_Ex7, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})


    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
