#!/usr/bin/python3
"""web static pack nodule"""
import os
from datetime import datetime
import fabric.api as fab

now = datetime.utcnow().strftime("%Y%m%d%H%M%S")


def do_pack():
    """do pack fabric functioin"""
    archive_name = f"web_static_{now}.tgz"
    versions_dir = "versions"
    if os.path.isfile(os.path.join(versions_dir, archive_name)):
        return os.path.join(versions_dir, archive_name)
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
