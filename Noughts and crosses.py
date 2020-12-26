#!/usr/bin/env python
# coding: utf-8

# In[ ]:


one_more_try = False

while not one_more_try: # прописываем цикл для повторной игры
    field = list(range(1, 10))
    count = 0
    win = False

    while not win:    # создаем цикл для самой игры в крестики и нолики
        print("--" * 6)
        for i in range(3): # создаем игровое поле
            print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
            print("--" * 6)
        
        if count % 2 == 0 : # делаем проверку: чей сейчас ход
            val = False
            while not val: # Ход делает игрок, рисующий крестик
                answer = input("Куда поставим " + "X" +"? ")
                # Делаю проверку на корректность ввода символа пользователем
                try: 
                    answer = int(answer)
                except:
                    print("Некорректный ввод. Вы уверены, что ввели число?")
                    continue
                    
                # Делаю проверку: в верном ли диапазоне введено и не занято ли эта цифра
                if answer >= 1 and answer <= 9:
                    if(str(field[answer-1]) not in "XO"):
                        field[answer-1] = "X"
                        val = True
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
            else:
                val = False
        elif count % 2 != 0:
            val = False
            while not val:  # Ход делает игрок, рисующий нолик
                answer = input("Куда поставим " + "O" +"? ")
                # Делаю проверку на корректность ввода символа пользователем
                try:
                    answer = int(answer)
                except:
                    print("Некорректный ввод. Вы уверены, что ввели число?")
                    continue
                    
                # Делаю проверку: в верном ли диапазоне введено и не занято ли эта цифра
                if answer >= 1 and answer <= 9:
                    if(str(field[answer-1]) not in "XO"):
                        field[answer-1] = "O"
                        val = True
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
        count += 1
        # Делаю проверку на выигрышь, после того как было сделано более 3 ходов
        if count >= 3 :
            win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
            for each in win_combination:
                if field[each[0]] == field[each[1]] == field[each[2]]:
                    w = field[each[0]]
                else:
                    w = False
                if w :
                    print(w, " победил")
                    win = True
                    break
                
        if count == 9 : # Делаю проверку на ничью, поскольку за 9 ходов должно быть заполнено все игровое поле 
            print("Ничья")
            break
        
    print("--" * 6)
    for i in range(3): 
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("--" * 6)
    
    # Спрашиваю пользователей, будут они играть снова или нет 
    s = input("Для выхода следует нажать кнопку Enter, а для повтора поставить пробел или иной символ ") 
    if bool(s) == False :
        one_more_try = True
        break
    else:
        one_more_try = False
        
            
            


# In[ ]:





# In[ ]:




