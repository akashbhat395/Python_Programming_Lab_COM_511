#!/usr/bin/env python
# coding: utf-8

# In[44]:


side1 = int(input("Enter side1 of Triangle: "))
side2 = int(input("Enter side2 of Triangle: "))
side3 = int(input("Enter side3 of Triangle: "))

def check(side1, side2, side3):
    if(side1 ** 2 + side2 ** 2 == side3**2):
        print("3 Sides form a rightt angle triangle")

    else:
        print("It is not rt angle triangle")

def area(side1, side2, side3):
    s = (side1+side2+side3)/2
    area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
    print("Area of Triangle is: %0.2f" %area)

    print()

    
check(side1, side2, side3)
area(side1, side2, side3)


# In[ ]:





# In[ ]:




