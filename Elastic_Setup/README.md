# Anisible setup to install ElasticSearch , Opendistro and Kibana

- Create a ansible playbook to setup Elastricsearch, opendistro and Kibana on localhost using docker containers

# How it works
- Ansible playbook is run on localhost machine
- The following tasks are executed:

**1.Installation of packages**

 1. Docker
 2. Docker-compose

**2.Pull docker images** 
1. Opendistro
2. Kibana

**3.Configure sysctl**
<details>
<summary>What is sysctl?</summary>
<br>
    - A command used to modified default kernal behaviour. Changes can be on system reboot or at runtime.

    - The changes that will be made are increase virtual memory assigned by default to Elastic

    - More info : https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html
</details>
<br>
**4.Download Metricbeat deb package and installing**

<details>
<summary>What is Metricbeat?</summary>
<br>

 - A lightweight shipper you can install on yor server to periodically collects metric from the operating system and services on server.

 - Simplify collecting,parsing and visualizing infromation from key data sources (e.g. cloud platforms,containers). Based on Elastic Common Schema(ECS)

 - It then can take metrics and statistic to be used by Elasticsearch or Logstash
</details>
<br>

**5.Configure metricbeat.yml settings**
 - Replace the default metricbeat folder with custom metricbeat details

**6.Enable metricbeat modules**
 - Enable which module will be used by metricbeat having access to its metricsets (e.g for Docker CPU, containter,network etc.)

**7.Run the metricbeat setup command**
  - Initialize environment(e.g index template,ILM policies,Kibana dashboard etc.)

**8.Start metricbeat**
   - Start the shipper

- Finally ansible playbook is run and step-by-step each task is run on localhost

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
6. To run playbook run the command 
```
ansible-playbook playbook1.yml --ask-become-pass
```