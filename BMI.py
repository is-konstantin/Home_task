#!/usr/bin/env python
# coding: utf-8

# In[21]:


weight = float(input("Введите свой вес в кг "))


# In[7]:


growth = float(input("Введите свой рост в метрах "))


# In[ ]:





# In[22]:


index_BMI = round(weight / growth ** 2)

print("Ваш индекс BMI = ", index_BMI)


# На данном шаге расчитываем индекс BMI для пользователя

# In[30]:


gap_1 = index_BMI - 10
scale = '10' + "=" * (gap_1 - 1) + '|' + "=" *(40 - gap_1) + "50"


# In[33]:


print("Шкала : \n", scale)


# In[ ]:




