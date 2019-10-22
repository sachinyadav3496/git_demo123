"""
this file contains some custom modules like
    fib
"""

def fib(nterms): 
    """
    fib(nterms) --> return first n terms of fibonacci series
    
    >>>fib(6)
    0, 1, 1, 2, 3, 5, 

    """
    start = 0
    end = 1
    print(start,end,sep=', ',end=', ')
    for var in range(nterms-2): 
        start,end=end,start+end
        print(end,end=', ')

if __name__ == "__main__" : 

    nterms = int(input("Enter number of terms : "))
    fib(nterms)
