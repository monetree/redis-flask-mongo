# Steps to run this app locally with mongodb

1. install redis (`https://redis.io/`)
2. install mongodb (`https://www.mongodb.com/`)
3. create database with named `dummy` in mongodb
4. dump the data `comments.csv` or `comments.json` into db using `mongoexport --db=dummy --collection=comments --out=comments.json` command

5. install requiremets using `pip install -r requirements.txt` (You can use virtualenv also as i am using)
6. run `python app.py` in current directory
7. in browser run `http://127.0.0.1:5000/` 


I have added comments properly for each use cases and both db connection and how to use it for the codes.


I have used `Flask-PyMongo` for databse query from mongodb and `redis` client for caching