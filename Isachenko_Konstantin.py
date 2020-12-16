#!/usr/bin/env python
# coding: utf-8

# In[2]:


line = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'


# In[3]:


length = len(line)


# In[4]:


print('Шаг 1 - Количество символов в строке -', length)


# In[5]:


print('Шаг 2 - Развернутая строка - ', line[::-1])


# In[6]:


print('Шаг 3 - Все слова с большой буквы - ', line.title())


# In[7]:


print('Шаг 4 - Весь текст написан прописными буквами - ', line.upper())


# In[13]:


count1 = line.count('нд')


# In[14]:


count2 = line.count('ам')


# In[15]:


count3 = line.count('о')


# In[18]:


print('Шаг 5 : \n Число вхождений "нд" - ' +  str(count1) + '\n Число вхождений "ам" - ' + str(count2) + 
      '\n Число вхождений "о" - ' + str(count3))


# In[19]:


splitted_line = line.split('.')


# In[25]:


print('Шаг 6 - Разбиение предложения на несколько строк: \n')
for i in splitted_line:
    print(i)


# In[27]:


print('Шаг 7 - вывод исходной строки - \n', line)


# In[ ]:




