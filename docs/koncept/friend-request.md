# Funkcjonalność związana z zaproszeniami do znajomych


## FriendRequest
Przechowuje informacje o zaproszeniu do znajomych
* od kogo
* do kogo
* timestamp


## FriendRequestSerializer
Przekształca obiekt FriendRequest na słownik (JSON) i słownik na obiekt FriendRequest

### Publiczne metody
* `to_json(friend_request) -> dict`
* `from_json(json) -> FriendRequest`


## FriendRequestRepository
Protocol (interfejs) realizujący warstwę utrwalania obiektów FriendRequest.

Sposób utrwalania zależny od konkretnej implementacji 

### Publiczne metody
* `save(friend_request)`
* `get_requests_by_user(user) -> List[FriendRequest]`
* `get_requests_to_user(user) -> List[FriendRequest]`


## FilesystemFriendRequestRepository
Utrwala FriendRequest w pliku JSON

### Zależy od
* FriendRequestSerializer