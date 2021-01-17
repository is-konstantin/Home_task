import time
import sys

a = '\u2B1C'
b = '  '
ps = '\n'
zero = [(a*4), (a + b*2 + a), (a + b*2 + a), (a + b*2 + a), (a + b*2 + a), (a + b*2 + a), (a*4)]

one = [(b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a) ]

two = [(a*4), (b*3 + a), (b*3 + a), (a*4), (a + b*3), (a + b*3),  (a*4)]

three = [(a*4), (b*3 + a), (b*3 + a), (a*4), (b*3 + a), (b*3 + a),  (a*4)]

four = [(a + b*2 + a), (a + b*2 + a), (a + b*2 + a), (a*4), (b*3 + a), (b*3 + a), (b*3 + a)]

five = [(a*4), (a + b*3), (a + b*3), (a*4), (b*3 + a), (b*3 + a),  (a*4)]

six = [(a*4), (a + b*3), (a + b*3), (a*4), (a + b*2 + a), (a + b*2 + a),  (a*4)]

seven = [(a*4), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a), (b*3 + a) ]

eight = [(a*4), (a + b*2 + a), (a + b*2 + a), (a*4), (a + b*2 + a), (a + b*2 + a), (a*4)]

nine = [(a*4), (a + b*2 + a), (a + b*2 + a), (a*4), (b*3 + a), (b*3 + a), (a*4)]



change = 1

