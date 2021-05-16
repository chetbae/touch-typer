from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import sys, os, random, string
from time import sleep

def main():
    num_of_rounds = 0
    clear()

    print("touch-typing starting...💻\n")

    try:
        file = open("1-1000.txt", "r")
    except: 
        print("text file missing")
        exit(1)

    # prompt and collect user input
    options = landing(num_of_rounds)
    for i in range(20):
        sleep(1 / (1 + i))
        print("")
    print(options)
    # generate array from choices
    text = []
    lines = file.readlines()
    random.shuffle(lines)
    lines = lines[0:20]
    lines = ''.join(lines).replace('\n', ' ')
    char_arr = list(lines)

    if len(options) != 0:
        for i, c in enumerate(char_arr):
            if c not in options and c != ' ': char_arr[i] = random.choice(options)
            
    # generate 
    num_of_rounds += 1

def clear():
    print(chr(27) + "[2J")

def gui(user_keys):
    clear()


def landing(x):
    if x > 0: print(chr(27) + "[2J")

    questions = [{
        'type': 'checkbox',
        'message': 'Pick your poison:',
        'name': 'keys',
        'choices': [
            {
                'name': 'Middle Row'
            },
            {
                'name': 'Bottom Row'
            },
            {
                'name': 'Top Row'
            }
        ]
    }]
    selections = prompt(questions)["keys"]
    opt = []
    if 'Middle Row' in selections:
        opt.extend(['a','s','d','f','g','h','j','k','l'])
    if 'Bottom Row' in selections:
        opt.extend(['z','x','c','v','b','n','m'])
    if 'Top Row' in selections:
        opt.extend(['q','w','e','r','t','y','u','i','o','p'])
    return opt

if __name__ == '__main__':
    main()