#!/usr/bin/python3
"""Generates a .tgz archive from the contents of web_static."""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path
