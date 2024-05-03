#!/usr/bin/python3
"""web static deploy module """
import os
import fabric.api as fab


def do_deploy(archive_path):
    """web static deploy"""
    # env.hosts = ["34.201.165.130", "34.224.62.173"]
    fab.env.hosts = "34.201.165.130"
    fab.env.user = "ubuntu"
    file_name = archive_path.split("/")[-1]
    file_name_dir = file_name.split(".")[0]
    tmp_dir = "/tmp/{}".format(file_name)
    extract_dir = "/data/web_static/releases/{}".format(file_name_dir)
    try:
        if not os.path.exists(archive_path):
            raise FileExistsError
        # put: versions/web_static_20170315003959.tgz ->
        # /tmp/web_static_20170315003959.tgz
        fab.put(archive_path, tmp_dir)
        # run: mkdir -p /data/web_static/releases/web_static_20170315003959/
        fab.run("mkdir -p {}".format(extract_dir))
        # run: tar -xzf /tmp/web_static_20170315003959.tgz -C
        #  /data/web_static/releases/web_static_20170315003959/
        fab.run("tar -xzf {} -C {}".format(tmp_dir, extract_dir))
        fab.run("rm {}".format(tmp_dir))
        d1 = "/data/web_static/releases/{}/web_static/*".format(file_name_dir)
        d2 = "/data/web_static/releases/{}/".format(file_name_dir)
        fab.run("mv {} {}".format(d1, d2))
        fab.run("rm -rf /data/web_static/releases/{}/web_static".format(file_name_dir))
        l1 = "/data/web_static/releases/{}/".format(file_name_dir)
        lc = "/data/web_static/current"
        fab.run("rm -rf {}".format(lc))
        fab.run("ln -s {} {}".format(l1, lc))
        return True
    except FileExistsError:
        return False
    except Exception:
        return False
