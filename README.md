# latm-blog-backend
FastApi backend for the latm-blog project.

# Development Setup
## Dependencies
This project uses venv. So the following packages are needed
 - ```python3``` (recommend use version 3.10)
 - ```virtualenv``` (installed via pip)
 - ```make```
 - ```docker & docker compose```
## Setup
1. ```git clone git@github.com:PascalHoenisch/latm-blog-backend.git```
2. ```cd latm-blog-backend```
3. ```make setup``` - this installs venv
4. ```docker compose up -d``` - start the database
5. ```make start``` - starts the api server
6. have fun with ```localhost:8000/docs```