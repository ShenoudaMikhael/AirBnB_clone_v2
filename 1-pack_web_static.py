#!/usr/bin/python3
"""web static pack nodule"""
from datetime import datetime
import fabric.api as fab


def do_pack():
    """do pack fabric functioin"""
    now = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    archive_name = f"web_static_{now}.tgz"
    fab.local(f"tar -czvf versions/{archive_name} web_static/")
    print(f"Archive created: {archive_name}")

    # with tarfile.open(output_filename, "w:gz") as tar:
    # tar.add(source_dir, arcname=os.path.basename(source_dir))
