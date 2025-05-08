import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat

from dotenv import load_dotenv
load_dotenv()

# Zaproponuj 5 zadań-zagadek z działu o procentach, z których co najmniej 3 będą dotyczyły konkretnych sytuacji życiowych i co najmniej 2 będą wymagały rozwiązania poprzez równanie z jedną niewiadomą która wymaga przekształceń
# Działy matematyki: szkoła podstawowa: [Arytmetyka:] właściwości, działania i przekształcanie liczb naturalnych i całkowitych; właściwości, działania i przekształcanie liczb wymiernych: ułamków zwykłych i dziesiętnych; potęgowanie i działania na pierwiastkach liczb wymiernych | [Algebra] wyrażenia algebraiczne: tworzenie i przekształcanie; równania i nierówności - rozwiązywanie, interpretacja rozwiązań, zastosowanie równań w zadaniach tekstowych; proporcjonalność prosta | [Geometria płaska i przestrzenna:] podstawowe figury geometryczne; własności figur; geometria przestrzenna; symetrie | Statystyka opisowa i rachunek prawdopodobieństwa | kombinatoryka | Umiejętności praktyczne i zastosowania matematyki: odczytywanie i interpretacja informacji w różnych formach, zastosowania matematyki w praktyce życia codziennego
# Działy matematyki: szkoła ponadpodstawowa: [Arytmetyka i algebra:] Liczby rzeczywiste: właściwości, działania, przekształcanie; wyrażenia algebraiczne: przekształcanie, działania, wzory skróconego mnożenia, rozkładanie na czynniki; rozwiązywanie równań i nierówności liniowych, kwadratowych oraz wymiernych; układy równań | [Funkcje i ciągi:] Funkcje: liniowe, kwadratowe, wykładnicze, logarytmiczne, trygonometryczne; własności i analiza funkcji, przekształcenia wykresów; ciągi: liczbowe, arytmetyczne i geometryczne, wzory ogólne | [Geometria:] Planimetria: własności figur płaskich, obliczanie pól i obwodów, twierdzenia geometryczne; geometria analityczna: układ współrzędnych, równania prostych i okręgów, odległość między punktami | [Statystyka i rachunek prawdopodobieństwa:] statystyka opisowa: zbieranie i przedstawianie danych, średnia arytmetyczna, mediana, dominanta, odchylenie standardowe, interpretacja danych statystycznych; rachunek prawdopodobieństwa: reguły dodawania i mnożenia, prawdopodobieństwo warunkowe, niezależność zdarzeń | Kombinatoryka | Analiza matematyczna - optymalizacja i rachunek różniczkowy: pojęcie pochodnej, interpretacja geometryczna, zastosowanie pochodnych do badania przebiegu zmienności funkcji, znajdowanie ekstremów lokalnych i globalnych, optymalizacja

klasa = input("Wskaż na poziomie jakiej klasy jest uczeń (od 1 do 12, gdzie 1-8 to klasy szkoły podstawowej, a 9-12 to klasy szkół ponadpodstawowych, np. poziom 9 to pierwsza klasa szkoły ponadpodstawowej):  ")
dzial = input("Wskaż z jakiego działu potrzebujesz zadań, np.: arytmetyka (ułamki, potęgi i pierwiastki), algebra (wyrażenia algebraiczne, równania i nierówności), geometria (figury płaskie, figury przestrzenne, geometria analityczna), statystyka opisowa, rachunek prawdopodobieństwa, funkcje, ciągi, kombinatoryka, analiza matematyczna:  ")
zadanka = int(input("Wskaż ile chcesz zadanek 🔥💪🏻  "))
heheszka = input("Oceń w skali 1-5 radość dzieci z tyyylu nowych zadanek 🤣🤣🤣  ")

# initialize the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    description="Jesteś nauczycielem matematyki w szkole podstawowej oraz ponadpodstawowej, który daje na sprawdzianach własne zadania dodatkowe na ocenę celującą, które poziomem trudności wykraczają poza materiał, są na poziomie podstawy programowej o 2 lata wyżej niż poziom danej klasy (np. gdy uczeń jest w 6 klasie szkoły podstawowej, to Ty korzystasz z podstawy programowej dla 8 ósmej klasy, a gdy jest na 9 poziomie czyli w pierwszej klasie szkoły ponadpodstawowej, to korzystasz z zadań jak dla 3 klasy szkoły ponadpodstawowej itd.) i są zadaniami-zagadkami matematycznymi, których rozwiązanie wymaga pomyślenia, i nie wystarczy samo podstawienie do wzoru i wykonanie prostych obliczeń.",
    markdown=True
)


#tworzenie zadań
for i in range(1, zadanka + 1):
    prompt = f"Zaproponuj jedno zadanie-zagadkę z matematyki z działu {dzial}, dla ucznia z klasy {klasa}, które wykracza poza podstawę programową, jest powiązane z życiem codziennym i/lub wymaga rozwiązania równania z jedną niewiadomą."
    print(f"\nZadanie {i}:")
    agent.print_response(prompt, stream=True)