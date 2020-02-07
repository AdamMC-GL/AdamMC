
string1 = input('Geef een tekst: ')
rotation = input('Geef een rotatie: ')
newstring = ''
for letters in string1:
    if letters not in '.,? \'''!``""':
        newstring += chr(ord(letters) + int(rotation))
    else:
        newstring += letters
        
print('Ceasarcode: '+newstring)
