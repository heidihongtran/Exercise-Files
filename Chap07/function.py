#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#We call main, then main calls kitten, and 
#kitten calls print with literal string 'Meow'. 
def main():
    kitten()

def kitten():
    print('Meow.')

if __name__ == '__main__': main()
