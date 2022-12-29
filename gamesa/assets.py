class assets:
      map = {
            "Karla Čapka": {
                  "name": "Karla Čapka",
                  "desc": "Ááá, ulice Karla Čapka... Nejpodivuhodnější nátury z celého Habartova se v místních bytech scházejí k různým a jistě legálním aktivitám.",
                  "items": set(),
                  "zkoumej":  {"Nedopalek", "Zapalovač"},
                  "where": {"Raisovka", "Skatepark", "Texas"},
                  "obstacles": set()
                  },
            "Raisovka": {
                  "name": "Raisovka",
                  "desc": "Raisova ulice - protáhlá ulička s paneláčky, které mají přívětivě barevnou fasádu. Škoda, že stejně přívětiví nejsou místní obyvatelé...",
                  "items": set(),
                  "zkoumej": {"Klacek", "Květ", "Banán"},
                  "where": {"Karla Čapka"},
                  "obstacles": {"Hladové dítě"}
            },

      }
      items = {
            "Nedopalek": {
                  "desc": "Nedopalek od cigarety.",
                  "use": {"Zapalovač"},
                  "effect": "Smrad"
            }
      }
      obstacles = {"Hladové dítě": {
            "desc": "Na tvé cestě Raisovkou se nachází dítě, je hladové, hyperaktivní a nesleze ti z těla. Musíš nějak zakročit.",
            "killableBy": {"Klacek"},
            "unlock": {
                  "where":{"Karla Čapka", "Texas", "Horňák"},
                  "items": {"Amfetaminy na ADHD"}
                  },
            "afterKill": "Hodils dítěti klacek a dítě se po něm rozeběhlo jako šalený pes. Něco mu vypadlo z kapsy. Nyní můžeš opustit Raisovku. "

      }}
      inventory = {"Igelitka", "Telefon"}
      money = 100
      quotes = ("Co dál?", "Kam se vydáš?", "Další krok?", "Co hodláš dál dělat?", "Jak budeš pokračovat?", "Jak budeš postupovat?", "Co se bude dít dál?", "Co dál uděláš?")
      effects = {}


