 Ansible Thinkpad Setup
==========================
My Ansible Setup for my Lenovo Thinkpad.

 What is this playbook good for:
--------------------------------
 + Install common usefull base packages
 + Create dotfiles like .bashrc and .vimrc
 + Setup and configure I3WM as Window Manager

 Install instructions:
-----------------------
```bash
# Clone Git
git clone --recursive https://github.com/DO1JLR/ansible_thinkpad_setup.git ansible_thinkpad_setup
cd ansible_thinkpad_setup

# Download needed submodules
git submodule update --init --recursive
```
 
