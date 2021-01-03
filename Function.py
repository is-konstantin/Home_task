#!/usr/bin/env python
# coding: utf-8

# In[64]:


import functools

def log_in(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
         if args:
            return func(*args, **kwargs)
         else:
            print('Please log in first.', 'error')
    return wrapper_decorator
    


# In[39]:


def print_hello():
    print('Hello !!!')
    


# In[40]:


def print_goodbye():
    print('Goodbye !!!')


# In[65]:


import requests

@log_in
def weather(login, password):
    url = 'http://wttr.in/Moscow?0T'
    response = requests.get(url)  
    print(response.text) 
    


# In[42]:


print(' Приветсвую!!! \n Имеются следующие функции, которые можно выбрать: \n 1) Поприветсвует вас \n 2) Попрощается с вами \n 3) Скажет вам погоду, если вы авторизуетесь')

answer = int(input(" Выберите интересующую вас функцию для продолжения, путем ввода ее номера "))


# In[68]:


if answer == 1 :
    print_hello()
elif answer == 2 :
    print_goodbye()
else:
    login = input('Введите свой логин ')
    passw = input('Введите свой пароль ')
    if (login == '' or login == ' ') and (passw == '' or passw == ' '):
        weather()
    else:
        weather(login, passw)
    


# In[ ]:





# In[ ]:





# In[ ]:




