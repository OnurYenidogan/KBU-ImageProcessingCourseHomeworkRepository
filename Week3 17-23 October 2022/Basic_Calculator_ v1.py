#!/usr/bin/env python
# coding: utf-8

# In[ ]:


again = 1
while again == 1:
    o=(input ("Pick and type the operation's symbol (+,-,*,/)"))
    if o == "+":
        first=int(input ("Enter the first value "))
        second=int(input ("Enter the second value "))
        res=first+second
        print("The result is ",res)
    elif o == "-":
        first=int(input ("Enter the first value "))
        second=int(input ("Enter the second value "))
        res=first-second
        print("The result is ",res)
    elif o == "*":
        first=int(input ("Enter the first value "))
        second=int(input ("Enter the second value "))
        res=first*second
        print("The result is ",res)
    elif o == "/":
        first=int(input ("Enter the first value "))
        second=int(input ("Enter the second value "))
        res=first/second
        print("The result is ",res)
    else:
        print("Couldn't pick the operation")
    o = None
    res = None
    first= None
    second = None


# In[ ]:





# In[ ]:




