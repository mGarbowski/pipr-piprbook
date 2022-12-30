# PIPRbook

Projekt semestralny z podstaw informatyki i programowania

## Polecenie

Proszę zaimplementować symulator prostego serwisu społecznościowego.

Serwis powinien umożliwiać dodawanie znajomych i wysyłanie wiadomości.

Użytkownik powinien mieć możliwość:

* [x] zalogowania się do aplikacji
* [x] dodania zdjęcia profilowego
* [x] dodania krótkiej notki na swój temat
* [x] zaproszenia innego użytkownika do znajomych
* [x] wysłania wiadomości do znajomego
* [x] odczytania otrzymanych wiadomości
* [x] Program musi posiadać warstwę trwałości („baza danych” symulowana poprzez zapis do plików i czytanie z nich).

## Uruchomienie / Instalacja

Projekt testowany na wersji Pythona 3.8.10

W wersji 3.11 pojawiają się problemy z kompatybilnością z PySide2

### Uruchomienie GUI

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

### Uruchomienie testów

Testy jednostkowe

```bash
pytest ./tests
```

Sprawdzenie typów

```bash
mypy core persistence gui
```
