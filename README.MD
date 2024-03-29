# Covid Tracker with CAC scanner

Physically "logging" events ought to be a thing of the past. In the Marine Corps, that aging concept still lives on. This proof of 
concept is there to help supplement or remove a physical Marine to write anything down. With the pandemic of the Coronavirus, 
logging who enters an establishment becomes increasingly important to mitigate community spread of the virus.

## Problem

Camp Hansen Exchange assigned multiple Marines to manually log anyone who enters the building. During rush hours, a very long line 
could be seen coming out of the entrance. Once someone reaches the front, a Marine will take basic information and “legibly” 
transcribe it on loose printed log sheets. Sometimes, they will have the individual write their own information down with the same pen. Some issues arise such as the validity of who actually wrote what. The problems are the unintentional spread due 
to a single pen, legibility of the handwriting, the validity of the individual, and the quick seartch of an individual. This could cause a second or third-order 
effect in regards to tracing who was a close contact or a positive case.

## Solution

Common Access Cards (CAC) are widely owned for anyone wanting access to a federal location such as a military base. Therefore, they ought to be used for the logging process. With a good scanner (see below for specifics) 
and CACs, logging events to track individuals will provide a stand-alone technology solution.

## Hardware Requirements

1. Any Hands-Free and automatic scanner with a specification to read the `2D PDF417` type barcodes. That is because the front of the CAC is a 2D PDF417 type barcode
   1. For example: I used the TEEMI Handsfree 1D 2D Barcode Scanner bought on Amazon. For a military purchase, please see your supply about purchasing it through Servmart or other government procurement avenue.
2. Laptop or raspberry pi

Software Requirements

1. Installation of [Docker](https://docs.docker.com/get-docker/)
1. Installation of [Python3](https://www.python.org/downloads/)
1. Recommend: [Ubuntu](https://ubuntu.com/#download) Operating System

## Set Up
1. `git clone https://github.com/marinecoders/covid_tracker_scanner.git`
2. `cd covid_tracker_scanner`
3. Create `.env` in the `covid_project` directory with something like:
```.env
DJ_SECRET_KEY=super-secret-key
DJ_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0
DJ_DEBUG=True
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=change_database_name
SQL_USER=change_super_cool_user
SQL_PASSWORD=change_super_secret_password
SQL_HOST=db
SQL_PORT=5432
```
4. Create `.env.db` in the `covid_project` directory with something like:

```.env
POSTGRES_DB=change_database_name
POSTGRES_USER=change_super_cool_user
POSTGRES_PASSWORD=change_super_secret_password
```

5. go back to the root directory with the `docker-compose` file
1. `docker-compose up --build`
3. There might be an error that the database does not exist.
   1. If so, run `docker-compose down -v` then `docker-compose up --build`
   2. Afterwards, in a different terminal at the same directory, you might need to apply the tables to the database with `docker-compose exec web python manage.py migrate`
4. Open a browser and navigate to [localhost:8000](http://localhost:8000/)


## Creating a .desktop file for execution (ONLY WORKS ON UBUNTU OS)
Thank can only work if and only if `docker-compose` is up and running. Thoughts about automating the `docker-compose` is to run it upon start up so that the user does not have to do anything execpt the below.

This is to help the automation to "Marine proof" the application
1. Have the docker-compose run on start up through the `Startup Application Preferences`
1. Create the file as `example.desktop` to launch the browser to the correct url
   Add the following
   ```
   [Desktop Entry]
   Name=Example Name
   Comment=Launch browser to running application
   Exec=sh -c "path/to/run_me.sh"
   Icon=/path/to/cool/icon.svg
   Terminal=false
   Type=Application
   Version=1.0
   ```   
   Take note of the `run_me.sh`. You will have to create that file at the path you determined
1. Create the `path/to/run_me.sh`. Inside it should look something like:
   ```bash
   #!/bin/bash
   firefox http://localhost:8000   
   ```
2. ensure to make it executable with `chmod +x run_me.sh`
1. Afterwards, make sure the example.desktop can be be launched by right clicking on it and select `Allow Launching`
1. See the icon change.

## Built With

* [Django](https://www.djangoproject.com/) - High-Level Python Web Framework
* [Docker](https://www.docker.com/) - Containerization
* [Bootstrap](https://getbootstrap.com/) - Front-End open source toolkit
