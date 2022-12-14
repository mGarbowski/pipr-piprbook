# Koncept
Interfejs użytkownika graficzny / tekstowy

Aplikacja podzielona na warstwy
* Główna logika
* Warstwa utrwalania (komunikacja z bazą danych)
* Interfejs użytkownika

Warstwa utrwalania zrealizowana przez zapisywanie / odczytywanie plików JSON.
Wszystkie będą wyglądać podobnie, może dałoby się stworzyć jakieś generyczne Repository.

Application spina główną funkcjonalność z interfejsem użytkownika

Zdjęcia przechowywane w folderze

Bezpieczne logowanie, bez przechowywania w jawny sposób hasła

* Klasy modelowe User, Message, FriendRequest tylko przechowują informacje
* Klasy typu Service modyfikują / dodają nowych użytkowników / wiadomości / zaproszenia
* Klasy typu Repository utrwalają obiekty domenowe
* Klasy typu FilesystemRepository implementują interfejs Repository i utrwalają obiekty w plikach JSON
* Klasy typu Serializer tłumaczą obiekty modelowe na słowniki (JSON) i na odwrót

## Klasy / moduły
* Application
* [Authentication](authentication.md)
* [User](user.md)
  * UserService
  * UserSerializer
  * UserRepository (Protocol)
    * FilesystemUserRepository
    * SqliteUserRepository?
  * FilesystemPhotoRepository
* [Message](message.md)
  * MessageSerializer
  * MessageRepository (Protocol)
    * FilesystemMessageRepository 
    * SqliteMessageRepository?
* [FriendRequest](friend-request.md)
  * FriendRequestRepository (Protocol)
    * FilesystemFriendRequestRepository
    * SqliteFriendRequestReposiotry?
  * FriendRequestSerializer
* Generyczne Repository?
* Generyczne FilesystemRepository?
