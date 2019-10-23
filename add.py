"""
add module is used add two number 
"""
import os
def add(x,y):
    """
    add(x,y) -> x + y
    example : 

    >>>add(4,5)
    9
    """
    return x + y 


def sub(x,y):
    return x-y

if __name__ == "__main__" :
    
    os.system("cls")
    print("*"*60)
    print("*"*60)
    print("\n")
    x,y = map(int,input("x,y : ").split(","))
    print(f"x = {x}\ny = {y}\n x + y = {add(x,y)}")
    print("\n")
    print("*"*60)
    print("*"*60)
    
