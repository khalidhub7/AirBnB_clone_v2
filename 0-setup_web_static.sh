#!/usr/bin/env bash
# set up servers to deploy files


# Installs Nginx if it's not already installed
dpkg -l | grep nginx > /dev/null 2>&1 || (sudo apt -y update && sudo apt -y upgrade && sudo apt -y install nginx)

#Creates dir if doesn't exist
ls /data/web_static/releases/test/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/releases/test/
ls /data/web_static/shared/ > /dev/null 2>&1 || sudo mkdir -p /data/web_static/shared/


sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '26i \
    location /hbnb_static {\n\
        alias /data/web_static/current/;\n\
    }' /etc/nginx/sites-available/default


sudo service nginx restart
