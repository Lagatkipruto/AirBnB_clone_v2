#!/usr/bin/env bash
# Install Nginx if its not already installed.
#+ Creates necessery directories if it does not exist
#++ Creates an html file and creates a symbolic link to test the folder.
#++ Give ownership to the data folder to ubuntu user and group.
#++ Update Nginx configuration and it restarts it.

if [ ! -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/{releases,test,shared}
sudo echo "Hello, World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's|^\tserver {|&\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
