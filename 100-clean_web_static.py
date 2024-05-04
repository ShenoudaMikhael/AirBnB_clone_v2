#!/usr/bin/python3
"""do clean module """
from fabric.api import env, sudo, local

env.hosts = ["34.201.165.130", "34.224.62.173"]


def do_clean(number=0):
    """do clean function"""

    num = int(number)

    num = 2 if num == 0 else num + 1
    
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(num))
    path = '/data/web_static/releases'
    sudo('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, num))
