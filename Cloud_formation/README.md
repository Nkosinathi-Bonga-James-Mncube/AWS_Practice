# Launching ec2 instance using AWS CloudFormation
 - Deploy cloud formation template to create cloudformation stack using aws cli

<details>
 <summary>What is AWS cloudformation?</summary>

    - AWS service that uses template files to automate the setup of AWS resources
    - Described as IaC(Infrastructure-as-Code) tool for automation setup and deployment
 </details>  

## Pre-requisite 
N.B please remnber to add `KeyName` + "Security group for port 22" in template to SSH into ec2
# Installation
1. Install AWS CLI : https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html 
1. Copy AWS credentials from AWS Education account and paste in cd ~/.aws/credentials
![credentials_github](https://user-images.githubusercontent.com/50704452/116236401-51bcee00-a75f-11eb-9014-53b4e92f5f50.png)
 - NB: To test run : `aws s3 ls`
2. To Create a key pair
```
aws ec2 create-key-pair --key-name ec2key --query 'KeyMaterial' --output text > ec2key.pem
```

3. Change permission on key
```
chmod 400
```
4. Create cloud formation stack
```
aws cloudformation create-stack --stack-name CreateEc2 --template-body file://ec2-example.yaml
```

![create_stack](https://user-images.githubusercontent.com/50704452/116240624-5506a880-a764-11eb-9c2d-84f9e1b8f939.png)

5. Get Public IP address for instance
```
    aws ec2 describe-instances
```
5. SSH into  box
```
ssh -i ec2key.pem ec2-user@{{IP_ADDRESS}}
``` 

# Commands
 - To validate cloud formation template use:
 ```
 aws cloudformation validate-template --template-body file://ec2-example.yaml
 ```
 - To list validate key-pairs
 ```
 aws ec2 describe-key-pairs
 ```
 ![keys](https://user-images.githubusercontent.com/50704452/116238931-51722200-a762-11eb-8a3d-41b16913d469.png)

 - Check status of CloudFormation stack
 ```
 aws cloudformation describe-stacks

 ```
 ![complete](https://user-images.githubusercontent.com/50704452/116241342-18877c80-a765-11eb-94c8-be23193e6396.png)

- Check event of Cloud formation stack
```
aws cloudformation describe-stack-events --stack-name CreateEc2
```
- Delete cloud formation stack
```
aws cloudformation delete-stack --stack-name myteststack
```