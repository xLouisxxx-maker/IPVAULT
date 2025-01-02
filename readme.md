# IPVault
### Patent Database for Small- and Medium-sized IP-Firms
---
IPVault is a solution designed for small and medium-sized intellectual property firms. It offers an efficient way to store and manage patents, deadlines, etc.. 
Integration of OPS (Open Patent Service) API provided by the EPA. 

## Main Features
- **Patent Management**  
  Store and retrieve patents and  there filing dates, descriptions, and legal statuses.  
- **Deadline Tracking**  
  Keep track of important deadlines like renewal dates, opposition deadlines, etc. 
- **EPO API Integration**
 Pull Patentdata automatically from OPS API.
- **Visual Graph implementation of Portfolio**
---
---
### Windows virtual environments python aufsetzten/ django git
https://docs.python.org/3/library/venv.html
im Verzeichnis, python 3 muss installiert sein
cmd
$python3 --version
$mkdir ordnername

 
#### in visual studio im korrekten verzeichnis
$python3 -m venv .venv (create venv)
#### Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
$. .venv/Scripts/activate   <---diesem Command um in Virtual environment zu arbeiten
$pip install django (install django packages onyl once)
$pip freeze  (test, return all additional packages)
 
#### um virtual environment zu verlassen
$deactivate
$pip3 freeze (alle global installierten Packages, auserhalb des venv)
 
 
#### mit django arbeiten (https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
$python --version (diffrent outside venv)
$django-admin --help <-- liste von commands
$django-admin startproject IPVault (new directory)
 
 
---> jetzt source controll
$git --version
$git init <--- neues git repo
neues .gitignore file mit folgendem inhalt, damit nur essentielle files auf git landen
https://www.toptal.com/developers/gitignore/api/django
$git add .
$git status
$git commit -m "inital commit"
$venv <— Creation of virtual environments
Source code: Lib/venv/ The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual 
$en...
 
---
#### migrate database
$python manage.py makemigrations
$python manage.py migrate
#### create superuser in IPVault
$python manage.py createsuperuser
#### run locally
 §python manage.py runserver


Login Superuser

username: "admin"
psw: "admin"