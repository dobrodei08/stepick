sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx reload
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &
