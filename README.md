
# Welcome to Simple-api!

A simple api that exposes some routes for names and birth dates

### Run locally

	virtualenv -p python3 env && . env/bin/activate
    pip install --trusted-host pypi.python.org -r requirements.txt
    cd src
    python3 app.py 
    
Run tests:

  > python3 -m unittest discover -s tests/ -p '*_test.py' -v

### Run in docker

    docker build -t simple-api .
    docker run -d --name simple-api -p 8080:8080 simple-api

Run tests:

  > docker exec -i simple-api bash -c 'python3 -m unittest discover -s tests/ -p '*_test.py' -v'    
    

### API routes

|      Title          |Method                          |Route                         |
|----------------|-------------------------------|-----------------------------|
|Get user|GET            |/hello/\<username>            |
|Create user          |POST            |/hello            |
|Update user          |PUT|/hello/\<username>|
|Delete user          |DELETE|/hello/\<username>|


**Diagrams:**

![System diagram](https://i.ibb.co/XX1Dmfv/Aws-diagram.png)

Good luck.
