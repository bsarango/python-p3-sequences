#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    i=0
    while i < length:
        if len(fib_sequence) == 0:
            fib_sequence.append(0)
        elif len(fib_sequence) == 1:
            fib_sequence.append(1)
        else:
            fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
        i+=1
    print(fib_sequence)