import os

PLIK = "quiz.txt"


def main():

    # Wczytanie istniejącego słownika lub utworzenie pustego
    if os.path.exists(PLIK) and os.path.getsize(PLIK) > 0:
        with open(PLIK, "r", encoding="utf-8") as plik:
            quiz = eval(plik.read())
    else:
        quiz = {}

    while True:
        # Dodawanie nowego pytania
        pytanie = input("Podaj treść pytania: ")

        if pytanie in quiz.keys():
            print("Takie pytanie już istnieje! \n")
            print("Zapisane tresci pytan: ")
            for pytanie in quiz.keys():
                print(pytanie)

            czy_kontynuowac = input(
                "Czy chcesz wprowadzic inne pytanie? t/n").lower()
            while czy_kontynuowac not in ['t', 'n']:
                czy_kontynuowac = input(
                    "Czy chcesz wprowadzic inne pytanie? t/n ").lower()

            if czy_kontynuowac == "n":
                break

        else:

            odpowiedzi = []

            print("Najpierw wpisz poprawną odpowiedź!\n")

            poprawna = input("Podaj poprawna odpowiedz: ")
            odpowiedzi.append(poprawna)

            # print("Podaj niepoprawne odpowiedzi")
            for i in range(3):
                odp = input(f"Niepoprawna odpowiedź {i + 1}: ")
                while odp == poprawna:
                    print(
                        "Podanana niepoprawna odpowiedz jest taka sama jak odpowiedz poprawna!!! Wskaz inna tresc niepoprawnej odpowiedzi!")
                    odp = input()
                while odp in odpowiedzi:
                    print(
                        "Nie morzesz podac dwa razy takiej samej odpowiedzi. Podaj inna! ")
                    odp = input()
                odpowiedzi.append(odp)

            quiz[pytanie] = odpowiedzi

            # Zapis zaktualizowanego słownika
            with open(PLIK, "w", encoding="utf-8") as plik:
                plik.write(str(quiz))

            print(f'\n{pytanie}')
            for element in quiz[pytanie]:
                print(element)

            print("Pytanie zostało zapisane.")

            break


if __name__ == "__main__":
    main()

# dodaj sprawdzanie czy pytania sie nie powtarzaja
# dodaj sprawdzanie czy odpowiedzi sie nie powtarzaja
