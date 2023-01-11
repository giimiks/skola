#do 28.12.2022 - 2,5h ztraceno
#28.12.2022 - 1h
#29.12.2022 - 7,75h
#30.12.2022 - 30min
#04.01.2023 - 15min
#07.01.2023 - 6,25h
#10.01.2023 - 1h
#11.01.2023 - 4h
#celkem - 24h

from assets import *
from commands import commands, odcesti, typeOut, randomQuote

currentState = assets()
position: dict[str, str | list[str]] = currentState.map.get("Karla Čapka")

typeOut("  _    _       _                _                           _                 _                       \n | |  | |     | |              | |                 /\      | |               | |                      \n | |__| | __ _| |__   __ _ _ __| |_ _____   __    /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___  ___ \n |  __  |/ _` | '_ \ / _` | '__| __/ _ \ \ / /   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \/ __|\n | |  | | (_| | |_) | (_| | |  | || (_) \ V /   / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/\__ \n |_|  |_|\__,_|_.__/ \__,_|_|   \__\___/ \_/   /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___||___/", 0.002)
print("\n")
typeOut("   ___        _                            _    _ _ _        \n  / __|___ __| |_ __ _   _____ _   _ _ ___| |_ | (_) |___  _ \n | (__/ -_|_-<  _/ _` | |_ / _` | | '_/ _ \ ' \| | | / / || |\n  \___\___/__/\__\__,_| /__\__,_| |_| \___/_||_|_|_|_\_\\_, |\n                                                        |__/ ", 0.002)                                                                                                      
print("\n\n\n")
typeOut("Tvé jméno, věk ani jiné atributy nejsou důležité. Máš jen jediný a to zcela jasný úkol - dostat se přes nástrahy a překážky Habartova do Tesca a koupit rohlíky.", 0.002)
print("\n")
typeOut("Zdali toho dosáhneš, je už jen na tobě. Na nic nečekej a jdi. Při nejhorším máš k dispozici 'návod'", 0.002)
print("\n\n")

while True:
    executed = False
    end = False
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
                if position.get("name") == "Tesco":
                    end = True
                executed = True
                break
    if end:
        typeOut("\nGratuluji. Prodral jsi se přes celý Habartov až do Tesca a koupil sis rohlíky. Hra tímto končí. Děkuji za zahrání.")
        while True:
            pass

    if not executed:
            typeOut("\nNeznámý příkaz.") 
        
                



