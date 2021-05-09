import matplotlib.pyplot as plt

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.weather.go.kr/w/typhoon/typ-stat.do')
soup = BeautifulSoup(html, 'lxml')

namelist=soup.find_all('tr',{'class':'whole static'})
count=0
for i in namelist:
    count=count+1
    if count>1:
        print(i.get_text())
        a=i.get_text().split()

a.remove(a[0])
d=[]
for k in a:
    k=k.split("(")
    if len(k)>=2:
        k.remove(k[-1])
    r=float(k[0])
    d.append(r)
d.remove(d[-1])
print(d)

x=[1,2,3,4,5,6,7,8,9,10,11,12]
month=["January","February", "March","April","May", "June", "July", "August","September","October",'November',"December" ]
plt.bar(x,d,label='me',color='g')
plt.ylabel('count')
plt.xlabel('month')
plt.xticks(x,month,rotation='vertical')
plt.suptitle('Average frequency of typhoons per month over 10 years')

plt.show()
