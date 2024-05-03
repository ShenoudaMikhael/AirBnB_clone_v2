#!/usr/bin/python3
"""web static deploy module """
import os
from datetime import datetime
import fabric.api as fab

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

    file_name = archive_path.split("/")[-1]
    file_name_dir = file_name.split(".")[0]
    tmp_dir = "/tmp/{}".format(file_name)
    extract_dir = "/data/web_static/releases/{}".format(file_name_dir)
    try:

        # put: versions/web_static_20170315003959.tgz ->
        # /tmp/web_static_20170315003959.tgz
        fab.put(archive_path, tmp_dir, use_sudo=True)
        # run: mkdir -p /data/web_static/releases/web_static_20170315003959/
        fab.sudo("mkdir -p {}".format(extract_dir))
        # run: tar -xzf /tmp/web_static_20170315003959.tgz -C
        #  /data/web_static/releases/web_static_20170315003959/
        fab.sudo("tar -xzf {} -C {}".format(tmp_dir, extract_dir))
        fab.sudo("rm {}".format(tmp_dir))
        d1 = "/data/web_static/releases/{}/web_static/*".format(file_name_dir)
        d2 = "/data/web_static/releases/{}/".format(file_name_dir)
        fab.sudo("mv {} {}".format(d1, d2))
        fab.sudo("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name_dir))
        l1 = "/data/web_static/releases/{}/".format(file_name_dir)
        lc = "/data/web_static/current"
        fab.sudo("rm -rf {}".format(lc))
        fab.sudo("ln -s {} {}".format(l1, lc))
        return True
    except Exception:
        return False


def deploy():
    """deploy function"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
