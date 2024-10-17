from tester import tester_fun

def A_Ex2(s1,s2):
##   s=''
##   for c in s1:
##      if (s1.count(c)== s2.count(c)) and not (c in s):
##         s+=c
##         #print(s)
##   return len(s)
   s=''
   for c in s1:
      if (s1.count(c)==s2.count(c)) and not c in s:
         s+=c
   return len(s)


###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casa blue'],4)
counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casata blue'],3)
counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casacca blue sole'],3)
counter_test_positivi += tester_fun(A_Ex2, ['','casa blue'],0)
counter_test_positivi += tester_fun(A_Ex2, ['',''],0)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
