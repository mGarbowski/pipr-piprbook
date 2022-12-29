# PIPRbook
Projekt semestralny

~~[Pomysł na realizację](docs/koncept/koncept.md)~~ nieaktualne

## Polecenie
Proszę zaimplementować symulator prostego serwisu społecznościowego. 

Serwis powinien umożliwiać dodawanie znajomych i wysyłanie wiadomości. 

Użytkownik powinien mieć możliwość:
* [x] zalogowania się do aplikacji
* [x] dodania zdjęcia profilowego
* [x] dodania krótkiej notki na swój temat
* [ ] zaproszenia innego użytkownika do znajomych
* [x] wysłania wiadomości do znajomego
* [x] odczytania otrzymanych wiadomości

Program musi posiadać warstwę trwałości („baza danych” symulowana poprzez zapis do plików i czytanie z nich).


## Uruchomienie
Projekt testowany na wersji Pythona 3.8.10

W wersji 3.11 pojawiają się problemy z kompatybilnością z PySide2

W katalogu projektu
```bash
python -m gui.main {ścieżka do pliku z bazą danych}
```

### Zainstalowanie zależności
```bash
pip install -r requirements.txt
```

### Wygenerowanie klas do obsługi widgetów
```bash
./generate_components.sh
```

