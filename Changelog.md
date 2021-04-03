Friday, April 2, 2021 8:27:59 PM

Commented out Postgres info from `docker-compose.yaml` we are implementing mysql as the DB
For the time being I also enabled sqlite (django default db) by changing `gitgud_web_source/gitgud_web_source/settings.py`. So that a superuser could be created and the admin page accessed.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Started the index.html for tools page. 
Got index to load subprocess but its currently not returning stdout only error code 1.
TODO: Figure out how to get stdout of subprocess on webpage.

