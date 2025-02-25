import re

def Ex1(file):
##    fin=open(file,encoding='UTF-8')
##    s=fin.read()
##    fin.close()
##    pattern=r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
##    res=re.findall(pattern,s,re.IGNORECASE)
##    return len(res)

    f=open(file,'r',encoding='UTF-8')
    s=f.read().lower()
    f.close()
    pattern=r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
    ris=re.findall(pattern,s,re.IGNORECASE)
    return len(ris)
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ["file1_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex1, ["file1_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex1, ["file1_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_5.txt"] , 5)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
