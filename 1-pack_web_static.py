#!/usr/bin/python3
""" fabric file that generate tgz archive """
from datetime import datetime
from fabric.api import local


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
