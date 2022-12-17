#!/usr/bin/env python
# coding: utf-8

# In[54]:


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))


def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1

    elif (num2 >= num1) and (num2 >= num3):
        largest = num2

    else:
        largest = num3
        print("The largest number is", largest)
        print("\n")

def armstrong(num):
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        
    if num == sum:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")
        
find_largest(num1, num2, num3)
armstrong(num1)
armstrong(num2)
armstrong(num3)


# In[ ]:





# In[ ]:



