#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a dynamic inventory for this ansible playbook
"""
import socket
import sys
import json

# create a dict to match hostnames to enviroments
env_dict = {
  'work':
    ['workstation.local'],
  'private':
    ['dderpy.local', 'foo.bar']
}

def fqdn():
    """
    return fully qualified domain name
    """
    return socket.getfqdn()

def env(domain):
    """
    map a hostname to a space
    """
    for key, values in env_dict.items():
        if domain in values:
            return key
    print(json.dumps(empty_host_list(), sort_keys=True, indent=2))
    sys.exit()

def empty_host_list():
    """
    return empty host list
    """
    comment = "No valid host found. returning empty host list!"
    return json.loads('{"_meta": {"comment": "' + comment +
        '", "hostvars": {}}, "instances": {"hosts": []}}')

def main():
    """
    main funktion
      will analyse on which host this script is started
      and will print the dynamic inventory to tell ansible
      which host_vars and group_vars should be used
    """
    host = fqdn()
    group = env(host)
    print(host + group)
#{
#    "_meta": {
#        "hostvars": { }
#    },
#
#    "instances": {
#        "hosts": ["10.66.70.33"]
#    }
# }

main()
