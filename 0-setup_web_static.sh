#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

sudo echo "<html>
  <head>
  </head>
  <body>
    <p>Holberton School</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

sudo service nginx restart
