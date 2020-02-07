
def main():
    # Gegevens van de gebruiker krijgen
    aantal = int(input('Geef een cijfer: '))
    omkeer = input('Wilt u de pyramide omkeren? ')
    character = input('Welk character wilt u hebben? ')
    forofwhile = input('For loop of while loop? ')

    # Het programma met een for-loop of een while-loop uitvoeren, op basis van de ontvangen gegevens van de gebruiker
    if 'while' in forofwhile:
        pyramide_via_while_loop(aantal, omkeer, character)
    else:
        pyramide_via_for_loop(aantal, omkeer, character)


def pyramide_via_while_loop(aantal, omkeer, character):
    # Een pyramide van characters maken,
    # 'aantal' geeft aan hoe groot de pyramide moet zijn,
    # 'omkeer' geeft aan welke kant de pyramide op wijst,
    # 'character' geeft aan waarvan de pyramide uit gemaakt is.
    # De opteller houdt bij hoe lang de while-loop nog moet doorgaan

    opteller = 1

    # De formatting zorgt ervoor dat de pyramide omkeert
    # Geef whitespaces zo lang als de gegeven pyramide grootte
    # De formatting kan ook 0 whitespaces hebben(else), dit zorgt ervoor dat de pyramide Niet omdraait
    if omkeer in 'yesjayeahYESJAYEAH':

        formatting = '{:>' + str(aantal) + '}'
    else:

        formatting = '{:>' + str(0) + '}'

    # De 2 while-loops die de pyramide opstellen, 1 voor berg opwaarts, 1 voor berg afwaarts.
    while opteller <= aantal:
        sterren = str(character) * aantal
        print(formatting.format(sterren[:opteller]))
        opteller += 1
    while opteller > 1:
        opteller -= 1
        sterren = str(character) * aantal
        print(formatting.format(sterren[:opteller - 1]))


def pyramide_via_for_loop(aantal, omkeer, character):
    # Een pyramide van characters maken,
    # 'aantal' geeft aan hoe groot de pyramide moet zijn,
    # 'omkeer' geeft aan welke kant de pyramide op wijst,
    # 'character' geeft aan waarvan de pyramide uit gemaakt is.

    # De formatting zorgt ervoor dat de pyramide omkeert
    # Geef whitespaces zo lang als de gegeven pyramide grootte(if)
    # De formatting kan ook 0 whitespaces hebben(else), dit zorgt ervoor dat de pyramide Niet omdraait
    if omkeer in 'yesjayeahYESJAYEAH':

        formatting = '{:>' + str(aantal) + '}'
    else:
        formatting = '{:>' + str(0) + '}'

    # De 2 for-loops die de pyramide opstellen, 1 voor berg opwaarts, 1 voor berg afwaarts.
    for ster in range(1, (aantal + 1)):

        aantalsterren = str(character) * ster

        aantalsterren = formatting.format(aantalsterren)
        print(aantalsterren)
    for ster in range((aantal - 1), 0, -1):
        aantalsterren = str(character) * ster
        aantalsterren = formatting.format(aantalsterren)
        print(aantalsterren)


main()
