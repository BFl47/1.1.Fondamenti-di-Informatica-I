from tester import tester_fun

def A_Ex1(l):
##    massimo=0
##    piufreq=''
##    for i in range(len(l)):
##        for j in range(len(l[i])):
##            if l[i].count(l[i][j])>massimo and ord(l[i][j])>=ord('a') and ord(l[i][j])<=ord('z') and l[i][j]>piufreq:
##                massimo=l[i].count(l[i][j])
##                piufreq=l[i][j]     
##    return piufreq

    piufreq=''
    massimo=0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        count=0
        for elem in l:
            if c in elem:
                count+=1
        if count>massimo:
            massimo=count
            piufreq=c
        elif count==massimo and c>piufreq:
            piufreq=c
    return piufreq
    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(A_Ex1, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(A_Ex1, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")


    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
