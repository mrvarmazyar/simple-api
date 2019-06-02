
  

# Welcome to Simple-api!

A simple API for managing users! 

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
    
### Infrastructure provisioning

Export AWS Credentials or AWS profile or set environment variables in gitlab:

    export AWS_ACCESS_KEY_ID=your_access_key
    export AWS_SECRET_ACCESS_KEY=your_secret_access_key

Deploy all the infrastructure needed on AWS using Terraform:

```
# terraform get
# terraform init
# terraform plan -out config
# terraform apply config
```

To destroy the entire infrastructure, run the following command

```
# terraform destroy
```

#### deploying individual AWS components

Configure a VPC:

```
terraform apply -target=module.vpc
```

Configure the auto scaling group and launch configuration via EC2:

```
terraform apply -target=module.ec2
```

Configure and launch RDS:

```
terraform apply -target=module.rds
```

Configure a new ECS Cluster with a service:

```
terraform apply -target=module.ecs
```

### API routes

|      Title          |Method                          |Route                         |
|----------------|-------------------------------|-----------------------------|
|Get user|GET            |/hello/\<username>            |
|Create user          |POST            |/hello            |
|Update user          |PUT|/hello/\<username>|
|Delete user          |DELETE|/hello/\<username>|


**Diagrams:**
![Aws diagram](https://i.ibb.co/Q9Ww3vQ/aws-diagram.png)

Good luck.