# -*- coding: utf-8 -*-

import json

print('- Turing Machine Builder -', end = '\n\n')

print('Machine Name: ', end = '')
name = input()

print('Alphabet (except the Blank Symbol #): ', end = '')
alphabet = input()
Alphabet = ['#']
Dictionary = { '#' : 0 }
q = -1
i = 1
while True:
    p = alphabet.find(' ', q + 1)
    if p == -1:
        char = alphabet[q + 1 : len(alphabet)]
        Alphabet.append(char)
        Dictionary[char] = i
        break
    else:
        char = alphabet[q + 1 : p]
        Alphabet.append(char)
        Dictionary[alphabet[q + 1 : p]] = i
        q = p
        i += 1
CharAmount = len(Alphabet)

print('Amount of States (except the Start State q0:0 and the Halt State h:-1): ', end = '')
StateAmount = int(input())
print('input command like \'output direction state\' (if there is no command, press Enter)')
Commands = []
i = 0
while i <= StateAmount:
    Commands.append([])
    j = 0
    while j < CharAmount:
        print('q' + str(i) + ',' + Alphabet[j] + ': ', end = '')
        command = input()
        Commands[-1].append([])
        if command == '':
            Commands[-1][-1] = ['#', 0, -1]
        else:
            Commands[-1][-1] = []
            #output
            p1 = command.find(' ')
            Commands[-1][-1].append(Dictionary[command[0 : p1]])
            #direction
            p2 = command.find(' ', p1 + 1)
            Commands[-1][-1].append(int(command[p1 + 1 : p2]))
            #state
            Commands[-1][-1].append(int(command[p2 + 1 : len(command)]))
        j += 1
    i += 1

output = json.dumps({ 'Alphabet' : Alphabet, 'Commands' : Commands })
file = open('Turing Machines\\' + name + '.json', 'w')
file.writelines(output)
file.close()

print('Successfully built ' + name + '!')
input()
