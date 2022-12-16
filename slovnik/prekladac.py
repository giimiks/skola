rozdelovac = '|'

soubor=open('./encs.txt', encoding='utf-8').readlines()

def prelozSlovo(slovo: str, jazyk: str):
  if jazyk not in ['en', 'cs']:
    return 'Neznamy kod jazyka!!!'
  seznamPrekladu=[]
  slovo = slovo.lower()
  for radek in soubor:
    radek=radek.split(rozdelovac)
    radek[1]=radek[1].removesuffix('\n')
    if jazyk == 'cs':
      if slovo == radek[1]:
        seznamPrekladu.append(radek[0])
    if jazyk == 'en':
      if slovo == radek[0]:
        seznamPrekladu.append(radek[1])
        
  if seznamPrekladu == []:
      return slovo  
  else:return seznamPrekladu
        
    
def prelozVetu(veta: str, jazyk: str):
  if jazyk not in ['en', 'cs']:
    return 'Neznamy kod jazyka!!!'
  konecnyVysledek = []
  veta=veta.lower()
  veta=veta.split(' ')
  for slovo in veta:  
    prelozeno = prelozSlovo(slovo, jazyk)
    if isinstance(prelozeno, str):
      konecnyVysledek.append(slovo)
    else: 
      konecnyVysledek.append(prelozeno[0]) 
    
  return konecnyVysledek

while True:
  typ = input('Prelozit slovo nebo vetu? (zadej "slovo" nebo "veta")>>> ')
  if typ == 'slovo':
    slovo = input('Zadej slovo pro prelozeni>>> ')
    lang = input('Zadej cs pro prelozeni z cestiny do anglictiny nebo en pro prelozeni z anglictiny do cestiny>>> ')
    print(f'{slovo} : {", ".join(prelozSlovo(slovo, lang))}')
  elif typ == 'veta':
    veta = input('Zadej vetu pro prelozeni>>> ')
    lang = input('Zadej cs pro prelozeni z cestiny do anglictiny nebo en pro prelozeni z anglictiny do cestiny>>> ')
    print(f'{veta} : {" ".join(prelozVetu(veta, lang))}')
  