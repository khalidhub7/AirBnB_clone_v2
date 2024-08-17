#!/usr/bin/python3
""" rar && deploy """
from fabric.api import local, put, run, env
from datetime import datetime
import os

# Update with your actual server IPs
env.hosts = ['34.203.38.10', '54.175.223.87']


def do_pack():
    """Creates a .tgz archive of the web_static folder"""
    if not os.path.isdir("versions"):
        local("mkdir versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    result = local(
        "tar -cvzf {} web_static".format(archive_path),
        capture=True)
    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.isfile(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        basename = filename.split(".")[0]

        # Upload the archive to the /tmp/ directory on the remote server
        put(archive_path, "/tmp/{}".format(filename))

        # Create the directory on the remote server
        run("mkdir -p /data/web_static/releases/{}/".format(basename))

        # Uncompress the archive to the directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, basename))

        # Remove the archive from the remote server
        run("rm /tmp/{}".format(filename))

        # Move the content of the archive to the correct directory
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(basename, basename))

        # Remove the now empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static".format(basename))

        # Remove the current symlink
        run("rm -rf /data/web_static/current")

        # Create a new symlink
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(basename))

        print("New version deployed!")
        return True
    except BaseException:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
