sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo gunicorn restart
#﻿sudo /etc/init.d/mysql start﻿
