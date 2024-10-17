import re

def Ex2(file):
##    fin=open(file,encoding='UTF-8')
##    s=fin.read().lower()
##    fin.close()
##    pattern=r'\b\w*(\w{2})\w*\b\W*\b\w*\1\w*\b\W*\b\w*\1\w*\b'
##    res=re.findall(pattern,s,re.IGNORECASE|re.MULTILINE)
##    return len(res)

        f=open(file,'r',encoding='UTF-8')
        pattern=r'\w*(\w{2})\w*\W+\w*\1\w*\W+\w*\1\w*'
        count=0
        for riga in f:
           ris=re.finditer(pattern,riga,re.IGNORECASE)
           for m in ris:
               count+=1
        f.close()
        return count
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ["file2_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex2, ["file2_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex2, ["file2_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex2, ["file2_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex2, ["file2_5.txt"] , 5)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
