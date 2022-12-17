#!/usr/bin/env python
# coding: utf-8

# # Reverse kth row in matrix

# # 1. using reversed() and loop

# In[1]:


test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],[3, 6], [3, 7, 4], [2, 9]]

print("The original list is :" + str(test_list))

K = 3

res = []
for idx, ele in enumerate(test_list):

    if (idx + 1) % K == 0:
        res.append(list(reversed(ele)))        
    else:
        res.append(ele)

# printing result
print("After reversing every Kth row: " + str(res))


# # 2. using Slicing and List comprehension

# In[2]:


test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],[3, 6], [3, 7, 4], [2, 9]]

print("The original list is : " + str(test_list))
K = 3
res = [ele[::-1] if (idx + 1) % K == 0 else ele for idx,ele in enumerate(test_list)]
print("After reversing every Kth row: " + str(res))


# In[ ]:




