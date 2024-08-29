 Ansible Linux Desktop Setup
==========================
This ansible playbook collection manages some of my workstations and laptops. Because of this it sometimes contains very specific variables like my username, SSH keys or similar data that may not be the best choice for your system.

Nevertheless, this ansible playbook is not only publicly available on the internet, but by the MIT license a part of free open-source ansible, which may serve you as inspiration within the framework of the MIT license.


 Inventory
-------------
This is my first ansible with dynamic inventory. The [inventory.py](inventory.py) script looks at which hostname it was lauched on. If the hostname is known, the host is mapped to the group stored for it and a local connection to the host is established.

This has the advantage that different environments are automatically recognized and significantly less danger of accidentally rolling out the ansible with the variables for a completely different host and thus configuring things that were not intended for this device.

Obviously, this also means that **this playbook must always be run on the host you want to manage** and this ansible playbook is not meant to be run remotely.


Install tipps:
-----------------------
```bash
# Clone Git
git clone --recursive https://github.com/DO1JLR/ansible_linux_desktop_setup.git ansible_linux_desktop_setup

# go into the cloned folder
cd ansible_linux_desktop_setup

# Download needed submodules
git submodule update --init --recursive

# make sure you always check out the submodules
git config --global submodule.recurse true

# Install Ansible in venv
python3 -m venv ansible

# Activate Venv
source ansible/bin/activate

# Install Ansible
pip3 install --upgrade ansible-core ansible-lint pylint
```

 Which playbook?
---------------
L3D use different playbook for different workstations.<br/>
Maybe he change this in the future... But now this is the current state.

To use this by yourself copy or change a existing playbook and modify the variables.

Or create a new git repo and be inspired by the roles L3D uses.


 Add a New Device
------------------
1. After you installed the OS and cloned this git repo with all sumodules, you have to change the inventory.py script.
* Make sure you changed the ``INIT_HOST`` boolean variable to just install gopass.
* After running the playbook create a gopass and set a few passwords
* Add new device to ``env_dict`` and restore the ``INIT_HOST``  value
* Run ansible

 Used Gopass Variables
-----------------------
For ``work`` devices:
```ini
private/ansible/hosts/<hostname>/users/
├── l3d/
│   ├── pwd
│   └── pwd_hash
├── lilian/
│   ├── pwd
│   └── pwd_hash
└── root
```

For ``private`` devices:
```ini
ansible/hosts/<hostname>/users/
├── l3d/
│   ├── pwd
│   └── pwd_hash
└── root
```

 Feedback
------------
If you find this usefull please take a few secounds and say thankyou to L3D.

He is at the most [chaos events](https://events.ccc.de), simple give him a Tschunk or Club Mate there!

 Additional Infos
------------------
By the way, to store sensible passwords, I am using the [community.general.passwordstore](https://docs.ansible.com/ansible/latest/collections/community/general/passwordstore_lookup.html) Lookup to access my passwords, stored in [gopass](https://gopass.pw/) Password Manager.
