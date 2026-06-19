import os

PLIK = "quiz.txt"


def main():

    litery = "ABCD"

    if os.path.exists(PLIK) and os.path.getsize(PLIK) > 0:
        with open(PLIK, "r", encoding="utf-8") as plik:
            quiz = eval(plik.read())
    else:
        quit = {}
        print(
            f"Szukany plik nie istnieje. Utworzono nowy pusty plik o nazwie {PLIK}")

    for numer, (pytanie, odpowiedzi) in enumerate(quiz.items(), start=1):
        print(numer, pytanie)
        # licznik += 1

        for i, odpowiedz in enumerate(odpowiedzi):
            if i == 0:
                print(litery[i]+".", odpowiedz + " <--poprawna odpowiedz")
            else:
                print(litery[i]+".", odpowiedz)

        print()


if __name__ == "__main__":
    main()
