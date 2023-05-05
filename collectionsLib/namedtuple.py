from collections import namedtuple
# namedtuple make tuple element accessing easier

Student = namedtuple("Student", ('fname', 'lname', 'DOB')) 

roll_num_23 = Student('rohit', 'ghawale', '150999')

# print lname
print(roll_num_23.lname) # using namedtuple
print(roll_num_23[1]) # using conventional method
