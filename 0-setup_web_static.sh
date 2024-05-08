#!/usr/bin/env bash
set -e

sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p data/web_static/shared/
sudo touch data/web_static/releases/test/index.html

sudo echo -e '<!DOCTYPE html>\n<html>\n<body>\n    <h1>Hello, KHaleed!</h1>\n</body>\n</html>' > data/web_static/releases/test/index.html

# Remove the symbolic link if it exists
rm -f /data/web_static/current
# Create a new symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu data/

sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
