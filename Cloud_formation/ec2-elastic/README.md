# Launching ec2 instance with elastic IP using AWS CloudFormation
 - Deploy cloud formation template to create cloudformation stack using aws cli

# Terms

<details>
 <summary>What is AWS cloudformation?</summary>

    - AWS service that uses template files to automate the setup of AWS resources
    - Described as IaC(Infrastructure-as-Code) tool for automation setup and deployment
 </details>

<details> 
 <summary>What is AWS::EC2::SecurityGroupIngress</summary>

    - Inbound rule recieve trafffic from IPv4
    - Can specfiy protocol (e.g TCP)
</details>

<details>
 <summary>What is CidrIp?</summary>

    - IPv4 CIDR range

 </details>

<details>
 <summary>What is AWS::EC2::EIP?</summary>

    - Reserves public IP address that you can assign to any EC2 instance in a particular region.
    
 </details>
 <br>


# Pre-requisite 
N.B please remnber to add `KeyName` + "Security group for port 22" in template to SSH into ec2
# Installation
1. Install AWS CLI : https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html 
1. Copy AWS credentials from AWS Education account and paste in cd ~/.aws/credentials
![credentials_github](https://user-images.githubusercontent.com/50704452/116236401-51bcee00-a75f-11eb-9014-53b4e92f5f50.png)
 - NB: To test run : `aws s3 ls`
2. To Create a key pair
```
aws ec2 create-key-pair --key-name ec2elastic --query 'KeyMaterial' --output text > ec2elastic.pem
```

3. Change permission on key
```
chmod 400
```
4. Create cloud formation stack
```
aws cloudformation create-stack --stack-name CreateE2cElastic --template-body file://ec2-elastic.yaml
```
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

# Commands
 - To validate cloud formation template use:
 ```
 aws cloudformation validate-template --template-body file://ec2-elastic.yaml
 ```
 - To list validate key-pairs
 ```
 aws ec2 describe-key-pairs
 ```

 - Check status of CloudFormation stack
 ```
 aws cloudformation describe-stacks

 ```
- Check event of Cloud formation stack
```
aws cloudformation describe-stack-events --stack-name CreateEc2
```
- Delete cloud formation stack
```
aws cloudformation delete-stack --stack-name myteststack
```