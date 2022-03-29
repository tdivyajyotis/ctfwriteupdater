print('''
CTFWriteUPdater alpha by Team_Dd05
Released on 26 March 2022
THIS IS ALPHA SOFTWARE FOR INTERNAL TESTING IN WEB DEVELOPMENT TEAM
NOT TO BE USED OUTSIDE OF A VIRTUALIZED ENVIRONMENT
INTERNET ACCESS NEEDED''')

from datetime import datetime
timedate = datetime.utcnow()
print(timedate)

import requests as r
commandserver = "http://tdivyajyotis.github.io/commandapi/alpha.json"
response = r.get(commandserver)
run = response.json()["run"]

import sys
if run == True:
  pass
  print("CoLab is $#!T!")
else:
  pass
  sys.exit('''GET NEW VERSION OF SCRIPT AT https://tdivyajyotis.github.io/ctfwriteupdater !
  DEPRECATED CODE EXITED''')

