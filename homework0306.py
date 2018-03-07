
# coding: utf-8

# In[3]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1=response.text


# In[7]:


len(book1)


# In[10]:


pure_text = book1.replace('<HTML><HEAD>','')


# In[12]:


book1.find('胡一刀')

