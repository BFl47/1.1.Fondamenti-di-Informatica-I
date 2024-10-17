from tester import tester_fun

def Ex2(M,I):
    affondate = 0
    for i in range(len(M)):
        barca=set()
        for j in range(len(M[0])):
            if M[i][j]==1:
                barca.add((i,j))
                if j==len(M[0])-1 or M[i][j+1]==0:
                        if barca.issubset(I):
                            affondate+=1
            else:
                barca=set()
    return affondate

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2,[[[0,1,1,0,1,0],[0,0,0,1,1,0],[0,0,0,1,1,1]],{(0,1),(0,2),(1,3),(1,0),(2,3),(2,4),(2,5)}],2)
counter_test_positivi += tester_fun(Ex2,[[[1,1,1],[0,1,0],[0,0,0],[1,0,1]],{(0,0),(0,1),(0,2),(1,0),(1,1),(2,2),(3,0),(3,2)}],4)
counter_test_positivi += tester_fun(Ex2,[[[1,1,1],[0,1,0],[0,0,0],[1,0,1]],{(0,1),(0,2),(1,2),(2,2),(3,1)}],0)
counter_test_positivi += tester_fun(Ex2,[[[0,0],[0,1],[1,1]],{(0,0),(1,1),(2,1)}],1)
counter_test_positivi += tester_fun(Ex2,[[[0,0,0],[0,0,0],[0,0,0]],{(0,0),(0,1),(0,2),(1,0),(2,2)}],0)

print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


counter_test_positivi += tester_fun(Ex2,[[[1,0,0,0,0,1],[0,1,1,1,1,0],[1,1,0,0,0,0]],{(0,0),(0,1),(1,1),(1,2),(1,3),(1,4),(2,1)}],2)
counter_test_positivi += tester_fun(Ex2,[[[0,0,1],[0,0,1],[0,0,1]],{(0,2),(1,2),(2,2),(1,0),(1,1)}],3)
counter_test_positivi += tester_fun(Ex2,[[[1,0,1],[0,0,0],[0,0,0],[1,0,1]],{(0,1),(1,0),(1,2),(2,2),(3,1)}],0)
counter_test_positivi += tester_fun(Ex2,[[[1,1],[1,1],[1,1]],{(0,0),(0,1),(3,1)}],1)
counter_test_positivi += tester_fun(Ex2,[[[0,0,0],[0,1,0]],{(1,1)}],1)    
