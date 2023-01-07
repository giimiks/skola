class assets:
      map: dict[str, dict[str, str | list[str]]] = {
            "Karla Čapka": {
                  "name": "Karla Čapka",
                  "desc": "Ááá, ulice Karla Čapka... Nejpodivuhodnější nátury z celého Habartova se v místních bytech scházejí k různým a jistě legálním aktivitám.",
                  "items": [],
                  "zkoumej":  ["Nedopalek", "Zapalovač", "Test", "Ryba na rybu"],
                  "where": ["Raisovka", "Skatepark", "Texas"],
                  "obstacles": []
                  },
            "Raisovka": {
                  "name": "Raisovka",
                  "desc": "Raisova ulice - protáhlá ulička s paneláčky, které mají přívětivě barevnou fasádu. Škoda, že stejně přívětiví nejsou místní obyvatelé...",
                  "items": [],
                  "zkoumej": ["Klacek", "Květ", "Banán"],
                  "where": ["Karla Čapka"],
                  "obstacles": ["Hladové dítě"]
            }

      }
      _items: dict[str, dict[str, str | list[str] | dict[str, str]]] = {
            "Nedopalek": {
                  "desc": "Nedopalek od cigarety. Ještě se bude dát šluknout.",
                  "use": ["Zapalovač", "self"],
                  "effect": {
                        "Zapalovač": "Cigaretový smrad z pusy",
                        "Testující testíček": "Testující test"
                  }
            },
            "Zapalovač": {
                  "desc": "Plynový zapalovač.",
                  "use": ["Cigareta", "Joint", "Nedopalek", "self"],
                  "effect": {
                        "Nedopalek": "Cigaretový smrad z pusy"
                  }
            },
            "Testující testíček": {
                  "desc": "Test na test je test na test",
                  "use": ["self", "Nedopalek"],
                  "effect": {
                        "Nedopalek": "Testující test"
                  }
            },
            "Klacek": {
                  "desc":"Dubový klacek, nic extra.",
                  "use": "Hladové dítě",
            }
      }
      _obstacles: dict[str, dict[str, str | list[str] | dict[str, list[str]]]] = {
            "Hladové dítě": {
                  "desc": "Na tvé cestě Raisovkou se nachází dítě, je hladové, hyperaktivní a nesleze ti z těla. Musíš nějak zakročit.",
                  "killableBy": ["Klacek"],
                  "unlock": {
                        "where":["Karla Čapka", "Texas", "Horňák"],
                        "items": ["Amfetaminy na ADHD"]
                        },
                  "afterKill": "Hodils dítěti klacek a dítě se po něm rozeběhlo jako šalený pes. Něco mu vypadlo z kapsy. Nyní můžeš opustit Raisovku. "
            }
      }
      inventory: list[str] = ["Igelitka", "Telefon"]
      money: int = 100
      _quotes: set[str] = ("Co dál?", "Jaký je tvůj další krok?", "Další krok?", "Co hodláš dál dělat?", "Jak budeš pokračovat?", "Jak budeš postupovat?", "Co se bude dít dál?", "Co dál uděláš?", "A dál?", "Co se dál stane?")
      effects: list[str] = []


