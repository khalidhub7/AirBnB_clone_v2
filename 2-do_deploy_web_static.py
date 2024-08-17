#!/usr/bin/python3
""" fabric that distributes an archive to the web servers """
from fabric.api import put, run, env
from os.path import exists

env.hosts = ["34.203.38.10", "54.175.223.87"]


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
