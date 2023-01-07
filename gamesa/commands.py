import base64
from random import randint
from time import sleep
from types import FunctionType
from assets import assets
import json

arguments = list[str] | str
posType = dict[str, str | set[str]]
cmdOutput = tuple[posType, assets]

def typeOut(text: str, ): #speed: int
      i = 0
      x = str('')
      speed = 0.02 - (len(text) / 10000)
      for char in text:
            x+=char
            i+=1
            sleep(speed)
            print(char, end='', flush=True)
      return ''

def randomQuote(text: tuple[str]) -> str:
   return text[randint(0, len(text)-1)] 

def odcesti(txt: str):
    odcesteno = ''
    diakritika = 'áéěíóúůýščřžďťň'
    bezDiakritiky = 'aeeiouuyscrzdtn'
    for i in txt:
        if i in diakritika:
            odcesteno += bezDiakritiky[diakritika.index(i)]
        elif i.upper() in diakritika.upper():
            odcesteno += bezDiakritiky[diakritika.upper().index(i.upper())].upper()
        else:
            odcesteno += i
    return odcesteno

def checkExistence(args: str, checkAgainst: set[str]) -> list[str]:
      matches = []
      for item in checkAgainst:
            if odcesti(args[:3].lower()) == odcesti(item[:3].lower()):
                  matches.append(item)
      return matches  

def jdi(args: arguments, pos: posType, state: assets) -> cmdOutput:
    args = ' '.join(args)
    if args in pos.get('where'):
      typeOut(state.map.get(args).get("desc"))
      return (state.map.get(args), state)
    else:
      typeOut("Na toto místo nelze jít.")
      return (pos, state)

 

def seber(args: arguments, pos: posType, state: assets) -> cmdOutput:
      print(pos.get("items"))
      print(pos.get("zkoumej"))
      args = ' '.join(args)
      matchesInventory = checkExistence(args, pos.get("items"))
      if len(matchesInventory) == 1:
            pos.get("items").remove(matchesInventory[0])
            state.inventory.append(matchesInventory[0])
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Sebral jsi {matchesInventory[0]}"))
      elif len(matchesInventory) > 1:
            typeOut(f"Nejednoznačný vstup příkazu.")
            selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)}"))
            pos.get("items").remove(selection);state.inventory.append(selection);state.map.get(pos.get("name")).update(pos);typeOut((f"Sebral jsi {matchesInventory[0]}")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
      else: print(f"Nevidím v okolí {args}")
      return (pos, state)

def poloz(args: arguments, pos: posType, state: assets) -> cmdOutput:
      args = ' '.join(args)
      matchesInventory = checkExistence(args, state.inventory)
      if len(matchesInventory) == 1:
            pos.get("items").append(matchesInventory[0])
            state.inventory.remove(matchesInventory[0])
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Položil jsi {matchesInventory[0]}"))
      elif len(matchesInventory) > 1:
            typeOut(f"Nejednoznačný vstup příkazu.")
            selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)}"))
            pos.get("items").append(matchesInventory[0]);state.inventory.remove(selection);state.map.get(pos.get("name")).update(pos);typeOut((f"Položil jsi {matchesInventory[0]}")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
      else: print(f"Nevidím v okolí {args}")
      return (pos, state)

def kam(args: arguments, pos: posType, state: assets) -> cmdOutput:
      typeOut(f"Můžeš se dostat do:\n\n > {', '.join(pos.get('where'))}") if pos.get('where') != 0 else typeOut("Nemůžeš se odsud nikam dostat. Něco ti brání v cestě.")
      return (pos, state)
            
def zkoumej(args: arguments, pos: posType, state: assets) -> cmdOutput:
      if args[:3] == "zko":
            if len(pos.get("zkoumej")) != 0 or len(pos.get("items")) != 0:
                  for item in pos.get("zkoumej"):
                        pos.get("items").append(item)
                  pos.get("zkoumej").clear()
                  state.map.get(pos.get("name")).update(pos)
                  typeOut(f"Nachází se zde:\n\n > {', '.join(pos.get('items'))}")
            else: typeOut("Nenachází se zde žádné předměty.")
            if len(pos.get("obstacles")) != 0:
                  typeOut(f"V cestě dál ti zde brání:\n\n {', '.join(pos.get('obstacles'))}")
      else:
            matchesInventory = checkExistence(args[0], state.inventory)
            matchesObstacles = checkExistence(args[0], state._obstacles)
            if len(matchesInventory) == 1:
                  typeOut(state._items.get(matchesInventory[0]).get("desc"))
            elif len(matchesInventory) > 1:
                  typeOut(f"Nejednoznačný vstup příkazu.")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)}"))
                  typeOut(state._items.get(selection).get("desc")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
            elif len(matchesObstacles) == 1:
                  typeOut(state._obstacles.get(matchesObstacles[0]).get("desc"))
            elif len(matchesObstacles) > 1:
                  typeOut(f"Nejednoznačný vstup příkazu.")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesObstacles)}"))
                  typeOut(state._obstacles.get(selection).get("desc")) if selection in matchesObstacles else typeOut("Nezadal jsi správné slovo ze seznamu.")  
            else: typeOut("Toto nelze zkoumat. Buď je to předmět a nemáš ho v inventáři nebo je to objekt, který se v aktuální lokaci nenachází.")      
      return (pos, state)

