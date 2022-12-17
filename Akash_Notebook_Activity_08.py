#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Employee:
    def __init__(self):
        self.name = "Akash bhat"
        self.id = "01"
        self.designation = "software Engineer"
        self.Working_hours = "50"

    def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

    def Remove_Employee(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"

    def Promote_Employee(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"


class FrontEnd_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

class Software_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
      
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)

class Backend_Engineer(Employee):
  def __init__(self):
      self.name = "_"
      self.id = "_"
      self.designation = "_"
      self.Working_hours = "_"
  def Display_Employee(self):
      print("Identity number of the employee = " + self.id)
      print("Name of the employee = " + self.name)
      print("Position of the employee of the employee = " + self.designation)
      print("Woking hours of the employee = " + self.Working_hours)



emp = Employee()
SDE = Software_Engineer()
FEE = FrontEnd_Engineer()
BEE = Backend_Engineer()


def main():
  choice = int(input("\nSelect the desired option from the below menu:- \n 1. To display Employee \n 2. To promote Employee\n 3. To remove Employees\n 4. To add EMployees\n 5. To Exit the program\n\n"))
  if(choice == 1):
    emp.Display_Employee()

  if(choice == 2):
    emp.id == SDE.id
    emp.name == SDE.name
    emp.designation == SDE.designation
    emp.Working_hours == SDE.Working_hours
    print("Identity number of the employee = " + SDE.id)
    print("Name of the employee = " + SDE.name)
    print("Position of the employee of the employee = " + SDE.designation)
    print("Woking hours of the employee = " + SDE.Working_hours)
    print("\nEmploye Promoted successfully\n")

  if(choice == 3):
    emp.Remove_Employee()
    emp.name = "_"
    emp.id = "_"
    emp.designation = "_"
    emp.Working_hours = "_"

    print("Employee Removed successfully !!!")

  if(choice == 4):
    print("Employee details added successfuly !!!\n")
    emp.Display_Employee()
    print("\nEmployee Identity added successfully !!!")

  if(choice == 5):
    print("Thank You very much !!!")
    return 0

  else:
    print("!!!!!!!!!! BYE !!!!!!!!!!")

  main()

main()


# In[ ]:




