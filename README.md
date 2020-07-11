# Suary
Photo sharing web app written in Django 3.0 and React

# Requirements
<ol>
<li>Django 3.0 (Python 3.7+) see requirements.txt for dependinces
<li>Nodejs 12.18.2 with npm see `/frontend/package.json` for dependinces</li>
<li>Postgres 12.3</li>
<li>Mongodb 4.2</li>
</ol>

# How to run project 
<h5>(assuming you have all the above installed)</h5>
<ol>
<li>pip install -r requirements.txt</li>
<li>npm install</li>
<li>Set DEFAULT_DATABASE_URL in .env to postgres Database</li>
<li>Set MEDIA_DATABASE_URL in .env to same or other mongo database</li>
<li>npm run dev (to build frontend)</li>
<li>python manage.py runserver 0.0.0.0:80</li>
<li>Done!</li>
</ol>
