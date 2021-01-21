import os
from datetime import date


os.system('git add .')

st = input("Commit name : ")

if st=='':
    st = str(date.today())

status = input("Do you want to push to your Github ? \n yes : push | no : just commit : ")

s = 'git commit -m ' + st

os.system(s)

if(status=='yes'):
    os.system('git push')