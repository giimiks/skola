#do 28.12.2022 - 2,5h ztraceno
#28.12.2022 - 1h
#29.12.2022 - 7,75h
#30.12.2022 - 30min
#04.01.2023 - 15min
#07.01.2023 - 6,25h

from assets import *
from commands import commands, odcesti, typeOut, randomQuote

currentState = assets()
position: dict[str, str | list[str]] = currentState.map.get("Karla Čapka")

while True:
    executed = False
    print('\n')
    prompt: str | list[str] = input(f"{typeOut(randomQuote(currentState._quotes))} > ")
    if prompt != '':
        prompt = prompt.split(' ') if len(prompt.split(' ')) > 1 else prompt

        for command in commands:
            if True if isinstance(prompt, str) and odcesti(prompt[:3].lower()) == odcesti(command[:3].lower()) else odcesti(prompt[0][:3].lower()) == odcesti(command[:3].lower()):
                print('')
                prompt.pop(0) if not isinstance(prompt, str) else prompt
                callback: tuple[dict[str, str | set[str]], assets] = commands.get(command).get("callback")(prompt, position, currentState)
                position, currentState = callback
                executed = True
                break
    if not executed:
            typeOut("\nNeznámý příkaz.") 
        
                



