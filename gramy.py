import random
import os

PLIK = "quiz.txt"


def main():

    litery = "ABCD"

    niepoprawne = {}
    poprawne_ile = {}

    poprawne = 0

    if os.path.exists(PLIK) and os.path.getsize(PLIK) > 0:
        with open(PLIK, "r", encoding="utf-8") as plik:
            quiz = eval(plik.read())
    else:
        print("Plik z pytaniami do Quizu jest pusty. Uzupelnij go przed nastepnym uruchomieniem glownego trybu")
        return

    pytania = list(quiz.items())
    random.shuffle(pytania)

    for i, (pytanie, odpowiedzi) in enumerate(pytania, start=1):
        print(str(i) + ".", pytanie)

        szufluj = odpowiedzi.copy()
        random.shuffle(szufluj)

        for i, odpowiedz in enumerate(szufluj):
            print(litery[i]+".", odpowiedz)

        while True:
            odp_user = input("Podaj odpowiedz A B C D: ").upper()
            if odp_user in ['A', 'B', 'C', 'D']:
                break

        indeks = litery.index(odp_user)

        if szufluj[indeks] == quiz[pytanie][0]:
            poprawne += 1
            poprawne_ile[pytanie] = szufluj[indeks]
        else:
            niepoprawne[pytanie] = szufluj[indeks]

        print()
        # licznik_pytania += 1

    print(f'Poprawnosc: {poprawne/len(quiz) * 100:.2f}%')
    print(f"Poprawne odpowiedzi: {poprawne}/{len(quiz)}")
    for keys, values in poprawne_ile.items():
        print(keys, "Odpowiedziales: ", values,
              "<--To jest poprawna odpowiedz!\n")
    print()

    print(f"Niepoprawne odpowiedzi: {len(niepoprawne)}\n")

    for keys, values in niepoprawne.items():
        print(keys, "Odpowiedziales: ", values,
              "<--To nie jest poprawna odpowiedz!\n")


if __name__ == "__main__":
    main()

# dodaj wypisywanie poprawnych i niepoprawnych odpowiedzi
