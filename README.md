# Tornado Framework Tutorial

This is the code written while following [Nicholas Hunt-Walker's](https://opensource.com/users/nhuntwalker) [Tornado Framework Tutorial](https://opensource.com/article/18/6/tornado-framework).

## Set-up

The application must be built locally before other commands will work.

### Build the application

```bash
python setup.py develop
```

### Set up the database (requires [postgres](http://www.postgresqltutorial.com/install-postgresql/))

```bash
createuser tornado_todo
createdb tornado_todo
init_db
```

### Run the local development server

```python
serve_app
```

The application can now be accessed at [http://127.0.0.1:8888/](http://127.0.0.1:8888)

## Usage

### Add example user to database

```sql
INSERT INTO public.user (username, email, password, date_joined, token) 
VALUES ('kayra', 'kayra@test.com', 'badpass', NOW(), 'test_token');
```

### Make GET request

GET request to [http://127.0.0.1:8888/tasks/kayra](http://127.0.0.1:8888/tasks/kayra):

```bash
curl --request GET \
  --url http://127.0.0.1:8888/tasks/kayra
```

Should respond with:

```javascript
{
	"username": "kayra",
	"tasks": []
}
```

### Make POST request

POST request to [http://127.0.0.1:8888/tasks/kayra](http://127.0.0.1:8888/tasks/kayra) with `Task` name and `Task` note:

```bash
curl --request POST \
  --url http://127.0.0.1:8888/tasks/kayra \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form 'name=Finish tutorial' \
  --form 'note=Tutorial available at https://opensource.com/article/18/6/tornado-framework'
```

Should respond with:

```javascript
{
	"message": "Task created",
	"Task": "Finish tutorial"
}
```