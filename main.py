import sys
import gramy
import dodawanie_pytan
import usuwanie
import wyswietl_wszystko

if "--help" in sys.argv or "-h" in sys.argv:
    print("""
Dostępne opcje:

python main.py              -     - uruchamia quiz
python main.py --dodaj     -d     - dodaje nowe pytanie
python main.py --usun      -u     - usuwa pytanie
python main.py --wyswietl  -w     - wyświetla wszystkie pytania
python main.py --help      -h     - pokazuje tę pomoc
""")
elif "--dodaj" in sys.argv or "-d" in sys.argv:
    dodawanie_pytan.main()
elif "--usun" in sys.argv or "-u" in sys.argv:
    usuwanie.main()
elif "--wyswietl" in sys.argv or "-w" in sys.argv:
    wyswietl_wszystko.main()
else:
    gramy.main()
