#!/usr/bin/python3
"""do clean module """
from fabric.api import env, sudo, local

env.hosts = ["34.201.165.130", "34.224.62.173"]


def do_clean(number=0):
    """do clean function"""

    arch_count = int(number)

    if arch_count == 0 or arch_count == 1:
        arch_count = 1

    else:
        arch_count += 1
    local_dir = "cd versions/;"
    remote_dir = "cd /data/web_static/releases/;"
    comand = f"ls -t | tail -n +{arch_count} | xargs rm -rf"

    local("{} {}".format(local_dir, comand))
    sudo("{} {}".format(remote_dir, comand))
