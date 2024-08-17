#!/usr/bin/python3
"""Distributes an archive to web servers using fabric"""

from fabric.api import *
from os.path import exists
from os import path, makedirs
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['18.206.198.128', '107.23.109.180']


def do_pack():
    """generate a .tgz archive from the contents of the web_static folder"""
    if not path.exists("versions"):
        makedirs("versions")

    creation_time = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_archive_name = "web_static_{}.tgz".format(creation_time)
    tgz_archive_path = path.join("versions", tgz_archive_name)
    make_tgz = local("tar -cvzf {} web_static".format(tgz_archive_path))

    if make_tgz.succeeded:
        return (tgz_archive_path)
    else:
        return (None)


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if exists(archive_path) is False:
        return False

    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except Exception:
        return False
