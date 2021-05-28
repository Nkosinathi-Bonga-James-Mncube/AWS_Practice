# Deploy Kibana on Kubernetes Namespace cluster

- Created a Kubernetes master and deploy Kibana on namespace with kubeconfig details

# Terms

<details>
<summary>What is Kubernetes?</summary>

      -Kubernetes is used for orchestration automates the deployment, management, scaling, and networking of containers
      -Deploy same application accross different environment without redesign(create microservices)
      - Automate and manage tasks such as: 
        - Configuration
        - Scheduling
        - Scaling and removing containers
        - Secure interaction between containers
        
![0*RHsNYkGi10fU5XUv](https://user-images.githubusercontent.com/50704452/115887959-b6700400-a452-11eb-9c74-d3d3315bdb59.png)

</details>

<details>
<summary>What is kubeconfig?</summary>

    - A kubeconfig is a file used to configure access to Kubernetes using kubectl
    - More Details : 
                    https://ahmet.im/blog/mastering-kubeconfig/
                    https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
</details>

<details>
<summary>What is a Namespace?</summary>
        
        - Namespaces is a way to organize clusters into virtual sub-clusters
        - A number of Namespace can be supported in cluster, logically seperated and communicate with each other 
        - More Details: 
                        https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-to/namespace-scoped-objects
                        https://www.vmware.com/topics/glossary/content/kubernetes-namespace
</details>
<br>

# Pre-requisite
 - Add ssh RSA key(.pem) and modify `{{IP_ADDRESS}}` in `hosts` file
 - Requires `Namspace` and `kubeconfig`
 - Copy `kubeconfig` configuration folder into `kube_playbook`
 - Replace `{{kubeconfig_folder}}` with configuration folder name in `setup-kibana.yml`

## How it works
The following playbooks are run in `create_kube.yml`:

 - `setup.yml`
 - `master-setup`
 - `setup-kibana`

 # Setup.yml

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
 <br>

 # master-setup.yml
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

<br>

# setup-kibana.yml

 **state local connection**
 - Forcing to perform local tasks (e.g used for running playbook locally and deploy Kubernetes externally)
 - More details : http://willthames.github.io/2018/07/01/connection-local-vs-delegate_to-localhost.html

 **Adding ansible galaxy**
 - Package management

  **The following task are run:**
   - Deploy playbook to run Kinaba headless service and Deploy to namespace

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
9. Run `initial_setup.yml`
```
    ansible-playbook -i hosts initial_setup.yml
```
10. To remove Kubernetes run:

```
    ansible-playbook -i hosts kube_playbooks/remove.yml
```
# Commands

## Kubernetes

- To view nodes (inside ec2 terminal)
```
kubectl --kubeconfig={{kubeconfig_file}} --namespace={{namespace_cluster}} get nodes
```
- To delete deployment
```
kubectl --kubeconfig={{kubeconfig_file}} --namespace={{namespace_cluster}} delete deployment {{name_of_deployment}}
```
- To delete service
```
kubectl --kubeconfig={{kubeconfig_file}} --namespace={{namespace_cluster}} delete svc {{name_of_deployment}}
```
## Reference
- https://kubernetes.io/docs/home/
- https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-cluster-using-kubeadm-on-centos-7


