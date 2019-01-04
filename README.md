# flask-store-rest-api

## Description
A basic store REST API using Flask and SQLAlchemy, with sqlite3

## Dependencies:
1, flask
2. flask-restful
3. flask-jwt
4. flask-sqlalchemy
5. flask-bcrypt

## Implementation
1. Clone this repository:
```
git clone https://github.com/danielattiach/flask-store-rest-api.git
```
2. Create a virtual environment (pipenv in this case):
```
pipenv shell
```
3. Install dependencies listed above:
```
pipenv install Flask flask-restful Flask-JWT Flask-SQLAlchemy flask-bcrypt
```
4. Run app.py
```
python app.py
```

# Notes
On the first request to the API, a data.db file will be created, which is why the first request my take longer.
Now you can access the routes specified in app.py.
