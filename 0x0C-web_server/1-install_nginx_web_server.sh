#!/bin/bash
# Update
sudo apt-get update -y
sudo apt-get install nginx -y

# HTML
sudo mkdir -p /var/www/html
echo "<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    Hello World!
  </body>
</html>" | sudo tee /var/www/html/index.html

# Nginx configuration
sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup

# new Nginx configuration
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Nginx configuration
sudo service nginx reload

# nginx restarting
sudo update-rc.d nginx defaults

# Print status
sudo service nginx status
