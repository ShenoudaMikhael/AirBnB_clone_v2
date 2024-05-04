#!/usr/bin/python3
"""web static deploy module """
import os
from datetime import datetime
import fabric.api as fab
import shlex

fab.env.hosts = ["34.201.165.130", "34.224.62.173"]


def do_pack():
    """do pack fabric functioin"""
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{now}.tgz"
    versions_dir = "versions"
    if not os.path.exists(versions_dir):
        fab.local(f"mkdir {versions_dir}")
    try:

        fab.local(
            "tar -czvf {} web_static/".format(
                os.path.join(versions_dir, archive_name))
        )
        return os.path.join(versions_dir, archive_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """web static deploy"""
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        fab.put(archive_path, "/tmp/")
        fab.sudo("mkdir -p {}".format(releases_path))
        fab.sudo("tar -xzf {} -C {}".format(tmp_path, releases_path))
        fab.sudo("rm {}".format(tmp_path))
        fab.sudo("mv {}web_static/* {}".format(releases_path, releases_path))
        fab.sudo("rm -rf {}web_static".format(releases_path))
        fab.sudo("rm -rf /data/web_static/current")
        fab.sudo("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
