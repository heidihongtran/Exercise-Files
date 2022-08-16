#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
#The content of class Duck has 2 functions (or sometimes called methods): quack and walk.
#The ARGUMENT for a method inside of a class is always the word SELF (it's not a key word).
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
#In main, we have a variable called donald and we assign it from the class and that makes
#donald an object. So now donald is an OBJECT of the class duck. 
#And so we use the dot as the DE-REFERENCE OPERATOR to reference members of the object donald.
#And in this case, we're calling the method quack and walk.
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
