from random import randint
from time import sleep
from types import FunctionType
from assets import assets

arguments = list[str] | str
posType = dict[str, str | set[str]]
cmdOutput = tuple[posType, assets]

def typeOut(text: str, ): #speed: int
      i = 0
      x = str('')
      for char in text:
        x+=char
        i+=1
        sleep(0.02)
        print(char, end='', flush=True)
        if i % 96 == 0 and char == ' ':
            print('\n')
      return ''

def randomQuote(text: tuple[str]) -> str:
   return text[randint(0, len(text)-1)] 

def jdi(args: arguments, pos: posType, state: assets) -> cmdOutput:
    args = ' '.join(args)
    print(args)
    if args in pos.get('where'):
      typeOut(state.map.get(args).get("desc"))
      return (state.map.get(args), state)
    else:
      typeOut("Na toto místo nelze jít.")
      return (pos, state)

def checkExistence(args: str, checkAgainst: set[str]) -> bool:
      #Zatím neimplementováno - bude kontrolovat zkratky v příkazech
      return False

def seber(args: arguments, pos: posType, state: assets) -> cmdOutput:
      args = ' '.join(args)
      if args in pos.get("items"):
            pos.get("items").discard(args)
            state.inventory.add(args)
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Sebral jsi {args}"))
            return (pos, state)
      else: print(f"Nevidím v okolí {args}");return (pos, state)

def poloz(args: arguments, pos: posType, state: assets) -> cmdOutput:
      args = ' '.join(args)
      if args in state.inventory:
            state.inventory.discard(args)
            pos.get("items").add(args)
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Položil jsi {args}"))
            return (pos, state)
      else: print(f"Nemáš u sebe {args}");return (pos, state)

def kam(args: arguments, pos: posType, state: assets) -> cmdOutput:
      typeOut(f"Můžeš se dostat do:\n\n > {', '.join(pos.get('where'))}")
      return (pos, state)
            
def zkoumej(args: arguments, pos: posType, state: assets) -> cmdOutput:
      if isinstance(args, str):
            print(pos)
            for item in pos.get("zkoumej"):
                  pos.get("items").add(item)
            pos.get("zkoumej").clear()
            print(pos)
            typeOut(f"Nachází se zde:\n\n > {', '.join(pos.get('items'))}")
      return (pos, state)

def inventory(args: arguments, pos: posType, state: assets) -> cmdOutput:
      typeOut(f"V inventáři máš: \n\n > {', '.join(state.inventory)}") if len(state.inventory) != 0 else typeOut("Nemáš nic ve svém inventáři.")
      return (pos, state)

commands: dict[str, dict[str, FunctionType | str]] = {
      "jdi": {
            "callback": jdi,
            "desc": "Příkaz pro posun hráče na hráčem zadané místo.\n\n  Příklad: jdi Škola"
            }, 
      "seber": {
            "callback": seber,
            "desc": "Příkaz pro sebrání předmětu z aktuální lokace.\n\n  Příklad: seber Květina"
            },
      "polož":{
            "callback": poloz,
            "desc": "Příkaz pro položení předmětu v aktuální lokaci.\n\n  Příklad: polož Květina"
      },
      "zkoumej": {
            "callback": zkoumej,
            "desc": "Příkaz na prozkoumání aktuální lokace, předmětu v inventáři či objektu z aktuální lokace. \n\n  Příklad: zkoumej Škola     zkoumej Květina     zkoumej Policista"
            },
      "použij":{
           "desc": "" 
      }, 
      "save":{
            "desc": ""
      },
      "load":{
            "desc": ""
      }, 
      "info":{
            "desc": ""
      }, 
      "help": {
            "desc": ""
      },
      "inventory": {
            "callback": inventory,
            "desc": ""
      }, 
      "kam": {
            "callback": kam,
            "desc": "Příkaz na zobrazení všech dostupných lokací. \n\n  Příklad: kam"
            },
      "návod": {
            "desc": ""
      }
}
      