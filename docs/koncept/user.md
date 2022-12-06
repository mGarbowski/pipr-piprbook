# Funkcjonalność związana z użytkownikiem

## User
Przechowuje informacje o użytkowniku
* UUID
* login / username
* sól
* hash hasła
* email
* bio
* zdjęcie
* znajomi

## UserService
Główny interfejs do wchodzenia w interakcję z użytkownikiem.

Używa Authentication, żeby ograniczyć dostęp do zasobów / czynności np:
* użytkownik może przeczytać tylko swoje wiadomości
* użytkownik może zaakceptować tylko zaproszenia skierowane od niego

### Zależy od
* UserRepository
* MessageRepository
* FriendRequestRepository
* PhotoRepository
* Authentication

### Metody publiczne
* `get_user_by_id(id) -> User`
* `save_user(user) -> User`
* `get_messages(user) -> List[Message]`
* `send_message(message)`
* `add_profile_picture(picture, user)`
* `set_bio(text, user)`
* `send_friend_request(friend_request)`
* `accept_friend_request(friend_request)`

## UserSerializer
Przekształcenie obiektu User na słownik (JSON) i słownika na obiekt User

Listę znajomych przechowuje jako listę ID znajomych

### Metody publiczne
* `to_json(user) -> dict`
* `from_json(json) -> User`


## UserRepository
Protocol (interfejs) realizujący warstwę utrwalania.

Sposób utrwalania zależny od implementacji protokołu


### Metody publiczne
* `save(user)`
* `get_by_id(id) -> User`
* `find_by_username(username) -> User`


## FilesystemUserRepository
Implementacja protokołu UserRepository utrwalająca użytkowników w pliku JSON

### Zależy od
* UserSerializer


## PhotoRepository
Zapisuje plik zdjęcia w odpowiednim folderze

### Metody publiczne
* `save_photo(filename)`
* `get_photo(filename) -> file`
