#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static."""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ['54.236.54.151	', '34.229.189.161']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_name = os.path.basename(archive_path)
        folder_name = archive_name.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(folder_name)
        
        run("rm -rf {}".format(release_path))
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
