from tester import tester_fun

def A_Ex4(file):
    f = open(file,'r',encoding='UTF-8')
    nomi = f.readline().strip().split(',')
    ris = {}
    for nome in nomi:
        ris[nome] = [0,0,0,0] #tempo,n_partecipate,n_vinte,n_ultimo
        
    for riga in f:
        riga = riga.strip().split(',')
        iultimo = -1
        iprimo = -1
        for i in range(len(riga)):
            riga[i] = int(riga[i])
            if riga[i] > 0:
                ris[nomi[i]][1] += 1
                if iultimo < 0 or riga[i] > riga[iultimo]:
                    iultimo = i
                if iprimo < 0 or riga[i] < riga[iprimo]:
                    iprimo = i
                if ris[nomi[i]][0] == 0 or riga[i] < ris[nomi[i]][0]:
                    ris[nomi[i]][0] = riga[i]
        ris[nomi[iprimo]][2] += 1
        ris[nomi[iultimo]][3] += 1
    f.close()
    return ris
                
        
        
            

                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['maratone1.csv'],{'Mario': [130, 3, 0, 1], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone2.csv'],{'Mario': [111, 3, 1, 0], 'Paolo': [112, 3, 1, 1], 'Gianna': [113, 2, 1, 0], 'Giulia': [114, 3, 1, 1], 'Riccardo': [115, 2, 0, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone3.csv'],{'Mario': [135, 2, 0, 0], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1], 'Riccardo': [132, 1, 0, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone4.csv'],{'Mario': [121, 4, 1, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 1], 'Riccardo': [132, 1, 0, 0], 'Melania': [124, 3, 1, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone5.csv'],{'Mario': [121, 4, 2, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 2], 'Riccardo': [132, 1, 0, 1]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
