# Tornado Framework Tutorial

This is the code written while following [Nicholas Hunt-Walker's](https://opensource.com/users/nhuntwalker) [Tornado Framework Tutorial](https://opensource.com/article/18/6/tornado-framework).

# Set-up

The application must be built locally before other commands will work.

## Build the application

```bash
python setup.py develop
```

## Set up the database

```bash
createuser tornado_todo
createdb tornado_todo
init_db
```

## Run the local development server

```python
serve_app
```

The application can now be accessed at [http://127.0.0.1:8888/](http://127.0.0.1:8888)