#!/usr/bin/env python
# coding: utf-8

# In[1]:


# swap two number without third variable.
a = 10
b = 20
print("Before swap",a,b)
a = a+b
b = a-b
a = a-b
print("After swap",a,b)


# In[15]:


#HCF
def Hcf(x,y):
    if(x>=y):
        check = x
    else:
        check = y
    while(check%x != 0 or check%y != 0):
        check +=1
    return check

x = int(input("Enter x:"))
y = int(input("Enter y:"))
print("HCF :",Hcf(x,y))


# In[14]:


def lcm(x,y):
    if(x>=y):
        check = y
    else:
        check = x
    while(x%check !=0 or y%check !=0):
        check -=1
    return check
x = int(input("Enter x:"))
y = int(input("Enter y:"))
print("LCM:",lcm(x,y))


# In[ ]:




