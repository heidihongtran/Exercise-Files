#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str): # str is a built-in class, 
    def __str__(self): # This is a type of a string that
    #everytime I print it, it'll print backwards.   
        return self[::-1] 

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
