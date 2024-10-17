from tester import tester_fun

def A_Ex3(l):
##    i=0
##    while i<len(l)-1:
##        if l[i]<l[i+1]:
##            diff=l[i+1]-l[i]
##            l.append(diff)
##        i+=1
##    return l

    i=0
    while i<len(l)-1:
        if l[i]<l[i+1]:
            diff=l[i+1]-l[i]
            l.append(diff)
        i+=1
    return l
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, [[10,1,11,31,251]] , [10,1,11,31,251,10,20,220,10,200,190])
    counter_test_positivi += tester_fun(A_Ex3, [[]] , [])
    counter_test_positivi += tester_fun(A_Ex3, [[2,7,3]] , [2,7,3,5,2])
    counter_test_positivi += tester_fun(A_Ex3, [[200,501,300]] , [200,501,300,301,1])
    counter_test_positivi += tester_fun(A_Ex3, [[3,2,0]] , [3,2,0])


    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
