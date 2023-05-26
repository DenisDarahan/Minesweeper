Minesweeper
====

![main window screenshot](screenshots/main_window.png?raw=true)

**Another one minesweeper. But it's mine.**

This implementation contains **command line interface**, 
**graphic user interface** and **server** which stores users' 
wins.

GUI is based on the cross-platform framework **Kivy**. 
**SQLite** is used as local database.

Server is based on the **FastAPI** framework. **Postgres** is 
used as server-side database.

Server is built in asynchronous style. API allows to 
register a new user using OAuth2 protocol.
