
def count(lijst, x):
    xcount = 0
    alleen_1_en_0 = True
    alleen_1_en_0_voeldoet_aan_eisen = True

    for check in lijst:  # check of de lijst alleen van 1'en of 0'en bestaan
        if check != 0 and check != 1:

            alleen_1_en_0 = False
            break
    for number in lijst:
        if number == x:
            xcount += 1

    if alleen_1_en_0:
        one_count = 0
        zero_count = 0
        for number in lijst:
            if number == 1:
                one_count += 1
            if number == 0:
                zero_count += 1

        if zero_count > 12 or one_count < zero_count:
            alleen_1_en_0_voeldoet_aan_eisen = False

    return alleen_1_en_0_voeldoet_aan_eisen, xcount, alleen_1_en_0


def verschil(lijst):
    indexnumber = 1
    grootste_verschil = -1
    for number in lijst:
        if lijst[indexnumber] > number:
            verschil = (lijst[indexnumber] - number)
        else:
            verschil = (number - lijst[indexnumber])

        if verschil > grootste_verschil:
            grootste_verschil = verschil

        if number != lijst[-2]:  # zolang als de een na laatse Niet word vergeleken met de laatste, anders word de index hoger dan de lijst aan nummers heeft.
            indexnumber+=1
    return grootste_verschil


def main():
    N = 0
    lijst = [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    xcount = count(lijst, N)[1]
    grootste_verschil_tussen_twee_getallen = verschil(lijst)
    print('In de list: '+str(lijst))
    print(str(N)+' komt '+str(xcount)+' keer voor.')

    if count(lijst, N)[2]:
        if not count(lijst, N)[0]:
            print('De lijst voldoet niet aan de eisen')
        else:
            print('De lijst voldoet wel aan de eisen.')

    else:
        print('Het grootste verschil tussen twee getallen is: ' + str(grootste_verschil_tussen_twee_getallen))


main()