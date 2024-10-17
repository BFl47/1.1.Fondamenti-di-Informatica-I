from tester import tester_fun

def A_Ex3(file):
    d = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        riga = riga.strip().split()
        for parola in riga:
            d[parola] = d.get(parola,0)+1    
    f.close()
    l = []
    massimo = 0
    for parola in d:
        if len(parola) >= massimo and d[parola] >= 3:
            massimo = len(parola)
    for parola in d:
        if len(parola) == massimo and d[parola] >= 3:
            l.append(parola)        
    l.sort()
    if len(l) == 0:
        return ''
    return l[0]
            
            
      
                          
###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],'albero')
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'],'casolare')
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],'')

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
