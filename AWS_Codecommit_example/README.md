# Create a simple pipeline (CodeCommit repository)

- Created by following https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-codecommit.html

- The pipeline has two stages:

    A source stage (Source) for your CodeCommit source action.

    A deployment stage (Deploy) for your CodeDeploy deployment action.
 
# Step1: Open Codecommit

![code_commit_step1](https://user-images.githubusercontent.com/50704452/112804008-308bb380-9074-11eb-930e-5cca5846fe19.png)

# Step2 : Create a repo
![code_commit_step2](https://user-images.githubusercontent.com/50704452/112804483-c293bc00-9074-11eb-84c3-b2f74ca3d361.png)


# Step3: Create a IAM user

![code_commit_step4](https://user-images.githubusercontent.com/50704452/112806867-89108000-9077-11eb-8262-3acf54fc38fc.png)

# Step 4: Add permissions
![code_commit_step6](https://user-images.githubusercontent.com/50704452/112831291-06e28480-9094-11eb-888b-63b728e3261f.png)
![code_commit_step5](https://user-images.githubusercontent.com/50704452/112830880-70ae5e80-9093-11eb-9ecd-538a7064bcfc.png)


## Policies added to premissions

- AWSCodeCommitPowerUser
- AdministratorAccess

# Step 5: Add security credemtials 
1) Click on user
2) Click on security credentials
3) In terminal: 
> cd .ssh  
> ssh-keygen
4) Copy cat id_rsa.pub to Upload SSH public key
5) Generate username + password for HTTPS credentials

Two ways for accessing repo:

1) git clone ssh://{{SSH key ID}}@git-codecommit.us-east-1.amazonaws.com/v1/repos/Test-codecommit

2) git clone via https and enter username + password(Provided by HTTPS GIT credentials)

# Step 6: Add example files for repo

https://docs.aws.amazon.com/codepipeline/latest/userguide/samples/SampleApp_Linux.zip

![code_commit_step7](https://user-images.githubusercontent.com/50704452/112832390-89b80f00-9095-11eb-9901-d460ad982419.png)
![code_commit_step8](https://user-images.githubusercontent.com/50704452/112832557-c7b53300-9095-11eb-9491-1a61bfc84fd0.png)

# Step 7: Push files to repo

> git add *;git commit -m "Added test files to repo";git push

# Step 8 : Create a role

----
<details>
<summary>What are IAM roles?</summary>
<br>
    - An IAM role is a set of permissions that define what actions are allowed and denied by an entity in the AWS console
<br>
    - Role permissions are temporary credentials
</details>
<br>

----

 ### <u>Step to create role</u>
1) Select Trusted entity
2) Choose a use case
3) Add pemission 
> AmazonEC2RoleforAWSCodeDeploy
4) Add a name to role


To launch EC2 instance

----
<details>
<summary>What is a EC2 instance? </summary>
<br>
    - Virtual server in Amazon Web services that focuses on scalable computing capacity
<br>
    - Able to launch as many or as few virtual servers as you need, configure security and networking, and manage storage
<br>
<br>  
They contain:
<br>

 - Virtual computing environments, known as "Instances"

 - Preconfigured templates known as "Amazon Machine Images"(AMIs)
<br>
</details>
<br>

----


![code_commit_step9](https://user-images.githubusercontent.com/50704452/112839014-fdf6b080-909d-11eb-89cc-972136588bd6.png)

# Step 9 : Start CodeDeploy

----
<details>
<summary>What is a CodeDeploy? </summary>
<br>
    - Deployment service that automates application deployments to Amazon EC2 instances
<br>
    - Application ranging from :

    - Code
    - Scripts
    - Web and configuration files etc.
</details>
<br>

## <u>Steps in creating CodeDeploy<u>

![code_commit_step10](https://user-images.githubusercontent.com/50704452/112957961-42d42300-9142-11eb-95e2-8cd0cf9571bf.png)
----
![code_commit_step11](https://user-images.githubusercontent.com/50704452/112963326-8b420f80-9147-11eb-8249-7c9fd5716b4c.png)

![code_commit_step12](https://user-images.githubusercontent.com/50704452/112963376-99902b80-9147-11eb-862e-50aebfdd0123.png)

![code_commit_step13](https://user-images.githubusercontent.com/50704452/112963435-a90f7480-9147-11eb-88bd-e4c7cc397fa6.png)


## Creating a CodePipeline

-Details for source

![code_commit_step14](https://user-images.githubusercontent.com/50704452/112964230-6b5f1b80-9148-11eb-8689-9e1bf7ab0d25.png)