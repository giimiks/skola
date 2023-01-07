from random import randint
from time import sleep
from types import FunctionType
from typing import Any
from assets import assets
import json

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

def jdi(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      args = ' '.join(args)
      matches = checkExistence(args, pos.get("where"))
      if len(matches) == 1:
            if matches[0] in pos.get('where'):
                  typeOut(state.map.get(matches[0]).get("desc"))
                  return (state.map.get(matches[0]), state)
      elif len(matches) > 1:
            typeOut(f"Nejednoznačný vstup příkazu. ")
            selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matches)} "))
            if selection in matches:
                  typeOut(state.map.get(selection).get("desc"))
                  return (state.map.get(selection), state)
            else: typeOut("Nezadal jsi správné slovo ze seznamu.")
      else:
            typeOut("Na toto místo nelze jít.")
      return (pos, state)

def seber(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      args = ' '.join(args)
      matchesInventory = checkExistence(args, pos.get("items"))
      if len(matchesInventory) == 1:
            pos.get("items").remove(matchesInventory[0])
            state.inventory.append(matchesInventory[0])
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Sebral jsi {matchesInventory[0]}"))
      elif len(matchesInventory) > 1:
            typeOut(f"Nejednoznačný vstup příkazu. ")
            selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)} "))
            pos.get("items").remove(selection);state.inventory.append(selection);state.map.get(pos.get("name")).update(pos);typeOut((f"Sebral jsi {matchesInventory[0]}")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
      else: print(f"Nevidím v okolí {args}")
      return (pos, state)

def poloz(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      args = ' '.join(args)
      matchesInventory = checkExistence(args, state.inventory)
      if len(matchesInventory) == 1:
            pos.get("items").append(matchesInventory[0])
            state.inventory.remove(matchesInventory[0])
            state.map.get(pos.get("name")).update(pos)
            typeOut((f"Položil jsi {matchesInventory[0]}"))
      elif len(matchesInventory) > 1:
            typeOut(f"Nejednoznačný vstup příkazu. ")
            selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)} "))
            pos.get("items").append(matchesInventory[0]);state.inventory.remove(selection);state.map.get(pos.get("name")).update(pos);typeOut((f"Položil jsi {matchesInventory[0]}")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
      else: print(f"Nevidím v okolí {args}")
      return (pos, state)

def kam(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      typeOut(f"Můžeš se dostat do:\n\n > {', '.join(pos.get('where'))}") if pos.get('where') != 0 else typeOut("Nemůžeš se odsud nikam dostat. Něco ti brání v cestě.")
      return (pos, state)
            
def zkoumej(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
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
                  typeOut(f"Nejednoznačný vstup příkazu. ")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesInventory)} "))
                  typeOut(state._items.get(selection).get("desc")) if selection in matchesInventory else typeOut("Nezadal jsi správné slovo ze seznamu.")
            elif len(matchesObstacles) == 1:
                  typeOut(state._obstacles.get(matchesObstacles[0]).get("desc"))
            elif len(matchesObstacles) > 1:
                  typeOut(f"Nejednoznačný vstup příkazu. ")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesObstacles)} "))
                  typeOut(state._obstacles.get(selection).get("desc")) if selection in matchesObstacles else typeOut("Nezadal jsi správné slovo ze seznamu.")  
            else: typeOut("Toto nelze zkoumat. Buď je to předmět a nemáš ho v inventáři nebo je to objekt, který se v aktuální lokaci nenachází.")      
      return (pos, state)

