# follow deployment README in flask_uwsgi; after cd /var/www...
sudo git clone https://github.com/dmarsh19/admrsh.com.git admrsh.com_project
#cd admrsh.com_project
##sudo git checkout develop
#change server_name in admrsh.com.nginx
#add resume to server under admrsh/static/
#sudo nano settings.py
#  import os
#  basedir = os.path.abspath(os.path.dirname(__file__))
#  DEBUG = True
#  SECRET_KEY = 
#  SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/atmo.sqlite'.format(basedir)
#  SQLALCHEMY_ECHO = True
#cd ..
./admrsh.com_project/deploy.sh
#in browser, navigate to url




cloned socket_chat and cd to directory:
pygmentize -f html -O full,linenos=inline -o socket_chat.html chat.pyw
sudo cp socket_chat.html /var/www/admrsh.com_project

sudo apt install npm
sudo npm install chart.js --save
node_modules/chart.js/dist/
  Chart.bundle.js (includes Moment.js)
  Chart.bundle.min.js
  Chart.js
  Chart.min.js
