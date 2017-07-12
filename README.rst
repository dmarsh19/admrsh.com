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


# pygments syntax highlighter
cloned socket_chat and cd to directory:
sudo apt install python-pygments
pygmentize -f html -O full,linenos=table -o socket_chat.html chat.pyw
sudo cp socket_chat.html /var/www/admrsh.com_project

sudo apt install npm
sudo npm install chart.js --save
node_modules/chart.js/dist/
  Chart.bundle.js (includes Moment.js)
  Chart.bundle.min.js
  Chart.js
  Chart.min.js


# template for pygmentize to break code into several tables
# **no extra space or breaks between pre**
    <table class="highlighttable"><tr>
      <td class="linenos"><div class="linenodiv"><pre><!-- linenos --></pre></div></td>
      <td class="code"><div class="highlight"><pre><!-- code spans ---></pre></div></td>
    </tr></table>


# database conversion
select datetime, replace(datetime, ' ', 'T') from dht limit 15;
update DHT set datetime=replace(datetime, ' ', 'T');
select datetime from dht limit 15;
select datetime || ':00.000' from dht limit 15;
update DHT set datetime=datetime || ':00.000';
select datetime from dht limit 15;
DROP TABLE dhttemp;
.tables
.schema DHT
REINDEX dht_datetime;
VACCUUM;
