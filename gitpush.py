import os
from datetime import date


os.system('git add .')

s = 'git commit -m ' + str(date.today())

os.system(s)

os.system('git push')