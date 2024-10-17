from tester import tester_fun

def A_Ex4(file):
    f = open(file,'r',encoding='UTF-8')
    d = {}
    giorno = 1
    for riga in f:
        riga = riga.strip().split(';')
        best = {}
        for perf in riga:
            perf = perf.strip().split('-') 
            agente = perf[0]
            importo = int(perf[1])
            best[agente] = importo            
            if agente not in d:
                d[agente] = []
        massimo = 0
        nome = []
        for agente in best:
            if best[agente] > massimo:
                massimo = best[agente]
        for agente in best:
            if best[agente] == massimo:
                nome.append(agente)
        for agente in nome:
            d[agente].append(giorno)
        giorno += 1
    f.close()
    return d
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{'Mario': [1, 2], 'Marco': [], 'Anna': [3,4], 'Aldo': [2], 'Antonio': [5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{'Mario': [2], 'Marco': [], 'Anna': [1,3,4], 'Aldo':[], 'Antonio':[5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{'Mario': [], 'Marco': [], 'Anna': [1,2,3,4,5], 'Antonio':[]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{'Mario': [1,4], 'Anna': [2,3,5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{'Mario': [1,2,4], 'Marco': [1,4], 'Anna': [1,3,4,5], 'Aldo': [2,3], 'Antonio': [5]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
