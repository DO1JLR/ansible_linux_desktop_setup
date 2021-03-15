 Ansible Linux Desktop Setup
==========================
This ansible playbook collection creates [L3D](https://chaos.social/@l3d)s Desktop enviroment. Including window manager and some pre-installed programms like [Firefox](https://www.mozilla.org/de/firefox/new/) and some usefull shell programms.

 ATTENTION
-------------
Different to my other ansible playbooks:

### THIS PLAYBOOK HAS TO BE EXECUTET AT THE TARGET HOST DIRECTLY!

*It requires some GUI stuff and I did not find the time to forward X or wayland correctly to make it remotely working. Sorry. Feel free to create a Issue or pull-request*

  Install tipps:
-----------------------
```bash
# Clone Git
git clone --recursive https://github.com/DO1JLR/ansible_thinkpad_setup.git ansible_thinkpad_setup

# go into the folder
cd ansible_thinkpad_setup

# Download needed submodules
git submodule update --init --recursive

# make sure you always check out the submodules
git config --global submodule.recurse true
```

 Which playbook?
---------------
L3D use different playbook for different workstations.<br/>
Maybe he change this in the future... But now this is the current state.

To use this by yourself copy or change a existing playbook and modify the variables.

Or create a new git repo and be inspired by the roles L3D uses.


 Feedback
------------
If you find this usefull please take a few secounds and say thankyou to L3D.

He is at the most [chaos events](https://events.ccc.de), simple give him a Tschunk or Club Mate there!
