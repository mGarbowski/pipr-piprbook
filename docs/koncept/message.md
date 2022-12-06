# Funkcjonalność związana z wiadomościami


## Message
Obiekt przechowujący informacje o wiadomości

* treść
* timestamp
* od kogo
* do kogo




## MessageSerializer
Przekształca obiekt Message na słownik (JSON) i słownik na obiekt Message

* `to_json(message) -> dict`
* `from_json(json) -> Message`


## MessageRepository
Protocol (interfejs) realizujący warstwę utrwalania obiektów Message.

Sposób utrwalania zależny od konkretnej implementacji


### Publiczne metody
* `save(message)`
* `get_messages_by_user(user) -> List[Message]`
* `get_messages_to_user(user) -> List[Message]`


## FilesystemMessageRepository
Implementacja protokołu MessageRepository. Utrwala Message w pliku JSON i umożliwia ich odczyt.

### Zależy od
* MessageSerializer

