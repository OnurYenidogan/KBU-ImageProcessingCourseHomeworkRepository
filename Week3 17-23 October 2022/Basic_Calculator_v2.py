#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fourops(f,op,s):
    if op == "+":
        return f + s
    elif op == "-":
        return f - s
    elif op == "*":
        return f * s
    elif op == "/":
        return f / s
again = 1
while again == 1:
    o=(input ("Pick and type the operation's symbol (+,-,*,/)"))
    if o == "+" or o == "-" or o == "*" or o == "/":
        first=int(input ("Enter the first value "))
        second=int(input ("Enter the second value "))
        print("The result is ", fourops(first,o,second))
    else:
        print("Couldn't pick the operation")
    o = None
    res = None
    first= None
    second = None


# In[ ]:





# In[ ]:




