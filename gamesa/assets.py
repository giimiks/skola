class assets:
      map: dict[str, dict[str, str | list[str]]] = {
            "blank": {
                  "name": "",
                  "desc": "",
                  "items": [],
                  "zkoumej":  [],
                  "where": [],
                  "obstacles": []
            },
            "Karla Čapka": {
                  "name": "Karla Čapka",
                  "desc": "Ááá, ulice Karla Čapka... Nejpodivuhodnější nátury z celého Habartova se v místních bytech scházejí k různým a jistě legálním aktivitám.",
                  "items": [],
                  "zkoumej":  ["Nedopalek", "Zapalovač"],
                  "where": ["Raisovka", "Skatepark"],
                  "obstacles": []
                  },
            "Raisovka": {
                  "name": "Raisovka",
                  "desc": "Raisova ulice - protáhlá ulička s paneláčky, které mají přívětivě barevnou fasádu. Škoda, že stejně přívětiví nejsou místní obyvatelé...",
                  "items": [],
                  "zkoumej": ["Klacek", "Květ", "Banán"],
                  "where": [],
                  "obstacles": ["Hladové dítě"]
            },
            "Skatepark":  {
                  "name": "Skatepark",
                  "desc": "Tento skatepark již není skatepark. Rampy byly prodané a na místě se plánuje vybudování parkoviště. Jedno ovšem zůstalo - pochůzky habartovských dětí a veškerý bordel po nich.",
                  "items": [],
                  "zkoumej": [],
                  "where": ["Karla Čapka"],
                  "obstacles": ["Pavel Švácha"]
            },
            "Horňák": {
                  "name": "Horňák",
                  "desc": "Horňák je místem, kde se postarší občané Habartova scházejí, aby si dali pivo a zanadávali si na zastupitelstvo.",
                  "items": [],
                  "zkoumej":  ["Pivo"],
                  "where": ["Raisovka", "Garáže"],
                  "obstacles": ["Opilec"]
            },
            "Panelák": {
                  "name": "Panelák",
                  "desc": "Banda mladíků, ze kterých smrděla marihuana, tě pozvala do svého bytu a nabízí ti peníze za jisté „velice legální látky“.",
                  "items": [],
                  "zkoumej": [],
                  "where": ["Raisovka"],
                  "obstacles": ["Banda mladíků"]
            },
            "Garáže": {
                  "name": "Garáže",
                  "desc": "V těchto garážích lidé uskladňují svá auta a znečišťují okolí se svým bordelem.",
                  "items": [],
                  "zkoumej": [],
                  "where": ["Horňák","Benzínka"],
                  "obstacles": ["Starý pán"]
            },
            "Benzínka": {
                  "name": "Benzínka",
                  "desc": "Benzínka MOL.",
                  "items":[],
                  "zkoumej": [],
                  "where": ["Garáže"],
                  "obstacles": ["Prodavačka"]
            },
            "Auto": {
                  "name": "Auto",
                  "desc": "Auto toho starého pána. Prý tě sveze do Tesca.",
                  "items": [],
                  "zkoumej": [],
                  "where": ["Garáže","Parkoviště u Tesca"],
                  "obstacles": [] 
            },
            "Parkoviště u Tesca": {
                  "name": "Parkoviště u Tesca",
                  "desc": "Dojel jsi do Tesca. Teď už jen stačí s penězi zajít ke vchodu.",
                  "zkoumej": [],
                  "items": [],
                  "where": ["Auto","Vchod do Tesca"],
                  "obstacles": []
            },
            "Tesco": {
                  "name": "Tesco",
                  "desc": "Tesco Habartov, koupíš zde rohlíky a další důležité věci.",
                  "zkoumej": [],
                  "items":  [],
                  "where": [],
                  "obstacles": []
            }



}
      _items: dict[str, dict[str, str | list[str] | dict[str, str]]] = {
            "Testující testíček": {
                  "desc": "Test na test je test na test",
                  "use": ["self", "Nedopalek"],
                  "effect": {
                        "Nedopalek": "Testující test"
                  }
            },
            "Nedopalek": {
                  "desc": "Nedopalek od cigarety. Ještě se bude dát šluknout.",
                  "use": ["Zapalovač"],
                  "effect": {
                        "Zapalovač": "Cigaretový smrad z pusy",
                        "Testující testíček": "Testující test"
                  }
            },
            "Zapalovač": {
                  "desc": "Plynový zapalovač.",
                  "use": ["Nedopalek"],
                  "effect": {
                        "Nedopalek": "Cigaretový smrad z pusy"
                  }
            },    
            "Klacek": {
                  "desc":"Dubový klacek, nic extra.",
                  "use": ["Hladové dítě"],
            },
            "Květ": {
                  "desc": "Podezřele vypadající květ",
                  "use": ["Banán"],
                  "effect": {
                        "Banán": "Super silný buff pana Šváchy"
                  }
            },
            "Banán": {
                  "desc": "Banán zajímavého vzhledu.",
                  "use": ["Květ"],
                  "effect": {
                        "Květ": "Super silný buff pana Šváchy"
                  }
            },
            "Pivo": {
                  "desc": "Lahodná plznička",
                  "use": ["self"],
                  "effect": {
                        "self": "Lehké opití pivem"
                  }
            },
            "Amfetaminy": {
                  "desc": "Amfetaminy na uklidnění hyperaktivního a hladového dítěte. Dají se za dobrou sumu prodat.",
                  "use": ["Banda mladíků"],
                  "effect": {

                  }
            },
            "Benzín": {
                  "desc": "Natural 95",
                  "use": ["Starý pán"],
                  "effect": {

                  }
            },
            "Peníze": {
                  "desc": "200Kč",
                  "use": ["Prodavačka", "Vchod do Tesca"],
                  "effect": {

                  }
            }
            
      }
      _obstacles: dict[str, dict[str, str | list[str] | dict[str, list[str]]]] = {
            "Hladové dítě": {
                  "desc": "Na tvé cestě Raisovkou se nachází dítě, je hladové, hyperaktivní a nesleze ti z těla. Musíš nějak zakročit.",
                  "killableBy": ["Klacek"],
                  "unlock": {
                        "where":["Karla Čapka", "Horňák", "Panelák"],
                        "items": ["Amfetaminy"]
                        },
                  "afterKill": "Hodils dítěti klacek a dítě se po něm rozeběhlo jako šalený pes. Něco mu vypadlo z kapsy. Nyní můžeš opustit Raisovku.",
                  "oslov": "none"
            },
            "Pavel Švácha": {
                  "desc": "Pan učitel Švácha číhá na skateparku. Pokud vlastníš jeho buff, dá ti dárek a vypaří se.",
                  "killableBy": [],
                  "unlock": {
                        "where":[],
                        "items": ["Pervitin"]
                  },
                  "afterKill": "Díky svému super úžasného buffu ti pan Švácha položil Pervitin na zem a záhy se vypařil ze světa.",
                  "oslov": "Super silný buff pana Šváchy"
            },
            "Banda mladíků": {
                  "desc": "Banda mladíků ti nabízí kšeft - peníze za narkotika. Použij na ně narkotika a peníze jsou tvé.",
                  "killableBy": ["Amfetaminy", "Pervitin"],
                  "unlock": {
                        "where": [],
                        "items": ["Peníze"]
                  },
                  "afterKill": "Předal jsi mladíkům své zboží a oni ti nechali na podlaze dost peněz na tvůj nákup v Tescu.",
                  "oslov": "none"
            },
            "Opilec": {
                  "desc": "Opilec na tebe něco mumlá. Možná, že když se dostaneš na stejnou opileckou frekvenci, budeš rozumět, co ti říká.",
                  "killableBy": [],
                  "unlock": {
                        "where": [],
                        "items": []
                  },
                  "afterKill": "Můj chábr má teďka (grrrc) ve své garáži (škyt) problém s nastartovánim svýho auta, nejspíš potřebuje benzin. Nemohl bys mu nějak pomoct?",
                  "oslov": "Lehké opití pivem"
            },
            "Starý pán": {
                  "desc": "Stojí zde zmatený starý pán.",
                  "killableBy": ["Benzín"],
                  "unlock":  {
                        "where": ["Auto"],
                        "items": ["Peníze"]
                  },
                  "afterKill": "Dal jsi starému pánovi benzín a on ti na oplátku dal nějaké ty peníze, aby sis mohl koupit ty rohlíky. Nabídl ti také odvoz domů z Tesca.",
                  "oslov": "none"
            },
            "Prodavačka": {
                  "desc": "Prodavačka na této benzíně.",
                  "killableBy": ["Peníze"],
                  "unlock": {
                        "items":["Benzín"],
                        "where": []
                  },
                  "afterKill": "Koupil sis od prodavačky benzín.",
                  "oslov": "none"
            },
            "Vchod do Tesca": {
                  "desc": "Do vchodu tohoto Tesca nainstalovali systém na identifikování zákazníkových financí. Pokud žádné u sebe nemá, neotevřou se mu dveře.",
                  "killableBy": ["Peníze"],
                  "unlock": {
                        "items":[],
                        "where":["Tesco"]
                  },
                  "afterKill": "Brána k rohlíkům se ti otevřela, nyní můžeš vstoupit do Tesca a ukončit svou pouť Habartovem. Ten starý pán od garáží tě pak hodí domů.",
                  "oslov": "none"
            }
      }
      inventory: list[str] = ["Igelitka", "Telefon"]
      _quotes: set[str] = ("Co dál?", "Jaký je tvůj další krok?", "Další krok?", "Co hodláš dál dělat?", "Jak budeš pokračovat?", "Jak budeš postupovat?", "Co se bude dít dál?", "Co dál uděláš?", "A dál?", "Co se dál stane?")
      effects: list[str] = []


