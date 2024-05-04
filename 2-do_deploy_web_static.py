#!/usr/bin/python3
"""web static deploy module """
import os
from datetime import datetime
from fabric.api import env, sudo, local, put

env.hosts = ["34.201.165.130", "34.224.62.173"]
now = datetime.utcnow().strftime("%Y%m%d%H%M%S")


def do_pack():
    """do pack fabric functioin"""

    archive_name = f"web_static_{now}.tgz"
    versions_dir = "versions"
    if os.path.isfile(os.path.join(versions_dir, archive_name)):
        return os.path.join(versions_dir, archive_name)
    if not os.path.exists(versions_dir):
        local(f"mkdir {versions_dir}")
    try:

        local(
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
    if not os.path.isfile(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    file_name_dir = file_name.split(".")[0]
    tmp_dir = "/tmp/{}".format(file_name)
    extract_dir = "/data/web_static/releases/{}".format(file_name_dir)
    try:

        # put: versions/web_static_20170315003959.tgz ->
        # /tmp/web_static_20170315003959.tgz
        put(archive_path, tmp_dir, use_sudo=True)
        # run: mkdir -p /data/web_static/releases/web_static_20170315003959/
        sudo("mkdir -p {}".format(extract_dir))
        # run: tar -xzf /tmp/web_static_20170315003959.tgz -C
        #  /data/web_static/releases/web_static_20170315003959/
        sudo("tar -xzf {} -C {}".format(tmp_dir, extract_dir))
        sudo("rm {}".format(tmp_dir))
        d1 = "/data/web_static/releases/{}/web_static/*".format(file_name_dir)
        d2 = "/data/web_static/releases/{}/".format(file_name_dir)
        sudo("mv {} {}".format(d1, d2))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name_dir))
        l1 = "/data/web_static/releases/{}/".format(file_name_dir)
        lc = "/data/web_static/current"
        sudo("rm -rf {}".format(lc))
        sudo("ln -s {} {}".format(l1, lc))
        print("New version deployed!")
        return True
    except Exception:
        return False
