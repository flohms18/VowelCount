def VowelConCount(text):
    voyelles = "aeiouyAEIOUY"
    consonnes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    VCount = 0
    CCount = 0

    for char in text:
        if char in voyelles:
            VCount += 1
        elif char in consonnes:
            CCount += 1
    print(VCount)
    print(CCount)

VowelConCount("James Bond")
        

