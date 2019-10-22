"""
this file contains some custom modules like
    fib
"""
def fib(n): 
    """
    fib(n) --> returns nth term of fibanacii series
    """
    if n == 1 : 
        return 0
    elif n == 2 : 
        return 1
    else  : 
        return fib(n-1) + fib(n-2)

if __name__ == "__main__" : 
    nterms = int(input("Enter number of terms : "))
    c = 1 
    while c <= nterms : 

        ans  = fib(nterms)
        print(ans,end=', ',flush=True)
        c += 1
