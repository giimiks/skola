#do 29.12.2022 - 2,5h ztraceno
#28.12.2022 - 1h session
#29.12.2022 - 4h session (zatím)

from assets import *
from commands import commands, typeOut, randomQuote, arguments, cmdOutput

currentState = assets()
position: dict[str, str | set[str]] = currentState.map.get("Karla Čapka")

while True:
    print('\n')
    prompt: str | arguments = input(f"{typeOut(randomQuote(currentState.quotes))} > ")
    prompt = prompt.split(' ') if len(prompt.split(' ')) > 1 else prompt
    for command in commands:
        if True if isinstance(prompt, str) and prompt[:3] == command[:3] else prompt[0][:3] == command[:3]:
                print('\n')
                prompt.pop(0) if not isinstance(prompt, str) else prompt
                callback: cmdOutput = commands.get(command).get("callback")(prompt, position, currentState)
                position, currentState = callback
                



