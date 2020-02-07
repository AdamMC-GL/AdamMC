
def Cyclisch_verschuiven(ch, amount):
    stringnumber = ord(ch)
    ch = bin(stringnumber)[2:]  # change character to byte


    while amount != 0:
        if amount > 0:
            ch = ch[1:] + ch[0]
            amount -= 1
        else:
            ch = ch[-1] + ch[:-1]
            amount += 1
    print(ch)


ch = 'b'
n = -4  # hoeveel moet worden verschoven
Cyclisch_verschuiven(str(ch), n)
