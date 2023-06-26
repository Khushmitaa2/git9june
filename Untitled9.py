#!/usr/bin/env python
# coding: utf-8

# In[8]:


setA = {10,20,30}
setB = {30,40,50}
print(setA.difference(setB))
print(setB.difference(setA))


# In[7]:


setA = {10,20,30}
setB = {30,40,50}
setC = {10,20,30,40,50}
print(setC.issuperset(setA))
print(setC.issuperset(setB))


# In[6]:


setA = {10,20,30}
setB = {30,40,50}
setC = {10,20}
print(setB.isdisjoint(setA))
print(setC.isdisjoint(setB))


# In[5]:


setA = {10,5,20,30}
setB = {30,40,50}
setC = {10,20}
setA.symmetric_difference_update(setB)
print(setA)
print(setC.symmetric_difference(setB))


# In[4]:


row = int(input("Enter a number of row"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")
    print("")
for i in range(0,row):
    for j in range(0,row-i-1):
        print("*",end="")
    print("")


# In[3]:


row = int(input("Enter a number of row"))
for i in range(0,row):
    for j in range(0,row):
        if(i ==row-1 or i == 0 or j==row-1 or j==0):
            print("*",end="")
        else:
             print(" ",end="")
    print("")


# In[2]:


row = int(input("Enter a number of row"))
for i in range(0,row):
    print(i+1)
    for j in range(0,i+1):
        print("*",end="")
    print("")


# In[1]:


row = int(input("Enter a number of row"))
for i in range(1,row+1):
    print(i,end="")
    for j in range(1,(i*i)+1):
        print("*",end="")
    print("")


# In[ ]:




