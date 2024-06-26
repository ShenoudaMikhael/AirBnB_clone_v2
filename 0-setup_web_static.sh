#!/usr/bin/env bash
#  0. Prepare your web servers

sudo apt update
sudo apt install -y nginx

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
echo "<html>
  <head>
  </head>
  <body>
	Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -hR ubuntu:ubuntu /data

echo "server {

	listen 80 default_server;
	listen [::]:80 default_server;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	add_header X-Served-By \$hostname;



	error_page 404 /404.html;
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://thedreamcatcher.dev permanent;
	}
	location = /404.html {
		root /usr/share/nginx/html;
		internal;
	}
	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}	
}" | sudo tee /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
sudo service nginx restart
