#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game) # Call function print_list

def print_list(o): # Define function print_list
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
