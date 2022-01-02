# Urban API

Urban API is an open source API to organise football matches with two teams of 5 players each.

## Basic Features

The organization of the match works as follows:

1 - The organizator inserts the match data (address, day and hour) and then a match with two unique teams is created

2 - The players should sign up by entering personal data (name and mail)

3 - The players can list all available matches and, once signed in, subscribe to them

4 - The players should select a team from a match, as the teams are unique for each match

All data is stored on a SQLite database.


## Routes

* CRUD match:

GET     /matches/ - lists a match or all available matches

POST    /matches/ - adds a match

PUT     /matches/ - updates a match

DELETE  /matches/ - deletes a match

* CRUD players:

GET     /players/ - lists a player or all players

POST    /players/ - adds a player

PUT     /players/ - updates a player

DELETE  /players/ - deletes a player

* CRUD team:

GET     /teams/ - lists the players of a team

POST    /teams/ - adds a player to a team

DELETE  /teams/ - deletes a player from a team

## Advanced Features

The next step to this API would be:

* A waiting list for a full match