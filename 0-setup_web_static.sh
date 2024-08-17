#!/usr/bin/env bash
# setup servers to deploy files


# Installs Nginx if it's not already installed
dpkg -l | grep nginx > /dev/null 2>&1 || (sudo apt -y update && sudo apt -y upgrade && sudo apt -y install nginx)

#Creates dir if doesn't exist
ls /data/web_static/releases/test/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/releases/test/
ls /data/web_static/shared/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/shared/

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/


# insert content if Line 22 is empty
if [ -z "$(sed -n '22p' /etc/nginx/sites-available/default | grep -v '^$')" ]; then
    sudo sed -i '22i \
\tlocation /hbnb_static {\n\
\t\talias /data/web_static/current/;\n\
\t}' /etc/nginx/sites-available/default
fi


sudo service nginx restart