def inventory(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      typeOut(f"V inventáři máš: \n\n > {', '.join(state.inventory)}") if len(state.inventory) != 0 else typeOut("Nemáš nic ve svém inventáři.")
      typeOut(f"\n\nPůsobí na tebe efekty: \n\n > {', '.join(state.effects)}") if len(state.effects) != 0 else typeOut("\nNepůsobí na tebe žádný efekt.")
      return (pos, state)

def pouzij(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      #TODO aby předmět byl použitelný na jiný předmět, musí oba dva předměty mít v "use" sebe navzájem (pokud používám předmět na obstacle, obstacle nemá use)
      
      if len(args) == 1:
            matches = checkExistence(args[0], state.inventory)
            if len(matches) == 1:
                  if 'self' in state._items.get(matches[0]).get("use"):
                        state.inventory.remove(matches[0])
                        state.effects.append(state._items.get(matches[0]).get("effect").get("self"))
                        typeOut(f"Použil jsi na sebe {matches[0]} a byl ti přidán efekt {state._items.get(matches[0]).get('effect').get('self')}")
                  else:
                        typeOut('Tento předmět nelze použít na sebe.')
            elif len(matches) > 1:
                  typeOut(f"Nejednoznačný vstup příkazu. ")
                  selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matches)} "))
                  if selection in matches:
                        if 'self' in state._items.get(selection).get("use"):
                              state.inventory.remove(selection)
                              state.effects.append(state._items.get(selection).get("effect").get("self"))
                              typeOut(f"Použil jsi na sebe {matches[0]} a byl ti přidán efekt {state._items.get(matches[0]).get('effect').get('self')}")
                        else:
                              typeOut('Tento předmět nelze použít na sebe.')
            else:
                  typeOut("Tento předmět nebyl v tvém inventáři nalezen.")
      elif len(args) > 1:  
            firstArgument = ''
            isFirstArgQuoted = False
            checkLengthAgainst = []
            if args[0][0] == '"':
                  isFirstArgQuoted = True
                  firstArgument += args[i][1:] + ' '
                  checkLengthAgainst.append(args[i])
            
            if isFirstArgQuoted == True:
                  if args[len(args)-1][-1] != '"': 
                        typeOut('Argument nebyl ukončen uvozovkou.')
                        return (pos, state)
                  for i in range(len(args)):
                        if args[i][-1] == '"':
                              firstArgument += args[i][:-1]
                              break
                        else: 
                              firstArgument += args[i] + ' '
                              checkLengthAgainst.append(args[i])
            else:
                  firstArgument = args[0] 
                  checkLengthAgainst.append(args[0])
            matchesFirst = checkExistence(firstArgument, state.inventory)
            if len(matchesFirst) == 0:
                  typeOut(f"Předmět {firstArgument} nebyl v tvém inventáři nalezen.")
                  return (pos, state)
            if len(args) == len(checkLengthAgainst):      
                  if len(matchesFirst) == 1:
                        if 'self' in state._items.get(matchesFirst[0]).get("use"):
                              state.inventory.remove(matchesFirst[0])
                              state.effects.append(state._items.get(matchesFirst[0]).get("effect"))
                              typeOut(f"Použil jsi na sebe {matchesFirst[0]} a byl ti přidán efekt {state._items.get(matchesFirst[0]).get('effect').get('self')}")
                        else:
                              typeOut('Tento předmět nelze použít na sebe.')
                  elif len(matchesFirst) > 1:
                        typeOut(f"Nejednoznačný vstup příkazu. ")
                        selection = input(typeOut(f"Vyber jedno slovo z následujícího seznamu (celým slovem):\n\n > {', '.join(matchesFirst)} "))
                        if selection in matchesFirst:
                              if 'self' in state._items.get(selection).get("use"):
                                    state.inventory.remove(selection)
                                    state.effects.append(state._items.get(selection).get("effect"))
                                    typeOut(f"Použil jsi na sebe {selection} a byl ti přidán efekt {state._items.get(selection).get('effect').get('self')}")
                              else:
                                    typeOut('Tento předmět nelze použít na sebe.')
                        else:
                              typeOut("Nesprávně zadaný výraz.")
            else:
                  if args[len(checkLengthAgainst)] != 'na':
                        typeOut('Mezi argumenty tohoto příkazu je očekáván výraz "na".')
                        return (pos, state)
                  else:
                        args.pop(len(checkLengthAgainst))
                  isSecondArgQuoted = False
                  secondArgument = ''
                  if args[len(checkLengthAgainst)][0] == '"':
                        secondArgument += args[len(checkLengthAgainst)][1:] + ' '
                        isSecondArgQuoted = True
                  else:
                        if args[1] != args[len(args)-1]:
                              typeOut("Argumenty složené z více slov musí být v uvozovkách")
                              return (pos, state)
                        secondArgument += args[1:]  
                  if isSecondArgQuoted == True:  
                        for i in range(len(args)):
                              secondArgument += args[i]  + ' '
                  
                  if isSecondArgQuoted == True and secondArgument[-1] != '"':
                        typeOut('Argument nebyl ukončen uvozovkou.')
                  matchesSecondItems = checkExistence(secondArgument, state._items)
                  matchesSecondObstacles = checkExistence(secondArgument, state._obstacles)
                  if len(matchesFirst) == 1:
                        if len(matchesSecondItems) == 1 and len(matchesSecondObstacles) == 0:
                              if not matchesFirst[0] in state._items.get(matchesSecondItems[0]).get("use"):
                                    typeOut(f"Nelze použít {matchesFirst[0]} na {matchesSecondItems[0]}.")
                              else:
                                    state.effects.append(state._items.get(matchesFirst[0]).get("effect").get(matchesSecondItems[0]))
                        elif len(matchesSecondItems) == 0 and len(matchesSecondObstacles) == 1:
                              print('here')            


                              
                       
                        


            



                   
      return (pos, state)

