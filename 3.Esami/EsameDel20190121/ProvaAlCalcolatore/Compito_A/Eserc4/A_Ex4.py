from tester import tester_fun

def A_Ex4(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(file,'r',encoding='UTF-8')
    f.readline()
    quadri = {}
    for riga in f:
        riga = riga.strip().split(',')
        aquirente = riga[0]
        venditore = riga[1]
        pittore = riga[2]
        if aquirente not in quadri:
            quadri[aquirente] = []
        if venditore == '':
            quadri[aquirente].append(pittore)
        else:
            if venditore in quadri and pittore in quadri[venditore]:
                quadri[venditore].remove(pittore)
                quadri[aquirente].append(pittore)                
    f.close()
    l = []
    massimo = 0
    for key in quadri:
        if len(quadri[key])> massimo:
             massimo = len(quadri[key])
    for key in quadri:
        if len(quadri[key]) == massimo:
            l.append(key)
    l.sort()
    return l
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['vendite1.csv'] ,['Mario'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite2.csv'] ,['Gianni', 'Mario', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite3.csv'] ,['Gianni', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite4.csv'] ,['Gianni', 'Maria', 'Paolo'] )
counter_test_positivi += tester_fun(A_Ex4, ['vendite5.csv'] ,['Paolo'] )

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
