#!/bin/bash
set -e

# Update package lists and install Nginx
sudo apt update -y
sudo apt install -y nginx

# Create necessary directories and files
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Hello, KHaleed!</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories
sudo chown -R ubuntu:ubuntu /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/web_static/shared/

# Update Nginx configuration
sudo tee -a /etc/nginx/sites-available/default <<EOF
    location /hbnb_static {
        alias /data/web_static/current/;
    }
EOF

# Restart Nginx service
sudo systemctl restart nginx
