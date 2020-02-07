infile = open('C:/Users/User/Desktop/opdracht8.txt', 'r')
outfile = open('C:/Users/User/Desktop/opdracht8_compressed.txt', 'w')

lines = infile.readlines()
Removespaceamount = 0
removeTabamount = 0

for line in lines:

    for characters in line:
        if characters != ' ':  # als het geen space is, kijkt hij of het ook geen tab is
            if characters == '\t':  # als het geen space is, kan het een letter of tab zijn, als het tab is moet het nog niet stoppen met tellen.
                removeTabamount += 1
            else:  # als het ook geen tab is, verwijdert hij alles spaces en tabs tot zo ver, en gaat hij meteen naar de volgende line
                line = line.replace(' ', '', Removespaceamount)  # verwijder spaces zovaak als de counter heeft opgeteld
                line = line.replace('\t', '', removeTabamount)  # verwijder Tabs zovaak als de counter heeft opgeteld
                Removespaceamount = 0  # reset de counter
                removeTabamount = 0
                break  # als het character geen tab of space is, betekent dat hij bij de eerste letter is, dus stopt hij met optellen hoeveel spaces of tabs weg moeten
        else:  # als het wel een space is
            Removespaceamount += 1  # na elke character telt hij op hoeveel spaces weg moeten, mits er geen letter voorbij is gekomen
    if line != '\n':  # zolang de gehele line niet alleen een lege regel is, dan pas schijft hij de regel in het nieuwe bestand.
        outfile.write(line)  # schijf de uitkomst van de for loops in een nieuw bestand.

outfile.close()
infile.close()
