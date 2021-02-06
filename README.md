# erp_project
here the way to clone <br>
Make sure you have added ssh keys
<Br>
Use following for help <br>
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
<Br><br>
```
git clone git@github.com:spriyanshu245/erp_project.git

```

if permission err then search how to add ssh key in github


make changes and save
```
git add . # . refer all files
git add <name> # single file / foldername
```
commit
```
git commit -m "usefull msg / changes "

```
push to github server
```

git push 


```
Dependencies Installations :
```
djnago == 3.0 and above
mysql server
django-filters

```
To get this project up and running locally on your computer:

Set up the Python development environment. We recommend using a Python virtual environment.
<br>
Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py test # Run the standard tests. These should all pass.
python3 manage.py createsuperuser # Create a superuser
python3 manage.py runserver
```
