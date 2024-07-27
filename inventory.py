#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a dynamic inventory for this ansible playbook
"""
import socket
import sys
import json

INIT_HOST=False

# create a dict to match hostnames to enviroments
env_dict = {
  'work':
    [],
  'private':
    ['derpy.local', 'applejack.local', 'rarity.local', 'discord.local']
}

def fqdn():
    """
    return fully qualified domain name
    """
    hostname = socket.gethostname()
    if '.' not in hostname:
        hostname = f"{hostname}.local"
    return str(hostname)

def become_pass(host, group):
    """
    return variable for become password using gopass lookup
    """
    if group == 'work':
        gopasslookupprefix = 'private/ansible/hosts/'
    else:
        gopasslookupprefix = 'ansible/hosts/'
    passstring = str("\"ansible_become_pass\": \"{{ lookup('community.general.passwordstore', '"
      + gopasslookupprefix + host + "/users/root') }}\"")
    return passstring

def env(domain):
    """
    map a hostname to a space
    or print empty list if no one matched and exit
    """
    for key, values in env_dict.items():
        if domain in values:
            return key
    if INIT_HOST:
        return str('init')
    print(json.dumps(empty_host_list(domain), sort_keys=True, indent=2))
    sys.exit()

def empty_host_list(domain):
    """
    return empty host list
    """
    comment = f"No valid host found. Found '{domain}'. Return empty host list!"
    return json.loads('{"_meta": {"comment": "' + comment +
        '", "hostvars": {}}, "instances": {"hosts": []}}')

def hostvars(host, group):
    """
    set variables to local connection
    """
    local = str('"' + host + '": {"ansible_connection": "local"')
    if not INIT_HOST:
        local += str(', ' + str(become_pass(host, group)))
    local += str('}')
    return local

def formated_host_group_list(host, group):
    """
    build inventory and return it
    """
    # pylint: disable=line-too-long
    return json.loads('{"_meta": {"hostvars": {' + str(hostvars(host, group)) + '}},"' + str(group) + '": {"hosts": ["' + str(host) + '"]},"instances": {"children": ["' + str(group) + '"]}}')

def main():
    """
    main funktion
      will analyse on which host this script is started
      and will print the dynamic inventory to tell ansible
      which host_vars and group_vars should be used
    """
    host = fqdn()
    group = env(host)
    print(json.dumps(formated_host_group_list(host, group), sort_keys=True, indent=2))

main()
