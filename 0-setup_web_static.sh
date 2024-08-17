#!/usr/bin/env bash
# setup servers to deploy files


# install Nginx if not installed
dpkg -l | grep nginx > /dev/null 2>&1 || (sudo apt -y update && sudo apt -y upgrade && sudo apt -y install nginx)

# Creates dir if doesn't exist
ls /data/web_static/releases/test/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/releases/test/
ls /data/web_static/shared/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/shared/


echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "23i\\
\tlocation /hbnb_static {\\
\n\t\talias /data/web_static/current/;\\
\n\t}" /etc/nginx/sites-available/default


sudo service nginx restart