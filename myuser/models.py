from django.db import models
import json
import re
# Create your models here.

path="user.json"
pics=[
         'f2',
         'f3',
         'f4',
         'f5',
         'f6',
         'f7',
     ]

#========================================================================
def load_users(path):
    fh=open(path,'rt')
    users = json.loads(fh.read())
    fh.close()
    return users

#========================================================================
def dump_users(path,users):
    fh=open(path,'wt')
    fh.write(json.dumps(users))
    fh.close()

#========================================================================
def validate_login(name,password):
   users=load_users(path)
   for user in users.values():
      if user['name'] == name and user['password'] == password:
         return True
   return False

#========================================================================
def validate_register(name,email,password,password2):
   users=load_users(path)
   names=users.keys()
   if name in names:
      return False, 'user already exists'
   if len(name) < 0 or len(name) > 8:
      return False,'length of user name should be between 0 and 8'
   if not re.match(r"[\w.]+\@[\w]+\.[\w]+", email):
      return False,'Please input valid email address'
   if password != password2:
      return False,'Please confirm password'
   users[name]={'name':name,'email':email,'password': password, 'password2': password2}
   dump_users(path, users)
   return True,''
#========================================================================



