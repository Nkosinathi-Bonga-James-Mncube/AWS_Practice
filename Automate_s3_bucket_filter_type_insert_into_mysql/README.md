# Filter file type to add to MYSQL database(Part.2)
 - Automate downloading files in AWS s3 bucket using AWS credentials and setting up MYSQL database
 - Filter file type to add to MYSQL database.
 - This is just a oversimplified version of overall part.2 task to be done.

# Prerequisite
 - Add ssh RSA key(.pem)
 - Name of S3 bucket
 - AWS credentials
# Terms
<details>
<summary>What is AWS Credentials?</summary>
<br>
    - Credentials to authenticate user giving access to AWS resources

    - More info : 
    https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html
    https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_profiles.html
    

</details>
<details>
<summary>What is AWS CLI?</summary>
<br>
    - Command Line Interface (CLI) for interacting with AWS resources

    - More info :
    https://aws.amazon.com/cli/
</details>

<details>
<summary>What is AWS S3 bucket?</summary>
<br>
    - Provides object storage through a web service interface.Policies can be assigned to restrict access to bucket.

    - More info :
    https://aws.amazon.com/s3/
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html
</details>

# How it works
- Ansible playbook is run on localhost machine
- The following tasks are executed:

**1.Removes previous packages in ec2 instance**

**2.Installation of packages**
 1. Docker
 3. Python3
 4. Python-pip

**2.Creates .aws folder**
- Create a aws folder use to place aws credentials to use aws cli to access s3 bucket. Registering variables to output state of task

**3.Copy AWS settings to aws location**
- ec2 instance now has access to AWS resources.

**4.Create new folder for s3 bucket**
- Create a location for s3 bucket

**5.Use AWS CLI to execute command**
- Using AWS CLI to download s3 bucket in command 

**6.Start and lauch docker in ec2 instance**
 - Start docker service

**7.Installing Docker-compose** 
- curl url to install docker compose and changes read and write properties of docker compose. 

**8.Copy docker-compose settings in /tmp/mysql location**
- Copy docker-compose settings to lauch contain in ec2 instance.

**9.Run docker-compose mysql**
 - Set up MYSQL with docker-compose

**10. Loop through folders download from s3 bucket for .csv files**
 - Recusive search inside folder with '.csv', set fact results of location of .csv.

**11. Execute python script to insert into MYSQL database**
 - Run python script to accept arguments:

     a) .csv file path location

     b) Name of folder of each folder
   
 
# Installation
1. Create AWS ec2 instance

        https://github.com/Nkosinathi-Bonga-James-Mncube/DevOp_learning/tree/main/Cloud_formation/ec2
2. Create s3 bucket and files

        https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html

3. Install pipenv
4. Clone repo
5. Create pipenv
```
pipenv --three
```

6. Activte virtual environment
```
pipenv shell
```
7. Install packages
```
pip install -r requirements.txt
```
8. Run VPN (optinal)
9. SSH into EC2 instance:

```
sudo ssh -i intern.pem ec2-user@{{IP_ADDRESS}}
```
10. Replace the following: 
- Replace `{{ IP_Address }}` in `hosts` with ec2 instance IP addresss
 - Replace `{{ BUCKET_NAME }}` in `hosts`
 - Replace `{{ PASSWORD }}` in docker-compose/mysql/docker-compose.yml for MYSQL
 - Replace `{{ PASSWORD }}` in xml_scipt.py for MYSQL
 - Replace `{{ RSA KEY }}` in `host`
 - Replace `{{ AWS_ACCESS_KEY }}` `{ AWS_SECRET_ACCESS_KEY }}` `{{ REGION }}
` `{{ AWS_SESSION_TOKEN }}` in /.aws/credentials folder
- If you do not require a session token please remove this line in /.aws/
credentials folder
```
    aws_session_token= {{ AWS_SESSION_TOKEN }}
```
11. Run `main.yml` playbook

```
 ansible-playbook -i hosts main.yml
```
12. Files should be located at:

```
/home/ec2-user
```
13. To stop container, remove packages and remove folders
```
ansible-playbook -i hosts clean_up.yml
```
# Resources
- How to spin MySQL server with Docker and Docker Compose (plus Adminer)

    https://dev.to/sonyarianto/how-to-spin-mysql-server-with-docker-and-docker-compose-33b2


 - Deploy Jenkins with Docker and Ansible

    https://medium.com/@oleggorj/deploy-jenkins-with-docker-and-ansible-c76ee7854440

- Docker Ansible offical documentation

    https://docs.ansible.com/ansible/latest/collections/community/docker/docker_compose_module.html
    
- The definitive Guide to Docker compose

    https://gabrieltanner.org/blog/docker-compose
