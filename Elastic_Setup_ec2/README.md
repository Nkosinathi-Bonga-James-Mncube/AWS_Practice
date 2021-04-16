# Setting Opendistro and Elastic on AWS EC2 instance

 - Created a ansible playbook to setup Elastricsearch, Opendistro and Kibana on AWS EC2 instance
 - Created a inventory file with ec2 ip address with location of ssh key

## Prerequisite
 - Create inventory file with ip-address and location of ssh key
 - Add .pem file to ssh into EC2 instance

# How it works
The following task are executed in playbook:

**1.Installation of packages**
 1. Docker
 2. Docker-compose

**2.Start Docker and Enable docker**
- Enable docke at kernal level with systemctl

**3.Copy Docker-compose file to EC2**
- Copy docker-compose file to system being able to run it

**4.Pull docker images** 
1. Opendistro For Elasticsearch
2. Kibana

**5.Increase Virtual Memory for Elastic Search**
-  More info : https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

**6.Lauch docker compose**

# Installation
1) Run VPN
2) ssh into EC2 instance:

```
sudo ssh -i intern.pem ec2-user@{{IP_ADDRESS}}
```
3) Run Ansible playbook with command: 

```
ansible-playbook playbook.yml -i inventory
```
