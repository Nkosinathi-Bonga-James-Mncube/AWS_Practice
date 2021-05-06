# AWS CloudFormation Init 
 - Install Docker using AWS::CloudFormation::Init

 # Terms

<details>
 <summary>What is AWS cloudformation?</summary>

    - AWS service that uses template files to automate the setup of AWS resources
    - Described as IaC(Infrastructure-as-Code) tool for automation setup and deployment
 </details>  

<details>
 <summary>What is AWS::CloudFormation::Init?</summary>

    - Contains metadata(or attribute) on an Amazon EC2 instance (e.g Packages,Service, Groups etc)
    - Helper scripts are used installing and starting services (e.g. cfn-init , cfn-signal,cfn-get-metadata,cfn-hup)
   
     Helper scripts used in the template:
    - cfn-init : receiving and intrepreting metadata for installing,start services and creating files
    - cfn-signal: Use CreatePolicy to synchronize with resources send signal back to AWS Cloudformation(e.g Get status of ec2 creation outcome)

 </details>  
<br>
 

# CloudFormation Design diagram

<img width=30% height=30% src=https://user-images.githubusercontent.com/50704452/116811460-bdc99880-ab49-11eb-9cc9-704729e57b0f.png>

<br>

# Pre-requisite 
N.B please remnber to add `KeyName` + "Security group for port 22" in template to SSH into ec2
<br>


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
aws cloudformation create-stack --stack-name CreateEc2 --template-body file://ec2-Docker.yaml
```

![Screenshot from 2021-05-06 14-40-48(1)](https://user-images.githubusercontent.com/50704452/117300684-1666a180-ae7a-11eb-95c9-b05facb9a338.png)


5. Get Public IP address for instance
```
    aws ec2 describe-instances
```
5. SSH into  box
```
ssh -i ec2key.pem ec2-user@{{IP_ADDRESS}}
``` 

# Template syntax
- AWS::EC2::Instance
  
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html

 - AWS::EC2::SecurityGroup

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html

 - AWS::EC2::SecurityGroupIngress

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html

 - AWS::EC2::EIP

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html

-  AWS::AWS::CloudFormation::Init

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html


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
# References
 - AWS CloudFormation Init with Examples

    https://devops4solutions.com/aws-cloudformation-init-with-examples/

