def Fibbonaci(N1, N2, NumberToFind, f):
    f += 1
    N3 = N1 + N2
    
    if N3 == NumberToFind:
        f += 1
        return f
    else:
        return Fibbonaci(N2, N3, NumberToFind, f)  # de volgende 2 getallen, n2 en n3, worden in de functie gevoegd


n = 34

print("n = " + str(n))
print("f"+str(Fibbonaci(0, 1, n, 0)))
