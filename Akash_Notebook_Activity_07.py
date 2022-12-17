#!/usr/bin/env python
# coding: utf-8

# # Program to convert temperature to and from Celsius to Fahrenheit

# In[7]:


# Temperature in celsius degree
celsius = 40
# Converting the temperature to
# fahrenheit using the above
# mentioned formula
fahrenheit = (celsius * 1.8) + 32
# printing the result
print("%.2f Celsius is equivalent to: %.2f Fahrenheit" %(celsius,fahrenheit))


# # Second taking Input from user

# In[8]:


celsius = int(input("Enter the temperature: "))
# Converting the temperature to
# fehrenheit using the above
# mentioned formula
fahrenheit = (celsius * 1.8) + 32
# printing the result
print("%.2f Celsius is equivalent to: %.2f Fahrenheit" %(celsius, fahrenheit))


# # Converting the given program from statement to function for Celsius to Fahrenheit conversion.

# In[9]:


# Define function to convert Celsius into Fahrenheit
def ConvertCtoF(C):
# Convert the Celsius into Fahrenheit
    F = (C* 1.8) + 32

# Return the conversion value
    return F

# Take the Fahrenheit value from the user
C = float(input("Enter the temperature in Celsius: "))

# Print the Celsius value
print("Temperature in Celsius = {:.2f}".format(C))
# Print the Fahrenheit value
print("Temperature in Fahrenheit = {:.2f}".format(ConvertCtoF(C)))


# # Converting the given program from statement to function for Fahrenheit to Celsius conversion.

# In[10]:


# Define function to convert Fahrenheit to Celsius
def ConvertFtoC(F):
# Convert the Fahrenheit into Celsius
    C = (5 / 9) * (F - 32)
# Return the conversion value

    return C

# Take the Fahrenheit value from the user
F = float(input("Enter the temperature in Fahrenheit: "))

# Print the Fahrenheit value
print("Temperature in Fahrenheit = {:.2f}".format(F))
# Print the Celsius value
print("Temperature in Celsius = {:.2f}".format(ConvertFtoC(F)))


# In[ ]:



