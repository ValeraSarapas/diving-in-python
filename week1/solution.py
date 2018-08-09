# coding: utf-8
# In[1]:

import sys
if __name__ == '__main__':
    print('Run ',sys.argv)
    digit_string = sys.argv[1]
    summa = 0
    for digit in digit_string:
        if digit.isdigit():
            summa = summa + int(digit)
    print('Summa digits in the string is: ',summa)    

