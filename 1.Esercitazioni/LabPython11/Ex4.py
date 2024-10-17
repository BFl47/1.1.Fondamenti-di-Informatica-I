def Ex4(file):
##    f=open(file,'r',encoding='UTF=8')
##    header=f.readline()
##    d={}
##    for riga in f:
##        riga=riga.strip().split(',')
##        oggetto=riga[0]
##        antenato=riga[1]
##        erede=riga[2]
##        if oggetto not in d:
##            d[oggetto]=[]
##            d[oggetto].append(antenato)
##            d[oggetto].append(erede)
##        if oggetto in d and antenato==d[oggetto][1]:
##            d[oggetto][1]=erede
##    return d  
    f=open(file,'r',encoding='UTF-8')
    header=f.readline()
    d={}
    for riga in f:
        riga=riga.strip().split(',')
        oggetto=riga[0]
        antenato=riga[1]
        erede=riga[2]
        if oggetto not in d:
            d[oggetto]=[]
            d[oggetto].append(antenato)
            d[oggetto].append(erede)
        if oggetto in d and antenato==d[oggetto][1]:
            d[oggetto][1]=erede
    return d
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Anello': ['Silvia', 'Paolo']})
    counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
    counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
