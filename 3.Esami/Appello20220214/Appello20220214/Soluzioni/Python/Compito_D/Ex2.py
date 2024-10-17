def Ex2(l,s,t):
    ris = []
    for parola in l:
        compatibile = True
        for i in range(5):
            if t[i] == 2 and parola[i] != s[i]:
                compatibile = False
            if t[i] == 1 and (s[i] not in parola or parola[i]==s[i]):
                compatibile = False
            if t[i] == 0 and s[i] in parola:
                compatibile = False
            if t[i] == 1 and s[i] not in parola:
                compatibile = False
        if compatibile:
            ris.append(parola)
    return ris
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [['caste','pesta','paste','pance'],'pinza',(2,0,0,0,1)],['paste'])
    counter_test_positivi += tester_fun(Ex2, [['caste','cesta','pesta','pance'],'pinza',(2,0,0,0,1)],[])
    counter_test_positivi += tester_fun(Ex2, [['carte','sorta','sarte'],'folte',(0,2,0,2,0)],['sorta'])
    counter_test_positivi += tester_fun(Ex2, [['croce','astro','torsa'],'sorta',(1,1,1,1,1)],['astro'])
    counter_test_positivi += tester_fun(Ex2, [['clero','diego','truce','frego','pesto'],'testo',(0,1,0,0,2)],['clero','diego','frego'])

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, [['forse','afghe','aeghi','aeczf'],'abcde',(2,0,0,0,1)],['aeghi'])
    counter_test_positivi += tester_fun(Ex2, [['forse','afghe','aighe','aecfg'],'abcde',(2,0,0,0,1)],[])
    counter_test_positivi += tester_fun(Ex2, [['capta','aoecd','aoceu'],'noprq',(0,2,0,0,0)],['aoecd','aoceu'])
    counter_test_positivi += tester_fun(Ex2, [['baced','edbca','abcde'],'abcde',(1,1,1,1,1)],['edbca'])
    counter_test_positivi += tester_fun(Ex2, [['cdero','erdso','pcedo','drexo','erduo'],'perdo',(0,1,1,1,2)],['cdero','erdso','drexo','erduo'])

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
