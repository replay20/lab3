produkt = {"Ananas":"szt",
           "Ziemniak":"kg",
           "Mleko":"l",
           "Kokos":"szt",
           "Kurczak":"kg",
           "Rosol":"l"}

print(produkt)

lista = [j for j,k in produkt.items() if k == "szt"]

print(lista)