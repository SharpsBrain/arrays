#!/usr/bin/env python
# coding: utf-8

# In[15]:


cars=["Ford", "Volvo", "BMW"]
cars[2]="Toyotta"
x=len(cars)
cars.append("Honda")
cars.pop(0)
cars.remove("Volvo")
print(len(cars))
for x in cars:
    print(x)


# In[ ]:


x=len(cars)
#append()
#clear()

