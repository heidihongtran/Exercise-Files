#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1(f): #f1 takes the argument f.
        def f2():
            print('This is before the function call.')
            f()
            print('This is after the function call.')
        return f2

@f1 # This is called a DECORATOR, followed directly by the  
# function definition and it takes that function & passed it
# as an argument to the decorator function and it returns and 
# it assigns that name of f3 to the wrapper itself.
# So now can't call f3 directly, can only call it thru the wrapper.
# f3 now is wrpped inside that decorator function.
def f3():
    print('This is f3.')

f3()
