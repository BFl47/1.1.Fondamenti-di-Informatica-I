from tester import tester_fun

def A_Ex4(file1,file2):
    '''inserisci qui la tua soluzione'''
    rank = {}
    f1 = open(file1,'r',encoding='UTF-8')
    count = 1
    for riga in f1:
        riga = riga.strip().split()
        nome = riga[0]
        rank[nome] = count
        count += 1
    f1.close()
    
    f2 = open(file2,'r',encoding='UTF-8')
    vincitori = {}
    ris = set()
    for riga in f2:
        riga = riga.strip().split(',')
        gioc1 = riga[0]
        gioc2 = riga[1]
        set1 = int(riga[2])
        set2 = int(riga[3])
        if set1 > set2:
            if gioc1 in vincitori:
                vincitori[gioc1].add(gioc2)
            else:
                vincitori[gioc1] = {gioc2}
            if rank[gioc1] > rank[gioc2]:
                ris.add(gioc1)
        else:
            if gioc2 in vincitori:
                vincitori[gioc2].add(gioc1)
            else:
                vincitori[gioc2] = {gioc1}
            if rank[gioc2] > rank[gioc1]:
                ris.add(gioc2)
    f2.close()
    for k in rank:
        if k in vincitori and k not in ris:
            vincitori.pop(k)
    return vincitori
        
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri1.csv'],{'Federer':{ 'Medvedev', 'Djokovic'}, 'Nadal':{ 'Federer', 'Djokovic'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri2.csv'],{'Federer':{ 'Medvedev', 'Thiem','Djokovic'},'Nadal':{ 'Federer', 'Djokovic'},'Thiem':{'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri3.csv'],{'Medvedev':{ 'Federer'},'Thiem':{ 'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri4.csv'],{'Paperoga':{ 'Paperino'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri5.csv'],{'Paperoga':{ 'Pippo','Paperino'},'Pippo':{'Topolino','Paperoga'}})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
