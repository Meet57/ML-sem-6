import os
from datetime import date


os.system('git add .')

st = input("Commit name : ")

if st=='':
    st = str(date.today())

s = 'git commit -m ' + st

os.system(s)

os.system('git push')