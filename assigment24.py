#!/usr/bin/env python
# coding: utf-8

# In[1]:


# take a input from the user and count the character and put it into the directory.
strr = input ("Enter a string")
count = {}
for chrr in strr:
    if chrr in count:
        count[chrr] += 1
    else:
        count[chrr]= 1
for chrr in count:
    print(chrr,":",count[chrr])


# In[4]:


# take a input from user if this conditions are true A-P,c-z,0-9,(@,#,!)
string = input("Enter a string")
lowc = 0
uprc = 0
num = 0
sym = 0
for chrr in string:
    if("A" <= chrr <= "p"):
        uprc += 1
    elif("c" <= chrr <= "z"):
        lowc += 1
    elif(chrr == "@" or chrr == "#" or chrr == "!"):
        sym += 1
    elif("9" >= chrr >= "0"):
        num +=1
if(lowc > 0 and uprc > 0 and num > 0 and sym >0):
    print(bool(1))
else:
    print(bool(0))


# In[ ]:


# 3. print a pattern


# In[6]:


for i in range(0,5):
    for j in range(0,5):
        if (i+j >= 4):
            print("*",end="")
        else:
            print(" ", end="")
    print("")    


# In[ ]:


#print the pattern


# In[7]:


row = int(input("Enter the number of row"))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print("")   
    


# In[ ]:




