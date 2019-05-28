# Welcome to Simple-api!

A simple api that exposes some routes for names and birth dates

**To run project localy run this commands:**
	> `virtualenv -p python3 env && . env/bin/activate`
    > `pip install --trusted-host pypi.python.org -r requirements.txt`
    > `cd src`
    > `python3 app.py` 
**To run project In docker run this commands:**
   > `docker build -t simple-api .`
   > `docker run -d --name simple-api -p 8080:8080 simple-api`

**API routes:**

|      Title          |Method                          |Route                         |
|----------------|-------------------------------|-----------------------------|
|Get Username's birthdate|GET            |/hello/\<username>            |
|Post Username and birthdate          |POST            |/hello            |
|Update Username and birthdate          |PUT|/hello/\<username>|
|Delete User data          |DELETE|/hello/\<username>|


**Diagrams:**

![enter image description here](https://picasaweb.google.com/107013579644100072093/6695988051737016961#6695988048131509362)

Good luck.
