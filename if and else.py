#!/usr/bin/env python
# coding: utf-8

# Первое задание

# In[20]:


a = int(input('Введите 1 целое число '))
b = int(input('Введите 2 целое число '))
c = int(input('Введите 3 целое число '))


# In[71]:


d = 1
d = a and b and c and "Нет нулевых значений!!!"
d


# Второе задание

# In[72]:


d = 1
d = a or b or c or "Введены все нули!"
d


# Третье и четвертое задания

# In[12]:


if (a > b + c ):
    f = a - b - c
    print(f)
    
else:
    f = b + c - a
    print(f)


# Пятое и шестое задания

# In[21]:


if (a > 50 and (b > a or c > a)):
    print('Вася ')
elif (a > 5 or (b == 7 and c == 7)):
    print('Петя')
else:
    print('')
    


# In[ ]:




