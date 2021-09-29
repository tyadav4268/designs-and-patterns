'''
Code to print following kind of pattern.
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

rows = int(input())
ch = rows + 96
dash = 2 * rows - 2
for i in range(rows):
    for j in range(dash - 2*i):
        print('-', end = '')
    for k in range(i+1):
        print(chr(ch), end = '')
        if i != 0:
            print('-', end = '')
        ch = ch - 1
    ch = ch + 1
    for m in range(i):
        ch = ch + 1
        print(chr(ch), end = '')
        if m != i - 1:
            print('-', end = '')
    ch = rows + 96
    for j in range(dash - 2*i):
        print('-', end = '')
    print()
for i in range(rows - 1):
    for j in range(2 + 2*i):
        print('-', end = '')
    for l in range(rows - 1 - i, 0, -1):
        print(chr(ch), end = '')
        if i != rows - 2:
            print('-', end = '')
        ch = ch - 1
    ch = ch + 1
    for m in range(rows - i - 2, 0, -1):
        ch = ch + 1
        print(chr(ch), end = '')
        if m != 1:
            print('-', end = '')
    ch = rows + 96
    for n in range(2 + 2*i):
        print('-', end = '')
    print()
