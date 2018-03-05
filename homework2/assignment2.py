
# coding: utf-8

# In[1]:


import requests
import bs4
import csv


# In[2]:


from bs4 import BeautifulSoup


# In[ ]:





# In[3]:


urls = []
for i in range(0,10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    urls.append(url)
        


# In[4]:


urls


# In[5]:


data = []
for url in urls:
    r=requests.get(url)
    mypage=BeautifulSoup(r.text)
    mylis = mypage.find('ol', attrs={'class': 'grid_view'}).find_all('li')

    for li in mylis:
        myspans = li.find('div', attrs={'class': 'hd'}).find_all('span')
        cn_name = myspans[0].text
        rating_num = li.find('span', attrs={'class': 'rating_num'})
        rating_num.text
        rating = li.find('div', attrs={'class': 'star'}).find_all('span')[3].text[:-3]
        data.append([cn_name, rating,rating_num.text])


# In[6]:


data


# In[7]:


with open('data.csv','w') as f:
    writer = csv.writer(f)
    header = ['title','number of comments''rating']
    writer.writerow(header)
    
    writer.writerows(data)

