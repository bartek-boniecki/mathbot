i = int(input("Podaj liczbę zagadek, które chcesz rozwiązać, ale bądź ambitny!"))
if i > 3:
    for i in range(1, i):
        print(f"Puzzle {i}: What is {i} + {i} 🤔")
else:
        print("Mordeczko, no to nie było zbyt ambitne")