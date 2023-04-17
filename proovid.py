import sys, time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(0.2)

print_slow("Type whatever you want here     ")

import sys,time,random
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/50)
slow_type("kabrish")