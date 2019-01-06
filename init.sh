sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn.conf
sudo /etc/init.d/nginx restart
#gunicorn -b 0.0.0.0:8080 hello:app &
#sudo gunicorn -b 0.0.0.0:8000 -c /home/box/web/etc/gunicorn.conf ask.wsgi:application &
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
