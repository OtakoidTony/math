import math
import time
from time import strftime

def fibo(n):return round((( (1+ math.sqrt(5) ) ** n ) - ( (1 - math.sqrt(5) )**n ))/( (2**n) * math.sqrt(5) )) # 1 1 2 3 5 8 ...

def test(n):
    temptime=1
    p=0
    while temptime<n+1:
        temp=1
        start_time = time.time()
        while temp<=200:
            p=fibo(temp)
            temp=temp+1
        print("%s" %(time.time() - start_time))
        temptime=temptime+1
