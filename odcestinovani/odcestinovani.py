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

while True:
    text = input('Zadej text k odcesteni (nebo zadej .exit pro ukonceni programu): ')
    if text == '.exit':
        break
    print('\n'+odcesti(text)+'\n')
