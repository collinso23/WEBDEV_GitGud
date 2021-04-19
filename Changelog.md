**Friday, April 2, 2021 8:27:59 PM**

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

**Sat Apr  3 02:05:12 EDT 2021**

Created new pages to test dig and ping `localhost:8000/tools/pingpage` or `/tools/digpage`. Stdout is still not working, but runTool should be the primary method of invoking shell commands. It takes in two arguments. The tool to run, and the parameters (ie. `runTool("ping","-c4 -q www.google.com")`, or `runTool("dig","www.google.com")`). Eventually these arguments will be captured by the html form on the website, but for now they are hard coded. 

**Tuesday, April 13, 2021 11:46:50 AM**

Re-strucutured the dockerfile so that tools were getting coppied into the src for the web app. The test pages, `tools/testdig`, `tools/testmtr`, and `tools/testping` are working. Got the DB image running. Next we need to implement the DB into the django app. 

The DB is running, but keep crashing on start, and is not accepting connections.

added mount of source code into `/development` on the gudweb container so rebuild is not necessary to test changes


**Saturday, April 17, 2021 4:32:34 PM**

Implemented the static files for the website. Got the static content to be served following the tutorial here  https://www.youtube.com/watch?v=c3GFUpRx8pw.

The website is using conflicting styles, id like to move everything over from the multiple pages into a more dynamic single page. 

Create a test view in templates called `test_form`. It will take in options and print them out, which is similar words