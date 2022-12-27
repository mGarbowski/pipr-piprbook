# PIPRbook
Projekt semestralny

[Pomysł na realizację](docs/koncept/koncept.md)

## Polecenie
Proszę zaimplementować symulator prostego serwisu społecznościowego. 

Serwis powinien umożliwiać dodawanie znajomych i wysyłanie wiadomości. 

Użytkownik powinien mieć możliwość:
* zalogowania się do aplikacji
* dodania zdjęcia profilowego
* dodania krótkiej notki na swój temat
* zaproszenia innego użytkownika do znajomych
* wysłania wiadomości do znajomego
* odczytania otrzymanych wiadomości

Program musi posiadać warstwę trwałości („baza danych” symulowana poprzez zapis do plików i czytanie z nich).


## Uruchomienie
### Zainstalowanie zależności
```bash
pip install -r requirements.txt
```

W katalogu projektu
```bash
python -m gui.main {ścieżka do pliku z bazą danych}
```