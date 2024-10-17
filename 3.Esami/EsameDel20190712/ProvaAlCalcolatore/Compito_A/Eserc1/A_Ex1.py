from tester import tester_fun

def A_Ex1(s1,s2):
    dis = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1
        return dis
    if len(s1) > len(s2):
        dis = len(s1) - len(s2)
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                dis += 1
        return dis
    if len(s2) > len(s1):
        dis = len(s2) - len(s1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1
        return dis
        

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["aceto","aceto"],0)
counter_test_positivi += tester_fun(A_Ex1, ["pippo","pappa"],2)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","ace"],2)
counter_test_positivi += tester_fun(A_Ex1, ["alba","albino"],3)
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"],5)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
