def sprTrojkat(a,b,c):
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2

a = input("Podaj pierwszy bok trojkata: ")
a=int(a)
b = input("Podaj drugi bok trojkata: ")
b=int(b)
c = input("Podaj trzeci bok trojkata: ")
c=int(c)

if sprTrojkat(a,b,c):
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")