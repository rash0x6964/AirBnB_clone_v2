#!/usr/bin/python3
"""Fabfile to delete out-of-date archives."""
import os
from fabric.api import *

env.hosts = ['54.236.54.151	', '34.229.189.161']


def do_clean(number=0):
    """Delete out-of-date archives."""

    number = int(number)
    if number < 1:
        number = 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
