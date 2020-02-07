def gemmidelde(lijst):
    gemGrootte = 0
    for items in lijst:  # alles bij elkaar gedeelt door aantal is het gemmidelde
        gemGrootte += items  # dus hij gaat door de lijst heen en telt het meteen op, het uiteindelijke getal is gemGrootte
    gemmidelde = gemGrootte / len(lijst)
    print(gemmidelde)


def gemmidelde_van_lijsten(list):
    gemGrootte = 0
    itemcount = 0
    for sublists in list:
        for items in sublists:
            gemGrootte += items
            itemcount += 1
    gemmidelde = gemGrootte / itemcount
    print(gemmidelde)


lijstje = [[5, 5, 7, 3], [5, 5, 7, 3], [10, 10, 14, 6]]
gemmidelde_van_lijsten(lijstje)
