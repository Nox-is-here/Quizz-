import os
import wyswietl_wszystko

PLIK = "quiz.txt"


def main():
    # Wczytanie istniejącego słownika lub utworzenie pustego
    if os.path.exists(PLIK) and os.path.getsize(PLIK) > 0:
        with open(PLIK, "r", encoding="utf-8") as plik:
            quiz = eval(plik.read())
    else:
        print("Nie znaleziono zadnych pytan do quizu!")
        return

    pytania = list(quiz.keys())

    for i, pytanie in enumerate(pytania, start=1):
        print(f"{i}. {pytanie} ")

    numer_do_usuniecia = int(input("Podaj numer do usuniecia"))

    del quiz[pytania[numer_do_usuniecia-1]]

    with open(PLIK, "w", encoding="utf-8") as plik:
        plik.write(str(quiz))

    print("Pytanie zostało usunięte. Aktualna lista pytan:")
    wyswietl_wszystko.main()


if __name__ == "__main__":
    main()
