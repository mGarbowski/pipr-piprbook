# Funkcjonalność związana z logowaniem / uwierzytelnianiem


## Authentication
Zarządza uwierzytelnianiem

Porównuje dane podane przez użytkownika przy logowaniu z danymi z UserRepository
Przechowuje stan - informacje o aktualnie zalogowanym użytkowniku

### Zależy od
* UserRepository

### Publiczne metody
* `log_in(login, password)`
* `log_out()`