def save(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      saveData = {"pos": pos, "map": state.map, "inv": state.inventory, "money": state.money, "effects": state.effects}
      with open(".savefile", "w", encoding='utf8') as file:
            json.dump(saveData, file, ensure_ascii=False, default=tuple)
      return (pos, state)

def load(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      with open(".savefile", "r", encoding='utf8') as file:
            data: dict[str, dict[str, Any]] = json.loads(file.read())
            state.map = data.get("map")
            state.money = data.get("money")
            state.effects = data.get("effects")
            state.inventory = data.get("inv")
                  
            pos = data.get("pos")

      return (pos, state)

def help(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      if isinstance(args, str):
            typeOut('\nSeznam příkazů:\n > ' + ', '.join(list(commands.keys())))
      else:
            args = ' '.join(args)
            if args == 'help':
                  typeOut(commands.get('help').get('desc'))
            else:
                  matches = checkExistence(args, list(commands.keys()))
                  if len(matches) == 0:
                        typeOut('Hledaný příkaz neexistuje.')
                  else:
                        typeOut(commands.get(matches[0]).get("desc"))
      return (pos, state)

def info(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      text = '  Autor: Lukáš Rada\n  Den zahájení práce: 25.12.2022 (Veškerý postup v práci byl 29.12.2022 zahozen a začal jsem od nuly)\n  Čas práce v hodinách: '
      print('-'*len(text.split('\n')[1])+'----')
      typeOut(text)
      print('\n'+'-'*len(text.split('\n')[1])+'----\n')
      return (pos, state)

def navod(args: list[str] | str, pos: dict[str, str | list[str]], state: assets) -> tuple[dict[str, str | list[str]], assets]:
      typeOut('Tuto hru lze ovládat pouze pomocí příkazů zadaných do konzole.\n')
      typeOut('Hra obsahuje celkem 12 příkazů a každý z nich se dá zapsat zkrácenou verzí pomocí prvních tří písmen a to i bez ohledu na velká/malá písmena či diakritiku\n')
      typeOut('Drtivá většina příkazů relevantních pro postup hry vyžaduje tzv. argument - dodatečné slovo, se kterým příkaz pracuje. To může být předmět, lokace či překážka.\n')
      typeOut('Některé příkazy mohou argumentů přijímat více a argumenty mohou být i víceslovné. V případě zadání víceslovného argumentu je potřeba jej umístit do uvozovek\n')
      typeOut('Existují i příkazy, které fungují jak s argumenty, tak i bez jediného argumentu.\n')
      typeOut('Pro přesnější definici jakéhokoliv příkazu doporučuji použít příkaz help. (Příkaz help bez argumentů vypíše seznam všech dostupných příkazů)')
      
      return(pos, state)
                  
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
            "desc": "Příkaz na použití předmětu na jiný předmět nebo překážku. \n\n  Příklad: použij Telefon     použij Pistole na Zombík     použij \"Prací prášek\" na Prádlo" 
      }, 
      "save":{
            "callback": save,
            "desc": "Uloží postup hry."
      },
      "load":{
            "callback": load,
            "desc": "Načte uložený postup hry."
      }, 
      "info":{
            "callback": info,
            "desc": "Podrobnosti o práci."
      }, 
      "help": {
            "callback": help,
            "desc": "Ukáže seznam příkazů, pokud nebyl zadán žádný argument. V opačném případě ukáže použití daného příkazu. \n\n  Příklad: help     help seber"
      },
      "inventory": {
            "callback": inventory,
            "desc": "Ukáže obsah hráčova inventáře."
      }, 
      "kam": {
            "callback": kam,
            "desc": "Příkaz na zobrazení všech dostupných lokací. \n\n  Příklad: kam"
            },
      "návod": {
            "callback": navod,
            "desc": "Ukáže návod na ovládání hry."
      }
}
      