#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


import time


# In[4]:


from selenium.webdriver.common.by import By


# In[5]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[6]:


driver.get('https://amazon.com/')
time.sleep(2)


# In[7]:


driver.find_element(By.ID,'nav-global-location-popover-link').click()
time.sleep(2)


# In[8]:


driver.find_element(By.ID,'GLUXZipUpdateInput').send_keys('10081')
time.sleep(2)


# In[9]:


driver.find_element(By.XPATH,"//*[@id ='GLUXZipInputSection']/div[2]/span/span/input").click()
time.sleep(2)


# In[10]:


driver.find_element(By.XPATH,"//*[@class='a-popover-footer']/span/span/input").click()
time.sleep(2)


# In[11]:


driver.find_element(By.ID,'twotabsearchtextbox').click()
time.sleep(2)


# In[12]:


driver.find_element(By.ID,'twotabsearchtextbox').send_keys('mobile phone')
time.sleep(2)


# In[13]:


driver.find_element(By.ID,'nav-search-submit-button').click()
time.sleep(2)


# In[14]:


org = driver.find_elements(By.XPATH,"""//div[@data-component-type="s-search-result"]""")
time.sleep(2)


# In[15]:


len(org)


# In[ ]:





# In[ ]:





# In[ ]:




