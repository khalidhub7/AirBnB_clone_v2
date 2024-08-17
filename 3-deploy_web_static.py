#!/usr/bin/python3
"""
Fabric script to pack and deploy an archive to web servers.
Execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

# Define the hosts (web servers)
env.hosts = ['34.203.38.10', '54.175.223.87']


def do_pack():
    """
    Packs the web_static folder into a .tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        archive_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploys the given archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        no_extension = file_name.split('.')[0]
        remote_path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f'mkdir -p {remote_path}{no_extension}/')
        run(f'tar -xzf /tmp/{file_name} -C {remote_path}{no_extension}/')

        # Clean up
        run(f'rm /tmp/{file_name}')
        run(f'mv {remote_path}{no_extension}/web_static/* {remote_path}{no_extension}/')
        run(f'rm -rf {remote_path}{no_extension}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {remote_path}{no_extension}/ /data/web_static/current')

        return True
    except Exception:
        return False


def deploy():
    """
    Creates an archive and deploys it to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
