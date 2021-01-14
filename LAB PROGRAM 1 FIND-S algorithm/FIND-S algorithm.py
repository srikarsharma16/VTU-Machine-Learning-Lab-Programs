#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
a = []


# In[14]:


with open('C:/BACHELOR OF ENGINEERING(ISE) NOTES/7th sem/ML LAB PROGRAMS/enjoysport.csv', 'r') as csvfile: 
    for row in csv.reader(csvfile):
        a.append(row) 
    print(a)


# In[15]:


print("\nThetotalnumberoftraininginstancesare:",len(a))


# In[18]:


num_attribute =len(a[0])-1
print("\n The initial hypothesis is : ")


# In[20]:


hypothesis = ['0']*num_attribute
print(hypothesis)


# In[22]:


for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j]=='0'or hypothesis[j]==a[i][j]: 
                hypothesis[j] =a[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is:\n" .format(i+1),hypothesis)


# In[24]:


print("\n The Maximally specific hypothesis for the training instance is ")
print(hypothesis)

