from tester import tester_fun

def A_Ex2(M):
    """inserisci qui la tua soluzione"""
    ris = []
    righe = len(M)
    colonne = len(M[0])
    for j in range(colonne):
        col = []
        for i in range(righe):
            if M[i][j]!=0:
                col.append(M[i][j])
        if len(col) != 0:
            somma = sum(col)
            n = somma/len(col)
            k = round(n,2)
            ris.append(k)
        else:
            ris.append(0)
    return ris
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[24, 30, 0], [22, 0, 28], [23, 29, 0], [18, 0, 0]]],[21.75, 29.50, 28.0])
counter_test_positivi += tester_fun(A_Ex2, [[[0, 26, 30, 0], [0, 24, 30, 18]]],[0, 25.0, 30.0, 18.0])
counter_test_positivi += tester_fun(A_Ex2, [[[0, 26], [0, 24],[19, 23],[20, 0]]],[19.5, 24.33])
counter_test_positivi += tester_fun(A_Ex2, [[[18], [19], [20], [21], [0], [22]]],[20])
counter_test_positivi += tester_fun(A_Ex2, [[[25, 28, 30, 26], [27, 30, 30, 24], [25, 28, 30, 26]]],[25.67, 28.67, 30.0, 25.33])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


