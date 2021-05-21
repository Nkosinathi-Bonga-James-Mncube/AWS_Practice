# Automating downloading files in AWS s3 bucket (Part.1)
 - Automate downloading files in AWS s3 bucket using AWS credentials and setting up MYSQL database
 - This is just a oversimplified version of overall part.1 task to be done.

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
    - Command Line Interface (CLI) for interactiving with AWS resources

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
- To place AWS Credentials to be a authenticated user to gain access to your AWS S3 bucket.

**3.Copy AWS credentials to .aws folder**
- ec2 instance now has access to AWS resources.

**4.Use AWS CLI to execute command**
- Using AWS CLI to download s3 bucket in command 

**5.Start and lauch docker in ec2 instance**
 - Start docker service

**6.Installing Docker-compose** 
- curl url to install docker compose and changes read and write properties of docker compose. 

**7.Copy docker-compose settings in /tmp/mysql location**
- Copy docker-compose settings to lauch contain in ec2 instance.

**8.Run docker-compose mysql**
 - Set up MYSQL with docker-compose

 
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

    https://gabrieltanner.org/blog/docker-
    
- Install Docker compose

    https://docs.docker.com/compose/install/
