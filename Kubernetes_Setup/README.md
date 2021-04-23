# Setup Kubernetes in ec2 CentOS 7 

- Created a Kubernetes cluster and assign ec2 instance as master node.

<details>
<summary>What is Kubernetes?</summary>

      -Kubernetes is used for orchestration automates the deployment, management, scaling, and networking of containers
      -Deploy same application accross different environment without redesign(create microservices)
      - Automate and manage tasks such as: 
        - Configuration
        - Scheduling
        - Scaling and removing containers
        - Secure interaction between containers

</details>

## Prerequisite
 - Add ssh RSA key(.pem) and modify `hosts` file

## How it works
The following playbooks are run in `create_kube.yml`:

 - `setup.yml`
 - `master-setup`

 ## Setup.yml

 **Install packages**
 - Docker
 - Kubernetes

 **Start docker service**
 **Set values for bridge.bridge-nf-call-ip6tables and iptables**
 -  Set configuration for node network using sysctl

 **Installing Kubernetes node components**
  - Kubelet
 <details>
 <summary>What is kubelet?</summary>
 <br>
 
    - Kubelet is the agent that runs on each node in the cluster.

    - Making sure each node is running expectedly. 

    - Communicates with master components to recieve commands to work.

    - Responsiblity include: run containers,network rules,port forwarding
</details>
  
  - Kubeadm

 <details>
 <summary>What is kubeadm?</summary>
 <br>

    - Kubeadm is a tool to create cluster by using commands "kubeadm init" and "kubeadm join"

 </details>


 
 - kubectl 
 <details>
 <summary>What is kubectl?</summary>

    - Kubectl command line interface to control Kubernetes cluster

 <br>
 </details>

 ## master.yml
 The following task are run:
 **Initialize the cluster**
 - Specify the private subnet with range 10.244.0.0/16
 
 **Create .kube directory**
 - Store configurations of admin keys to connect to cluster and cluster API address

**Copy admin.conf to user's kube config**
-   Copy `admin.conf` to home directory.This allows you to kubectl on access newly-created cluster.

**Install Pod network**
- Install fannel (Open sourced virtual network for Kubernetes)
- More details at : https://dzone.com/articles/configure-kubernetes-network-with-flannel



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
8. Replace `{{IP_Address}}` in `hosts` with ec2 instance IP addresss 
9. Run `create_kube.yml`
```
 ansible-playbook -i hosts create_kube.yml
```
10. To remove Kubernetes run:

```
 ansible-playbook -i hosts kube_playbooks/remove.yml
```
# Commands

## Kubernetes

- To view nodes (inside ec2 terminal)
```
Kubectl get nodes
```
## Reference
- https://kubernetes.io/docs/home/
- https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-cluster-using-kubeadm-on-centos-7


