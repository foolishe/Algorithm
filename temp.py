def genfib():
    fib1=1 #fib(n-1)
    fib2=0 #fib(n-2)
    while True:
        #fib(n)=fib(n-1)+fib(n-2)
        n=fib1+fib2
        yield n 
        fib2=fib1
        fib1=next#fib(n+1)=next+fib(n-1)
import os,ipython
os.system(ipython.start_ipython())
#