import re

def Ex2(file):
##        f=open(file, encoding='UTF=8')
##        s=f.read()
##        f.close()
##        pattern=r'\W*\b\w*(\w)\w*(\w)\w*\b\W*\b\w*\2\w*\1\w*\b\W*'
##        ris=re.findall(pattern,s,re.IGNORECASE)
##        return len(ris)

        f=open(file,'r',encoding='UTF-8')
        s=f.read()
        f.close()
        pattern=r'\b\w*(\w)\w*(\w)\w*\b\W*\b\w*\2\w*\1\w*\b'
        ris=re.findall(pattern,s,re.IGNORECASE)
        return len(ris)
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ["file2_1.txt"] , 2)
    counter_test_positivi += tester_fun(Ex2, ["file2_2.txt"] , 3)
    counter_test_positivi += tester_fun(Ex2, ["file2_3.txt"] , 4)
    counter_test_positivi += tester_fun(Ex2, ["file2_4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex2, ["file2_5.txt"] , 4)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
