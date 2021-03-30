# Create a simple pipeline (CodeCommit repository)

- Created by following https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-codecommit.html

- The pipeline has two stages:

    A source stage (Source) for your CodeCommit source action.

    A deployment stage (Deploy) for your CodeDeploy deployment action.
 
Step1: Open Codecommit

![code_commit_step1](https://user-images.githubusercontent.com/50704452/112804008-308bb380-9074-11eb-930e-5cca5846fe19.png)

Step2 : Create a repo
![code_commit_step2](https://user-images.githubusercontent.com/50704452/112804483-c293bc00-9074-11eb-84c3-b2f74ca3d361.png)


Step3: Create a IAM user

![code_commit_step4](https://user-images.githubusercontent.com/50704452/112806867-89108000-9077-11eb-8262-3acf54fc38fc.png)

Step 4: Add permissions
![code_commit_step6](https://user-images.githubusercontent.com/50704452/112831291-06e28480-9094-11eb-888b-63b728e3261f.png)
![code_commit_step5](https://user-images.githubusercontent.com/50704452/112830880-70ae5e80-9093-11eb-9ecd-538a7064bcfc.png)


* Added 
- AWSCodeCommitPowerUser
- AdministratorAccess  
NB. if any issues arise , 
AWSCodeCommitPowerUser 

Step 5: Add security credemtials 
1) Click on user
2) Click on security credentials
3) In terminal: 
> cd .ssh  
> ssh-keygen
4) Copy cat id_rsa.pub to Upload SSH public key
5) Generate username + password for HTTPS credentials

Two ways for accessing repo:
1)git clone ssh://{{SSH key ID}}@git-codecommit.us-east-1.amazonaws.com/v1/repos/Test-codecommit

2)git clone via https and enter username (Provided by HTTPS GIT credentials)

Step 6: Add example files for repo

https://docs.aws.amazon.com/codepipeline/latest/userguide/samples/SampleApp_Linux.zip

Step 7:
![code_commit_step7](https://user-images.githubusercontent.com/50704452/112832390-89b80f00-9095-11eb-9901-d460ad982419.png)
![code_commit_step8](https://user-images.githubusercontent.com/50704452/112832557-c7b53300-9095-11eb-9491-1a61bfc84fd0.png)

Step 8: Push files to repo

> git add *;git commit -m "Added test files to repo";git push

Step 9 : Create a role

1) Select Trusted entity
2) Choose a use case
3) Add pemission 
> AmazonEC2RoleforAWSCodeDeploy
4) Add a name to role


To launch instance


![code_commit_step9](https://user-images.githubusercontent.com/50704452/112839014-fdf6b080-909d-11eb-89cc-972136588bd6.png)


###- Roles vs Policies


