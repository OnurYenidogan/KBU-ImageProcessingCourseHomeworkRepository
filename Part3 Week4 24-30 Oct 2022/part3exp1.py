#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install opencv-python')


# In[ ]:


import cv2
import numpy as np
picture1 = cv2.imread("Onur.jpg")
cv2.imshow("Onur",picture1)
print(picture1.size)
print(picture1.dtype)
print(picture1.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




