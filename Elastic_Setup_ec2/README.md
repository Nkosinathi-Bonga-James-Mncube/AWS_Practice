# Setting Opendistro and Elastic on AWS EC2 instance

 - Created a ansible playbook to setup Elastricsearch, Opendistro and Kibana on AWS EC2 instance
 - Created a inventory file with ec2 ip address with location of ssh RSA key(.pem)

## Prerequisite
 - Create inventory file with ip-address and location of ssh RSA key(.pem)

# How it works
The following task are executed in playbook:

**1.Installation of packages**
 1. Docker
 2. Docker-compose

**2.Start Docker and Enable docker**
- Enable docker at kernal level with systemctl

**3.Copy Docker-compose file to EC2**
- Copy docker-compose file to system being able to run it

**4.Pull docker images** 
1. Opendistro For Elasticsearch
2. Kibana

**5.Increase Virtual Memory for Elastic Search**
-  More info : https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

**6.Lauch docker compose**

# Installation
1. Install pipenv
2. Clone repo
3. Create pipenv
```
pipenv --three
```

4. Activte virtual environment
```
pipenv shell
```
5. Install packages
```
pip install -r requirements.txt
```
6. Run VPN (optinal)
7. SSH into EC2 instance:

```
sudo ssh -i intern.pem ec2-user@{{IP_ADDRESS}}
```
8.  Run Ansible playbook with command: 

```
ansible-playbook playbook.yml -i inventory
```
# Commands

- To view master and data nodes(both on local and external network)
```
curl -XGET https://{{IP_ADDRESS}}:9200/_cat/nodes?v -u 'admin:admin' --insecure

```

- To check elasticsearch logs for ec2 instance

```
sudo /usr/local/bin/docker-compose logs -f
```
- To stop docker compose on ec2 instance(after ssh into it)
```
sudo /usr/local/bin/docker-compose down -v
```
