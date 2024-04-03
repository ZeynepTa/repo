import os 
from random import randint

for i in range(1, 370):
    d = str(i) + ' days ago'

    for j in range(0,randint(0,3)):
        with open('file.txt','a') as file: 
            file.write(d + '\n')
        os.system('git add .')
        os.system('git commit --date="'+ d + '" -m "commit "')

os.system('git push -u origin main')