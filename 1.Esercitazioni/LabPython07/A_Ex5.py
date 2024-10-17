def A_Ex5(l):
##    l1=[]
##    for i in range(len(l)):
##        num=0
##        for j in range(len(l[i])):
##            num+=ord(l[i][j])
##        l1.append(num)
##    return l1
    l1=[]
    for i in range(len(l)):
        somma=0
        for j in range(len(l[i])):
            somma+=ord(l[i][j])
        l1.append(somma)
    return l1
                        

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
