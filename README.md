
**SETTING UP THE DJANGO ENVIROMENT**

First setup the python envrioment, and install the django packages locally, this allows for development of the site and container simultaneously

```
python -m pip install venv
python -m venv $PATH_TO_PROJECT_DIR
cd $PATH_TO_PROJECT_DIR
```

Activate the venv before continuing
```
#~$:./Scripts/activate.ps1

#~$: (activate) $PATH_TO_PROJECT_DIR: >

django-admin startproject $PROJECT_NAME

#~$: pip freeze > $PROJECT_NAME/requirements.txt
```
In the $PROJECT_NAME/$PROJECT_NAME/settings.py file, change the ALLOWED_HOSTS to the following:

`ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]`


**SETTING UP THE ENVIROMENT INSIDE CONTAINER**

Docker build images based of the dockerfile, which provides the syntax for creating the layers.
Once an image is built docker will check the cache for existing images, this will prevent it from re-downloading packages
This image is built using python as a base image to allowing for deployment on systems with limited resources.

Start container:

`cd $PATH_TO_PROJ_DIR && docker-compose up`

Perform migrations 

`docker-compose.exe run gudweb python manage.py migrate`


**Linux Tools:**

Install docker using package manager and use your favorite text editor to begin working


**Windows Tools necessary:**

https://code.visualstudio.com/docs/?dv=win
https://desktop.github.com/
https://www.docker.com/products/docker-desktop

**Useful Django Info**

When making changes to the db use `manage.py migrate` to apply changes.


**Useful docker commands**

`docker-compose build` <- Build or rebuild the current service

`docker-compose config` <- Lists out the current compose file visible to docker-compose.exe

`[docker-compose|docker] ps`<- List Containers and information
```
PS ..\GitHub\WEBDEV_GitGud> docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED              STATUS              PORTS                    NAMES
85d14043bcef   webdev_gitgud_gudweb   "python manage.py ru…"   58 seconds ago       Up 56 seconds       0.0.0.0:8000->8000/tcp   webdev_gitgud_gudweb_1
5f60ad1b724c   webdev_gitgud_gudweb   "bash"                   About a minute ago   Up About a minute                            webdev_gitgud_gudweb_run_ed2c9564c90b
e995214a4e30   postgres               "docker-entrypoint.s…"   8 minutes ago        Up About a minute   5432/tcp                 webdev_gitgud_db_1
PS ..\GitHub\WEBDEV_GitGud> 
```
`[docker-compose|docker] image` <- List Images stored in docker daemon

`docker-compose run $service_name $command_to_run` <- executes a command on the container, good for troubleshooting
```
PS ..\GitHub\WEBDEV_GitGud> docker-compose.exe run gudweb bash
Starting webdev_gitgud_db_1 ... done
Creating webdev_gitgud_gudweb_run ... done
root@5f60ad1b724c:/src# ls
Dockerfile  gitgud_web_source  manage.py  requirements.txt  sh_with_pie.py
root@5f60ad1b724c:/src
```

`docker-compose up` <- Start the container
```
(WEBDEV_GitGud) PS ..\GitHub\WEBDEV_GitGud> docker-compose.exe up
webdev_gitgud_db_1 is up-to-date
Recreating webdev_gitgud_gudweb_1 ... done
Attaching to webdev_gitgud_db_1, webdev_gitgud_gudweb_1
db_1      | The files belonging to this database system will be owned by user "postgres".
db_1      | This user must also own the server process.
db_1      |
...
gudweb_1  | Watching for file changes with StatReloader
gudweb_1  | Performing system checks...
gudweb_1  |
gudweb_1  | System check identified no issues (0 silenced).
gudweb_1  |
gudweb_1  | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
gudweb_1  | Run 'python manage.py migrate' to apply them.
gudweb_1  | March 04, 2021 - 18:44:58
gudweb_1  | Django version 3.1.6, using settings 'gitgud_web_source.settings'
gudweb_1  | Starting development server at http://0.0.0.0:8000/
gudweb_1  | Quit the server with CONTROL-C.
```


Init Webapp (This only needs to be run for new project, the git repo should include an already initialized project in the gitgud_web_source directory):

`docker-compose.exe run gudweb django-admin startproject gitgud_site .`

**REFERENCES**

dockerfile - https://docs.docker.com/engine/reference/builder/

docker + python app
https://blog.bitsacm.in/django-on-docker/

https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

Dockerfile - Contains instructions for creating docker container

sh_with_pie.py - Python program to test python's subprocess module in the container

Guide to create the docker compose image.
https://docs.docker.com/compose/django/