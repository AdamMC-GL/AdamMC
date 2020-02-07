
def Tekstcheck(eersteinput, tweedeinput):
    index = 0
    try:
        if eersteinput != tweedeinput:
            for vergelijking in eersteinput:

                if vergelijking == tweedeinput[index]:
                    index += 1
            return index
        else:
            return False

    except IndexError:
        return index


eersteinput = input('Geef een string: ')
tweedeinput = input('Geef nog een string: ')

if Tekstcheck(eersteinput, tweedeinput):
    print('Het eerste verschil zit op index: ' + str(Tekstcheck(eersteinput, tweedeinput)))
else:
    print('De 2 string zijn hetzelfde.')
