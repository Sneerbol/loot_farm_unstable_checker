#https://loot.farm/unstable.html

import requests


print ('downloading with requests')
url = ('https://loot.farm/unstable.html')
r = requests.get(url)
with open('unstable.html', 'wb') as code:
    code.write(r.content)

    
name = input('Skin name :')

f=open('unstable.html','r',encoding='utf-8') #
n = 0
for s in f:
    i = s.find(name)
    if i > 0:
        n += 1

if n >= 1:
    print('н1з9 лити')
elif n == 0:
    print('можна лити')


    



f.close()
        

