#!/usr/bin/python
import json
import sys


def load_users(path):
   fh=open(path,'rt')
   users = json.loads(fh.read())
   fh.close()
   return users


def dump_users(path,users):
   fh=open(path,'wt')
   fh.write(json.dumps(users))
   fh.close()



if __name__ == '__main__':
   if len(sys.argv) != 3:
      print "Wrong number of arguments"
      print "Usage: deleteuser.py username filename"
      sys.exit(1)
   name=sys.argv[1]
   jsonfile=sys.argv[2]
   users=load_users(jsonfile)
   users.pop(name,None)
   dump_users(jsonfile,users)
   #print "The following user(s) are(is) existing now after deleting user" 
   #for user in users:
   #   print user


