#!/usr/bin/env python
# coding: utf-8

# In[56]:


database = [("Akash Bhat", 39, "2020a1r039@mietjammu.in",'Male','05/12/22','Jammu','5th','A1',1234567890)]

def quering():
    for idx,element in enumerate(database):
        print(f"Name:{database[idx][0]}")
        print(f"Roll no:{database[idx][1]}")
        print(f"Email Id:{database[idx][2]}")
        print(f"Gender:{database[idx][3]}")
        print(f"Date:{database[idx][4]}")
        print(f"City:{database[idx][5]}")
        print(f"Semester:{database[idx][6]}")
        print(f"Section:{database[idx][7]}")
        print(f"Phone No.:{database[idx][8]}")
        
quering()


# In[ ]:



