#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a dynamic inventory for this ansible playbook
"""
import socket
import sys

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
    sys.exit('{"group": { "hosts": ["example.com"], "vars": {} }, "_meta": { "foo": "bar" }}')


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
# {
#   "group":
#     { "hosts": ["127.0.0.1", "::1"], "vars": {}  },
#   "_meta":
#     { "hostvars": { "192.168.28.71": {  "host_specific_var": "bar" },
#       "192.168.28.72": {  "host_specific_var": "foo"   }}    }
# }

main()
