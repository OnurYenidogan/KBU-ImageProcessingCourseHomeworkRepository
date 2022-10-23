#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input ("Kaç Adet Sayı Girilecek: "))
a= []
for i in range(0,n):
    elem=int(input("Sayıyı Girin: "))
    a.append(elem)
avg=sum(a)/n
print("Girilen Sayıların Ortalaması : ",round(avg,2))


# In[ ]:




