def diküçgenbulma(uzunluk):
    for c in range(1, int(uzunluk / 2)):
        for a in range(1, int(uzunluk / 2)):
            b = uzunluk - (a + c)
            if (b * b == a * a + c * c) and (uzunluk == a + b + c):
                return (a, b, c)


uzunluk = int(input("Üçgenin uzunluğunu giriniz:"))
print(diküçgenbulma(uzunluk))
