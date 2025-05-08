klasa = int(input("Do jakiej klasy chodzisz"))
dzial = input("Jaki dział właśnie omawiacie?")
print(f"\nTworzenie 5 zadan matematycznych - zagadek wykraczających poza zakres podstawy programowej z zakresu działu: {dzial} dla uczniów klasy {klasa+1}...\n")
def tworzenie_fejkowych_zadan(klasa, dzial, number):
    return f"Zadanie {number}: [Fake AI] Utwórz zadanie-zagadkę z działu {dzial} wykraczającą poza poziom ucznia klasy {klasa+1}"
for i in range(1, 6):
    question = tworzenie_fejkowych_zadan(klasa, dzial, i)
    print(question)