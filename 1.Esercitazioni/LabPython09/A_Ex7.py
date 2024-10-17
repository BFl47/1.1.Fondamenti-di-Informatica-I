def A_Ex7(file):
##    fin=open(file,encoding='UTF-8')
##    riga=fin.readline()
##    d={}
##    for riga in fin:
##        riga=riga.strip().split(',')
##        if int(riga[2])>int(riga[3]):
##            d[riga[0]]=d.get(riga[0],0)+3
##            d[riga[1]]=d.get(riga[1],0)+0
##                
##        elif int(riga[2])==int(riga[3]):
##            d[riga[0]]=d.get(riga[0],0)+1
##            d[riga[1]]=d.get(riga[1],0)+1
##                
##        else:
##            d[riga[0]]=d.get(riga[0],0)+0
##            d[riga[1]]=d.get(riga[1],0)+3
##    fin.close()
##    return d
    f=open(file,'r',encoding='UTF-8')
    header=f.readline()
    d={}
    for riga in f:
        riga=riga.strip().split(',')
        squadra1=riga[0]
        squadra2=riga[1]
        gols1=int(riga[2])
        gols2=int(riga[3])

        if gols1>gols2:
            d[squadra1]=d.get(squadra1,0)+3
            d[squadra2]=d.get(squadra2,0)+0
        elif gols1==gols2:
            d[squadra1]=d.get(squadra1,0)+1
            d[squadra2]=d.get(squadra2,0)+1
        else:
            d[squadra1]=d.get(squadra1,0)+0
            d[squadra2]=d.get(squadra2,0)+3
    f.close()
    return d
        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