def inventory(args: arguments, pos: posType, state: assets) -> cmdOutput:
      typeOut(f"V inventáři máš: \n\n > {', '.join(state.inventory)}") if len(state.inventory) != 0 else typeOut("Nemáš nic ve svém inventáři.")
      return (pos, state)

def pouzij(args: arguments, pos: posType, state: assets) -> cmdOutput:
      #TODO: matchArgs je vždy první argument uživatelova vstupu, použít při podmínce pouze args jako list
      #args = ' '.join(args)
      
      matchArgs = checkExistence(' '.join(args), state.inventory)
      if args:
            if len(matchArgs) == 1:
                  matchArgs = checkExistence(' '.join(args), state.inventory)
                  if "self" in state._items.get(matchArgs[0]).get("use"):
                        state.inventory.remove(matchArgs[0])
                        state.effects.append(state._items.get(matchArgs[0]).get("effect"))
                        typeOut(state._items.get(matchArgs[0]).get("effect"))
                  else: 
                        typeOut(f"Předmět {matchArgs[0]} nelze použít na sebe.")      
            elif len(matchArgs) > 1: 
                  typeOut(f"Nejednoznačný vstup příkazu.")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchArgs)}"))
                  if selection in matchArgs:
                        if "self" in state._items.get(selection).get("use"):
                              state.effects.append(state._items.get(selection).get("effect"))
                              typeOut(f'Použil jsi předmět a byl ti přidán efekt: {state._items.get(selection).get("effect")}')
                        else: typeOut(f"Předmět {selection} nelze použít na sebe.")
                  else: typeOut("Nezadal jsi správné slovo ze seznamu.")      
      else:
            
            query: dict[str, list] = {"firstItem": [], "secondItem": []}
            order: str = "firstItem"
            for word in args:
                  print(word)
                  if word != 'na':
                        query.get(order).append(word)
                  else: order = "secondItem"
            first = checkExistence(' '.join(query.get("firstItem")), state.inventory)
            secondItems = checkExistence(' '.join(query.get("secondItem")), state.inventory)
            secondObstacles = checkExistence(' '.join(query.get("secondItem")), pos.get("obstacles"))
            if len(first) == 1:
                  if len(secondItems) == 1:
                        print(first + secondItems)
                        if secondItems[0] in state._items.get(first[0]).get("use"):
                              state.inventory.remove(first[0])
                              state.inventory.remove(secondItems[0])
                              state.effects.append(state._items.get(first[0])).get("effect")
                  elif len(secondItems) > 1:
                        typeOut(f"Nejednoznačný vstup příkazu.")
                        selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(secondItems)}"))
                        if selection in secondItems:
                                    state.inventory.remove(first[0])
                                    state.inventory.remove(selection)
                                    state.effects.append(state._items.get(selection).get("effect"))  
                        else: typeOut("Nezadal jsi správné slovo ze seznamu.") 
                  elif len(secondObstacles) == 1:
                        if first[0] in state._obstacles.get(secondObstacles[0]).get("killableBy"):
                              pos.get("obstacles").remove(secondObstacles[0])
                              typeOut(state._obstacles.get(secondObstacles[0]).get("afterkill"))
                  elif len(secondObstacles) > 1:
                        typeOut(f"Nejednoznačný vstup příkazu.")
                        selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(secondObstacles)}"))
                        if selection in matchArgs:
                              pos.get("obstacles").remove(selection)
                              typeOut(state._obstacles.get(selection).get("afterkill"))
                 
                        else: typeOut("Nezadal jsi správné slovo ze seznamu.") 
                  else: typeOut(f"Nelze použít {first[0]} na {' '.join(query.get('secondItems'))}. Buď je to předmět a nemáš ho v inventáři nebo je to objekt, který se v aktuální lokaci nenachází.")
            elif len(first) > 1:
                  typeOut(f"Nejednoznačný vstup příkazu.")
                  selectionFirst = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(first)}")) 
                  if selectionFirst in first:
                        if len(secondItems) == 1:
                              if secondItems[0] in state._items.get(selectionFirst).get("use"):
                                    state.inventory.remove(selectionFirst)
                                    state.inventory.remove(secondItems[0])
                                    state.effects.append(state._items.get(selectionFirst)).get("effect")
                        elif len(secondItems) > 1:
                              typeOut(f"Nejednoznačný vstup příkazu.")
                              selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(secondItems)}"))
                              if selection in secondItems:
                                          state.inventory.remove(selectionFirst)
                                          state.inventory.remove(selection)
                                          state.effects.append(state._items.get(selection).get("effect"))  
                              else: typeOut("Nezadal jsi správné slovo ze seznamu.") 
                        elif len(secondObstacles) == 1:
                              if first[0] in state._obstacles.get(secondObstacles[0]).get("killableBy"):
                                    pos.get("obstacles").remove(secondObstacles[0])
                                    typeOut(state._obstacles.get(secondObstacles[0]).get("afterkill"))
                        elif len(secondObstacles) > 1:
                              typeOut(f"Nejednoznačný vstup příkazu.")
                              selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(secondObstacles)}"))
                              if selection in matchArgs:
                                    pos.get("obstacles").remove(selection)
                                    typeOut(state._obstacles.get(selection).get("afterkill"))
                              else: typeOut("Nezadal jsi správné slovo ze seznamu.") 
                        else: typeOut(f"Nelze použít {selectionFirst} na {' '.join(query.get('secondItems'))}. Buď je to předmět a nemáš ho v inventáři nebo je to objekt, který se v aktuální lokaci nenachází.")
                  else: typeOut("Nezadal jsi správné slovo ze seznamu.") 
      return (pos, state)

def save(args: arguments, pos: posType, state: assets) -> cmdOutput:
      saveData = {"pos": pos, "map": state.map, "inv": state.inventory, "money": state.money, "effects": state.effects}
      with open(".savefile", "w", encoding='utf8') as file:
            json.dump(saveData, file, ensure_ascii=False, default=tuple)
      return (pos, state)

def load(args: arguments, pos: posType, state: assets) -> cmdOutput:
      with open(".savefile", "r", encoding='utf8') as file:
            data: dict[str, dict[str, str | list[str]  | int ]] = json.loads(file.read())
            state.map = data.get("map")
            state.money = data.get("money")
            state.effects = set(data.get("effects"))
            state.inventory = set(data.get("inv"))

                  
            pos = data.get("pos")

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
            "callback": pouzij,
            "desc": "Příkaz na použití předmětu na jiný předmět nebo překážku. \n\n  Příklad: použij Telefon     použij Pistole na Zombík" 
      }, 
      "save":{
            "callback": save,
            "desc": "Save"
      },
      "load":{
            "callback": load,
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
      