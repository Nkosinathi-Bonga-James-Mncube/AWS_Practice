# Automate setup Jenkins container in ec2
# Pre-requiresite
 - ec2 IP address as `HOST_IP`
 - ec2 pem key as `SSH_KEY`
# Installation
1. Setup up an ec2 instance with ssh key
2. Run ansible playbook 
```
ansible-playbook -i host playbook
```
3. To get Jenkins container password, ssh into ec2 and enter into cmd:
```
sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
4. To access jenkins url in ec2 ,copy AWS Public IPv4 DNS+port:
```
e.g  ec2-X-XX-XX-XXX.compute-1.amazonaws.com:8080
```