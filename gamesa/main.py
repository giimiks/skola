#do 29.12.2022 - 2,5h ztraceno
#28.12.2022 - 1h session

import assets as currentState
from random import randint
from time import sleep

def typeOut(text: str, speed: int) -> None:
    i = 0
    x = str('')
    for char in text:
        x+=char
        i+=1
        sleep(speed)
        print(char, end='', flush=True)
        if i % 96 == 0 and char == ' ':
            print()
def randomQuote(text: tuple[str]) -> str:
   return text[randint(0, len(text)-1)] 

def jdi(args, pos):
    args.pop(0)
    args = ' '.join(args)
    if args in pos.get('where'):
        return currentState.map.get(args)
    else: return pos

commands = {"jdi": jdi, "seber":{}, "polož":{}, "zkoumej":{}, "použij":{}, "save":{}, "load":{}, "info":{}, "help": {}}

position = currentState.map.get("Karla Čapka")
inventory = currentState.inventory

while True:
    print(position)
    prompt = input(typeOut(str(randomQuote(currentState.quotes) + ' > '), 0.05)).split(' ')
    if prompt[0] in commands:
        print('true')
        position = commands.get(prompt[0])(prompt, position)
        print(position)
            