while True:
    from datetime import datetime
    import os
    now = datetime.now()
    numbers_dict = {'0' : zero, '1' : one, '2' : two, '3' : three, '4' : four, '5' : five, '6' : six, '7' : seven, 
                '8' : eight, '9' : nine}

    if change % 2 != 0:
        a = '\u2B1C'
    elif change % 2 == 0:
        a = '  '
    
    hour = str(now.hour)
    minutes = str(now.minute)
    seconds = str(now.second)

    if len(hour) == 1 and len(minutes) == 1 and len(seconds) == 1 :
        print(zero[0] + "   " + numbers_dict[hour][0] + "   " + "   " + zero[0] + "   " + numbers_dict[minutes][0] + "   " + "   " + zero[0] + "   " + numbers_dict[seconds][0])
        print(zero[1] + "   " + numbers_dict[hour][1] + "   " + "   " + zero[1] + "   " + numbers_dict[minutes][1] + "   " + "   " + zero[1] + "   " + numbers_dict[seconds][1])
        print(zero[2] + "   " + numbers_dict[hour][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[minutes][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[seconds][2])
        print(zero[3] + "   " + numbers_dict[hour][3] + "   " + "   " + zero[3] + "   " + numbers_dict[minutes][3] + "   " + "   " + zero[3] + "   " + numbers_dict[seconds][3])
        print(zero[4] + "   " + numbers_dict[hour][4] + "   " + "   " + zero[4] + "   " + numbers_dict[minutes][4] + "   " + "   " + zero[4] + "   " + numbers_dict[seconds][4])
        print(zero[5] + "   " + numbers_dict[hour][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[minutes][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[seconds][5])
        print(zero[6] + "   " + numbers_dict[hour][6] + "   " + "   " + zero[6] + "   " + numbers_dict[minutes][6] + "   " + "   " + zero[6] + "   " + numbers_dict[seconds][6])
    
    
    elif len(hour) == 2 and len(minutes) == 1 and len(seconds) == 1 :
        h = list(hour)
        print(numbers_dict[h[0]][0] + "   " + numbers_dict[h[1]][0] + "   " + "   " + zero[0] + "   " + "   " + numbers_dict[minutes][0] + "   " + "   " + zero[0] + "   " + numbers_dict[seconds][0])
        print(numbers_dict[h[0]][1] + "   " + numbers_dict[h[1]][1] + "   " + "   " + zero[1] + "   " + numbers_dict[minutes][1] + "   " + "   " + zero[1] + "   " + numbers_dict[seconds][1])
        print(numbers_dict[h[0]][2] + "   " + numbers_dict[h[1]][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[minutes][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[seconds][2])
        print(numbers_dict[h[0]][3] + "   " + numbers_dict[h[1]][3] + "   " + "   " + zero[3] + "   " + numbers_dict[minutes][3] + "   " + "   " + zero[3] + "   " + numbers_dict[seconds][3])
        print(numbers_dict[h[0]][4] + "   " + numbers_dict[h[1]][4] + "   " + "   " + zero[4] + "   " + numbers_dict[minutes][4] + "   " + "   " + zero[4] + "   " + numbers_dict[seconds][4])
        print(numbers_dict[h[0]][5] + "   " + numbers_dict[h[1]][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[minutes][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[seconds][5])
        print(numbers_dict[h[0]][6] + "   " + numbers_dict[h[1]][6] + "   " + "   " + zero[6] + "   " + numbers_dict[minutes][6] + "   " + "   " + zero[6] + "   " + numbers_dict[seconds][6])
    
    
    elif len(hour) == 1 and len(minutes) == 2 and len(seconds) == 1 :
        m = list(minutes)
        print(zero[0] + "   " + numbers_dict[hour][0] + "   " + "   " + numbers_dict[m[0]][0] + "   " + numbers_dict[m[1]][0] + "   " + "   " + zero[0] + "   " + numbers_dict[seconds][0])
        print(zero[1] + "   " + numbers_dict[hour][1] + "   " + "   " + numbers_dict[m[0]][1] + "   " + numbers_dict[m[1]][1] + "   " + "   " + zero[1] + "   " + numbers_dict[seconds][1])
        print(zero[2] + "   " + numbers_dict[hour][2] + "  " + a + "  " + numbers_dict[m[0]][2] + "   " + numbers_dict[m[1]][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[seconds][2])
        print(zero[3] + "   " + numbers_dict[hour][3] + "   " + "   " + numbers_dict[m[0]][3] + "   " + numbers_dict[m[1]][3] + "   " + "   " + zero[3] + "   " + numbers_dict[seconds][3])
        print(zero[4] + "   " + numbers_dict[hour][4] + "   " + "   " + numbers_dict[m[0]][4] + "   " + numbers_dict[m[1]][4] + "   " + "   " + zero[4] + "   " + numbers_dict[seconds][4])
        print(zero[5] + "   " + numbers_dict[hour][5] + "  " + a + "  " + numbers_dict[m[0]][5] + "   " + numbers_dict[m[1]][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[seconds][5])
        print(zero[6] + "   " + numbers_dict[hour][6] + "   " + "   " + numbers_dict[m[0]][6] + "   " + numbers_dict[m[1]][6] + "   " + "   " + zero[6] + "   " + numbers_dict[seconds][6])
    
    
    elif len(hour) == 1 and len(minutes) == 1 and len(seconds) == 2 :
        s = list(seconds)
        print(zero[0] + "   " + numbers_dict[hour][0] + "   " + "   " + zero[0] + "   " + numbers_dict[minutes][0] + "   " + "   " + numbers_dict[s[0]][0] + "   " + numbers_dict[s[1]][0])
        print(zero[1] + "   " + numbers_dict[hour][1] + "   " + "   " + zero[1] + "   " + numbers_dict[minutes][1] + "   " + "   " + numbers_dict[s[0]][1] + "   " + numbers_dict[s[1]][1])
        print(zero[2] + "   " + numbers_dict[hour][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[minutes][2] + "  " + a + "  " + numbers_dict[s[0]][2] + "   " + numbers_dict[s[1]][2])
        print(zero[3] + "   " + numbers_dict[hour][3] + "   " + "   " + zero[3] + "   " + numbers_dict[minutes][3] + "   " + "   " + numbers_dict[s[0]][3] + "   " + numbers_dict[s[1]][3])
        print(zero[4] + "   " + numbers_dict[hour][4] + "   " + "   " + zero[4] + "   " + numbers_dict[minutes][4] + "   " + "   " + numbers_dict[s[0]][4] + "   " + numbers_dict[s[1]][4])
        print(zero[5] + "   " + numbers_dict[hour][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[minutes][5] + "  " + a + "  " + numbers_dict[s[0]][5] + "   " + numbers_dict[s[1]][5])
        print(zero[6] + "   " + numbers_dict[hour][6] + "   " + "   " + zero[6] + "   " + numbers_dict[minutes][6] + "   " + "   " + numbers_dict[s[0]][6] + "   " + numbers_dict[s[1]][6])
    
    
    elif len(hour) == 2 and len(minutes) == 2 and len(seconds) == 1 :
        h = list(hour)
        m = list(minutes)
        print(numbers_dict[h[0]][0] + "   " + numbers_dict[h[1]][0] + "   " + "   " + numbers_dict[m[0]][0] + "   " + numbers_dict[m[1]][0] + "   " + "   " + zero[0] + "   " + numbers_dict[seconds][0])
        print(numbers_dict[h[0]][1] + "   " + numbers_dict[h[1]][1] + "   " + "   " + numbers_dict[m[0]][1] + "   " + numbers_dict[m[1]][1] + "   " + "   " + zero[1] + "   " + numbers_dict[seconds][1])
        print(numbers_dict[h[0]][2] + "   " + numbers_dict[h[1]][2] + "  " + a + "  " + numbers_dict[m[0]][2] + "   " + numbers_dict[m[1]][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[seconds][2])
        print(numbers_dict[h[0]][3] + "   " + numbers_dict[h[1]][3] + "   " + "   " + numbers_dict[m[0]][3] + "   " + numbers_dict[m[1]][3] + "   " + "   " + zero[3] + "   " + numbers_dict[seconds][3])
        print(numbers_dict[h[0]][4] + "   " + numbers_dict[h[1]][4] + "   " + "   " + numbers_dict[m[0]][4] + "   " + numbers_dict[m[1]][4] + "   " + "   " + zero[4] + "   " + numbers_dict[seconds][4])
        print(numbers_dict[h[0]][5] + "   " + numbers_dict[h[1]][5] + "  " + a + "  " + numbers_dict[m[0]][5] + "   " + numbers_dict[m[1]][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[seconds][5])
        print(numbers_dict[h[0]][6] + "   " + numbers_dict[h[1]][6] + "   " + "   " + numbers_dict[m[0]][6] + "   " + numbers_dict[m[1]][6] + "   " + "   " + zero[6] + "   " + numbers_dict[seconds][6])
    

    elif len(hour) == 1 and len(minutes) == 2 and len(seconds) == 2 :
        s = list(seconds)
        m = list(minutes)                   
        print(zero[0] + "   " + numbers_dict[hour][0] + "   " + "   " + numbers_dict[m[0]][0] + "   " + numbers_dict[m[1]][0] + "   " + "   " + numbers_dict[s[0]][0] + "   " + numbers_dict[s[1]][0])
        print(zero[1] + "   " + numbers_dict[hour][1] + "   " + "   " + numbers_dict[m[0]][1] + "   " + numbers_dict[m[1]][1] + "   " + "   " + numbers_dict[s[0]][1] + "   " + numbers_dict[s[1]][1])
        print(zero[2] + "   " + numbers_dict[hour][2] + "  " + a + "  " + numbers_dict[m[0]][2] + "   " + numbers_dict[m[1]][2] + "  " + a + "  " + numbers_dict[s[0]][2] + "   " + numbers_dict[s[1]][2])
        print(zero[3] + "   " + numbers_dict[hour][3] + "   " + "   " + numbers_dict[m[0]][3] + "   " + numbers_dict[m[1]][3] + "   " + "   " + numbers_dict[s[0]][3] + "   " + numbers_dict[s[1]][3])
        print(zero[4] + "   " + numbers_dict[hour][4] + "   " + "   " + numbers_dict[m[0]][4] + "   " + numbers_dict[m[1]][4] + "   " + "   " + numbers_dict[s[0]][4] + "   " + numbers_dict[s[1]][4])
        print(zero[5] + "   " + numbers_dict[hour][5] + "  " + a + "  " + numbers_dict[m[0]][5] + "   " + numbers_dict[m[1]][5] + "  " + a + "  " + numbers_dict[s[0]][5] + "   " + numbers_dict[s[1]][5])
        print(zero[6] + "   " + numbers_dict[hour][6] + "   " + "   " + numbers_dict[m[0]][6] + "   " + numbers_dict[m[1]][6] + "   " + "   " + numbers_dict[s[0]][6] + "   " + numbers_dict[s[1]][6])
                                          
                       
    elif len(hour) == 2 and len(minutes) == 1 and len(seconds) == 2:
        s = list(seconds)
        h = list(hour)                   
        print(numbers_dict[h[0]][0] + "   " + numbers_dict[h[1]][0] + "   " + "   " + zero[0] + "   " + numbers_dict[minutes][0] + "   " + "   " + numbers_dict[s[0]][0] + "   " + numbers_dict[s[1]][0])
        print(numbers_dict[h[0]][1] + "   " + numbers_dict[h[1]][1] + "   " + "   " + zero[1] + "   " + numbers_dict[minutes][1] + "   " + "   " + numbers_dict[s[0]][1] + "   " + numbers_dict[s[1]][1])
        print(numbers_dict[h[0]][2] + "   " + numbers_dict[h[1]][2] + "  " + a + "  " + zero[2] + "   " + numbers_dict[minutes][2] + "  " + a + "  " + numbers_dict[s[0]][2] + "   " + numbers_dict[s[1]][2])
        print(numbers_dict[h[0]][3] + "   " + numbers_dict[h[1]][3] + "   " + "   " + zero[3] + "   " + numbers_dict[minutes][3] + "   " + "   " + numbers_dict[s[0]][3] + "   " + numbers_dict[s[1]][3])
        print(numbers_dict[h[0]][4] + "   " + numbers_dict[h[1]][4] + "   " + "   " + zero[4] + "   " + numbers_dict[minutes][4] + "   " + "   " + numbers_dict[s[0]][4] + "   " + numbers_dict[s[1]][4])
        print(numbers_dict[h[0]][5] + "   " + numbers_dict[h[1]][5] + "  " + a + "  " + zero[5] + "   " + numbers_dict[minutes][5] + "  " + a + "  " + numbers_dict[s[0]][5] + "   " + numbers_dict[s[1]][5])
        print(numbers_dict[h[0]][6] + "   " + numbers_dict[h[1]][6] + "   " + "   " + zero[6] + "   " + numbers_dict[minutes][6] + "   " + "   " + numbers_dict[s[0]][6] + "   " + numbers_dict[s[1]][6])
                       
                        
    elif len(hour) == 2 and len(minutes) == 2 and len(seconds) == 2 :
        s = list(seconds)
        h = list(hour)
        m = list(minutes)
        print(numbers_dict[h[0]][0] + "   " + numbers_dict[h[1]][0] + "   " + "   " + numbers_dict[m[0]][0] + "   " + numbers_dict[m[1]][0] + "   " + "   " + numbers_dict[s[0]][0] + "   " + numbers_dict[s[1]][0])
        print(numbers_dict[h[0]][1] + "   " + numbers_dict[h[1]][1] + "   " + "   " + numbers_dict[m[0]][1] + "   " + numbers_dict[m[1]][1] + "   " + "   " + numbers_dict[s[0]][1] + "   " + numbers_dict[s[1]][1])
        print(numbers_dict[h[0]][2] + "   " + numbers_dict[h[1]][2] + "  " + a + "  " + numbers_dict[m[0]][2] + "   " + numbers_dict[m[1]][2] + "  " + a + "  " + numbers_dict[s[0]][2] + "   " + numbers_dict[s[1]][2])
        print(numbers_dict[h[0]][3] + "   " + numbers_dict[h[1]][3] + "   " + "   " + numbers_dict[m[0]][3] + "   " + numbers_dict[m[1]][3] + "   " + "   " + numbers_dict[s[0]][3] + "   " + numbers_dict[s[1]][3])
        print(numbers_dict[h[0]][4] + "   " + numbers_dict[h[1]][4] + "   " + "   " + numbers_dict[m[0]][4] + "   " + numbers_dict[m[1]][4] + "   " + "   " + numbers_dict[s[0]][4] + "   " + numbers_dict[s[1]][4])
        print(numbers_dict[h[0]][5] + "   " + numbers_dict[h[1]][5] + "  " + a + "  " + numbers_dict[m[0]][5] + "   " + numbers_dict[m[1]][5] + "  " + a + "  " + numbers_dict[s[0]][5] + "   " + numbers_dict[s[1]][5])
        print(numbers_dict[h[0]][6] + "   " + numbers_dict[h[1]][6] + "   " + "   " + numbers_dict[m[0]][6] + "   " + numbers_dict[m[1]][6] + "   " + "   " + numbers_dict[s[0]][6] + "   " + numbers_dict[s[1]][6])
                     
   
    print("\r", end="", flush=True)
    change += 1
    time.sleep(1)
    os.system('cls||clear')



  
    



