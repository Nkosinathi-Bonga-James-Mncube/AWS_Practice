# Ansible vault


# What is Ansible-Vault?
- Allows you to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in playbooks or roles

# Commands
- Encryt file

```cmd
    ansible-vault encryt credentials.yml
```
- Decrypt file
```cmd
    ansible-valut decrypt credentials.yml
```
 - View encrypt file (Prompt for password)

 ```cmd
    ansible-vault view credentials.yml
 ```
 - Run ansible vault inside playbook (Prompt for password)
 ```cmd
    ansible-playbook main.yml --ask-vault-password
 ```