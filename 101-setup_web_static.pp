#  5. Puppet for setup 
exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo mkdir -p /data/web_static/releases/test/;
  sudo mkdir -p /data/web_static/shared/;
  echo "<html>
    <head>
    </head>
    <body>
	    Holberton School
    </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html;
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
  sudo chown -hR ubuntu:ubuntu /data;
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
  }" | sudo tee /etc/nginx/sites-available/default;
  sudo ln -sf "/etc/nginx/sites-available/default" "/etc/nginx/sites-enabled/default";
  service nginx restart;',
  provider => shell,
}

