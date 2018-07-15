# -*- coding: utf-8 -*-

import json

print('- Turing Mahcine Runner -', end = '\n\n')

print('Machine Name: ', end = '')
name = input()
file = open('Turing Machines\\' + name + '.json', 'r')
Machine = json.loads(file.readline())

Dictionary = { '#' : 0 }
i = 1
length = len(Machine['Alphabet'])
while i < length:
    Dictionary[Machine['Alphabet'][i]] = i
    i += 1

print('Tape: ', end = '')
tape = input()
Tape = []
q = -1
while True:
    p = tape.find(' ', q + 1)
    if p == -1:
        Tape.append(Dictionary[tape[q + 1 : len(tape)]])
        break
    else:
        Tape.append(Dictionary[tape[q + 1 : p]])
        q = p

State = 0
Index = 0
length = len(Tape)
while True:
    if Index >= length:
        Input = 0
        Tape.append(0)
        length += 1
    elif Index < 0:
        Input = 0
        Tape.insert(0, 0)
        length += 1
        Index = 0
    else:
        Input = Tape[Index]
    Tape[Index] = Machine['Commands'][State][Input][0]
    Index += Machine['Commands'][State][Input][1]
    State = Machine['Commands'][State][Input][2]

    if State == -1:
        break

while Tape[0] == 0:
    Tape.pop(0)
while Tape[-1] == 0:
    Tape.pop()

i = 0
length = len(Tape)
while i < length:
    print(Machine['Alphabet'][Tape[i]], end = ' ')
    i += 1

input()
