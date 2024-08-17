#!/usr/bin/python3
"""Pack and deploy static files."""
from fabric.api import local, put, run, env
from datetime import datetime
import os
env.hosts = ['34.203.38.10', '54.175.223.87']


def do_pack():
    """ make archive web_static folder """
    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local("mkdir -p versions")
    rar = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if rar is not None:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """ deploying an archive """
    if exists(archive_path) == False:
        return False
    file_name = archive_path.split('/')[-1]
    remove_extention = file_name.split('.')[0]
    remote_path = "/data/web_static/releases/"

    put(archive_path, "/tmp")
    run('mkdir -p {}{}/'.format(remote_path, remove_extention))
    run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, remote_path, remove_extention))

    # Clean Up
    run('rm /tmp/{}'.format(file_name))
    run('mv {0}{1}/web_static/* {0}{1}/'.format(remote_path, remove_extention))
    run('rm -rf {}{}/web_static'.format(remote_path, remove_extention))
    run('rm -rf /data/web_static/current')
    run('ln -s {}{}/ /data/web_static/current'.format(remote_path, remove_extention))
    return True


def deploy():
    """Creates and distributes an archive to the web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
