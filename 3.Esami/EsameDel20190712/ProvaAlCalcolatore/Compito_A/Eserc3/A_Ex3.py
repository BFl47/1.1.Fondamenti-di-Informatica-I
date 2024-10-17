from tester import tester_fun

def A_Ex3(file):
    f = open(file,'r',encoding='UTF-8')
    testo = f.read().split()
    f.close()
    d = {}
    for i in range(len(testo)):
        testo[i] = int(testo[i])
    print(testo)
    for i in range(len(testo)):
        num = testo[i]
        if i == 0:
            d[num] = []
        else:
            if num not in d:
                d[num] = []
            if testo[i-1] not in d[num]:
                d[num].append(testo[i-1])
                d[num].sort()
    return d
        
       
                          
###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],{1 : [], 3: [1, 7, 24], 24 : [2, 3, 12], 12 : [3], 8 : [8,12], 7 : [8], 2 : [24]})
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],{1 : [1]})
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'],{0 : [], 1 : [0], 2 : [1], 3: [2], 4 : [3], 5 : [4], 6 : [5], 7 : [6], 8 : [7], 9 : [8] })
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],{-11: [12], 12: [-11], 3 : [-11, 4], 4 : [3]})
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],{1 : [1, 24], 3: [7, 24], 24 : [3, 12], 12 : [3], 8 : [8,12], 7 : [8]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
