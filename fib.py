"""
this file contains some custom modules like
    fib
"""
data = { } 
def fib(n): 
    """
    fib(n) --> returns nth term of fibanacii series
    """
    if n in data : 
        return data[n]
    if n == 1 : 
        return 0
    elif n == 2 : 
        return 1
    else  : 
        ans =  fib(n-1) + fib(n-2)
        data[n] = ans
        return ans 

if __name__ == "__main__" : 
    nterms = int(input("Enter number of terms : "))
    c = 1 
    while c <= nterms : 

        ans  = fib(c)
        print(ans,end=', ',flush=True)
        c += 1
