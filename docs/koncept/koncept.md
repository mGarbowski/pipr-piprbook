# Koncept
Interfejs użytkownika graficzny / tekstowy?

Warstwa utrwalania zrealizowana przez zapisywanie / odczytywanie plików JSON.
Wszystkie będą wyglądać podobnie, może dałoby się stworzyć jakieś generyczne Repository.

Application spina główną funkcjonalność z interfejsem użytkownika

Zdjęcia przekazywane przez nazwę pliku (CLI) i przechowywane w folderze.
Nie mam pomysłu jak to zrealizować nie ograniczając się tylko do systemu plików,
tak żeby zachować np możliwość trzymania ich w bazie danych.

Porządne logowanie, bez przechowywania w jawny sposób hasła

Na niektóre rzeczy (Serializer) na pewno nie potrzeba oddzielnych klas (naleciałość z Javy)

* Klasy User, Message, FriendRequest tylko przechowują informacje
* Klasy typu Service modyfikują / dodają nowych użytkowników / wiadomości / zaproszenia
* Klasy typu Repository utrwalają obiekty domenowe
* Klasy typu FilesystemRepository implementują interfejs Repository i utrwalają obiekty w plikach JSON
* Klasy typu Serializer tłumaczą obiekty dmoenowe na słowniki (JSON) i na odwrót

## Klasy / moduły
* Application
* Authentication
* User
  * UserService
  * UserSerializer
  * UserRepository (Protocol)
    * FilesystemUserRepository
    * SqliteUserRepository?
  * FilesystemPhotoRepository
* Message
  * MessageSerializer
  * MessageRepository (Protocol)
    * FilesystemMessageRepository 
    * SqliteMessageRepository?
* FriendRequest
  * FriendRequestRepository (Protocol)
    * FilesystemFriendRequestRepository
    * SqliteFriendRequestReposiotry?
  * FriendRequestSerializer
* Generyczne Repository?
* Generyczne FilesystemRepository?
