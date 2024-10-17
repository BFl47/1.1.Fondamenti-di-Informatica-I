import re

def Ex3(file):
##    fin=open(file,encoding='UTF=8')
##    s=fin.read().lower()
##    fin.close()
##    pattern=r'\b(\w)\w*(\w)\2\w*\1\b'
##    res=re.findall(pattern,s,re.IGNORECASE)
##    return len(res)

    f=open(file,'r',encoding='UTF-8')
    s=f.read().lower()
    f.close()
    pattern=r'\b(\w)\w*(\w)\2\w*\1\b'
    ris=re.findall(pattern,s,re.IGNORECASE)
    return len(ris)
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["file3_1.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["file3_2.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["file3_3.txt"] , 2)
    counter_test_positivi += tester_fun(Ex3, ["file3_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex3, ["file3_5.txt"] , 4)

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
