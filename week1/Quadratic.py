
# coding: utf-8

# In[1]:


import sys

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    if a is 0:
        print("А не может быть равно 0. В этом случае уравнение линейное.")
    else:
        print ("a: {}, b: {}, c: {}".format(a,b,c))
        D= b**2-4*a*c
        print("Дискриминант: ", D)
        print("D^1/2: ", D**(1/2))
        print("2a: ", 2*a)
        if D >0:
            x1 = int((-b +D**(1/2)) /(2*a))
            x2 = int((-b -D**(1/2)) /(2*a))
            print(f'{x1:d}\n{x2:d}')
        elif D == 0:
            x1=x2= int(-b /(2*a))
            print(f'{x1:d}\n{x2:d}')
        else:
            print("корней на множестве действительных чисел нет")        
    print("test1: ", a*x1**2+b*x1+c)
    print("test2: ", a*x2**2+b*x2+c)
    
        

