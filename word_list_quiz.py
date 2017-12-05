###################################################################
#text-tester.py
#Author:    Gavin Bernard
#Date:      Created 12/01/2017
#Brief:     Tests text files by retrieving certain words from them.
###################################################################

with open('words_alpha.txt.', 'r') as f:
    words = f.read().splitlines()

def total_number():
    total = 0
    for w in words:
        total += 1
    return total


def exactly_five():
    total = 0
    for w in words:
        if len(w) == 5:
            total += 1
    return total


def over_seven():
    total = 0
    for w in words:
        if len(w) > 7:
            total += 1
    return total


def total_char():
    total = 0
    for w in words:
        total += len(w)
    return total


def no_e():
    total = 0
    for w in words:
        if 'e' not in w:
            total += 1
    return total


def start_end():
    total = 0
    for w in words:
        if w[0] == w[-1]:
            total += 1
    return total


def three_a():
    a = 0
    total = 0
    for w in words:
        a = 0
        for letter in w:
            if letter == 'a':
                a += 1
        if a == 3:
            total += 1
    return total


def num_q():
    a = 0
    total = 0
    for w in words:
        for x in range(0,len(w)):
            if w[x:x+1] == 'q' and w[x:x+2] != 'qu':
                total += 1
                break
    return total


print(total_number())
print(exactly_five())
print(over_seven())
print(total_char())

print(no_e())
print(start_end())
print(three_a())
print(num_q())
