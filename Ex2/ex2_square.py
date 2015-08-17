#!/usr/bin/env python3
# A function which prints a rhombus within a square
# with the dimensions choosen by user
def square_printing(n):
    if n==1:
        print('###')
        print('#*#')
        print('###')
        raise SystemExit
    
    #as long as not one creates pattern for both the 2 upper and 2 lower
    #lines and by loop all other lines
    else:
        size=n*2+1
    print('#'*size)
    print('#'+' '*(n-1)+'*'+' '*(n-1)+'#')
    
    #making half way printing of the inside square
    x=0
    while x<(n-1):
        print('#'+' '*(n-x-2)+'*'+' '*(2*x+1)+'*'+' '*(n-x-2)+'#')
        x+=1
        
    #making of the other half
    a=x
    while x>1:
        print('#'+' '*(a-x+1)+'*'+' '*((n*2)-2*(a-x)-5)+'*'+' '*(a-x+1)+'#')
        x-=1
    print('#'+' '*(n-1)+'*'+' '*(n-1)+'#')
    print('#'*size) 

#Here to help you test your code.
if __name__=="__main__":  #If we are the main script, and not imported
    from sys import argv
    try:
        n = int(argv[1])
    except:
        n = int(input("Please enter a positive integer: "))
    square_printing(n)
        
