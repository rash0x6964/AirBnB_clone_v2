#!/usr/bin/python3
"""Creates and distributes an archive to your web servers."""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from datetime import datetime


env.hosts = ['54.236.54.151	', '34.229.189.161']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_name = os.path.basename(archive_path)
        folder_name = archive_name.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(folder_name)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_path))

        run('rm /tmp/{}'.format(archive_name))

        run('mv {}web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}web_static'.format(release_path))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_path))

        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
