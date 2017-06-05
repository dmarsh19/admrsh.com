sudo touch admrsh.com_project/settings.py
sudo chown -R www-data:www-data /var/www/admrsh.com_project
# sticky bit to keep new files owned by www-data; 755
sudo chmod -R u=rwX,g=srX,o=rX /var/www/admrsh.com_project
sudo python3 -m pip install -r admrsh.com_project/requirements.txt
sudo mv admrsh.com_project/admrsh.com.service /etc/systemd/system
sudo service admrsh.com start
sudo mv admrsh.com_project/admrsh.com.nginx /etc/nginx/sites-available/admrsh.com
sudo ln -s /etc/nginx/sites-available/admrsh.com /etc/nginx/sites-enabled/admrsh.com
sudo rm /etc/nginx/sites-enabled/default
# test syntax errors
sudo nginx -t
sudo service nginx restart
