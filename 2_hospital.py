# REMINDER: Start with print, and save and test after every change!

print('Hello function world!')

# For this challenge, we are going to build up a set of functions to create
# code for a semi-realistic situation: We will be building helper functions to
# manage data about a patient at a hospital. You can imagine the final software
# being useful for nurses and doctors to keep track of information on patients.

# The information about patients will be in a dictionary that is passed around
# via parameters to and from functions.

print('Challenge 1 -------------')
# Challenge 1:
# Uncomment and examine the following code. Can you explain what every line is
# doing?

# def patient_initialize(patient):
#     patient['first_name'] = 'Eric'
#     patient['last_name'] = 'Idle'
#     patient['is_checked_in'] = False

# eric = {}
# patient_initialize(eric)
# print(eric)

## Answer ##

# def patient_initialize(patient):
#     patient['first_name'] = 'Eric'
#     patient['last_name'] = 'Idle'
#     patient['is_checked_in'] = False

# eric = {}                     #eric is variable holding empty dictionary#
# patient_initialize(eric)      #function invoked for eric info
# print(eric)                   #data listed in function for eric is printed

print('Challenge 2 -------------')
# Challenge 2:
####Part One###
# Patient_initialize is too inflexible. We want it to work for ANY patient.
# - Rewrite the function definition of patient_initialize so that it can accept
# two additional parameters: "first", and "last"
# - Rewrite the lines containing 'Eric' and 'Idle' to use these two new
# parameter variables that you just created
####Part Two###
# - Write 2 more invocations of the function to create a patient for yourself
# and a famous celebrity (or someone sitting next to you!)
# - Use print to confirm that your function is working correctly by printing
# out the patient variable before and after the invocation of the function.

####Answer Part One###
# def patient_initialize(patient, first, last):
#     patient['first_name'] = first
#     patient['last_name'] = last
#     patient['is_checked_in'] = False

# eric = {} 
# patient_initialize(eric, 'Michael', 'B') 
# print(eric) 

####Answer Part Two###
def patient_initialize(patient, first, last):
    patient['first_name'] = first
    patient['last_name'] = last
    patient['is_checked_in'] = False

person1 = {} 
patient_initialize(person1, 'Michael', 'B') 
print(person1) 

person2 = {} 
patient_initialize(person2, 'Keanu', 'R') 
print(person2)


print('Challenge 3 -------------')
# Challenge 3:
# - Write a new function called "patient_check_in".
# - This function should accept a patient dictionary as an argument, much like
# the function from Challenges 1 & 2, and then modify the patient to make
# "is_checked_in" assigned to be True.
# - Like previous challenges, use print to verify the function works.

def patient_initialize(patient):
    patient['is_checked_in'] = True


print('Challenge 4 -------------')
# Challenge 4:
# - Write a new function called "patient_nurse_check_up". Like previous
# challenges, it should take a patient dictionary as an argument.
# - Using input(), it should then ask the following questions:
#     - Does the patient smoke?
#     - Does the patient drink?
#     - Patient blood-pressure?
# - It should store the responses into the patient dictionary, stored as new
# keys (name the keys whatever you think makes sense).
# - Like previous challenges, use print to verify the function works.







print('Challenge 5 -------------')
# Challenge 5:
# Time to bring it all together:
# 1. Write a new function called "patient_visit".
# 2. Using input(), it should ask the name of the patient, then initialize the
# patient with that information.
# 3. It should then use all of the above functions to "process" the patient
# (e.g. invoking them one at a time in sequence)

# Hint: Feel free to comment out the previous invocations of the above function
# Add a prints as needed to report back on the process.





print('-------------')
# Bonus Challenge:
# Create another function called "patient_doctor_diagnose". It should only
# accept patients who have already been checked in and visited a nurse. It
# should allow a doctor to enter a "diagnosis" and "recommendation".
#
# 1. Check that blood-pressure is below 120. If between 120-130 it should
#    diagnose "Stage 1 Hypertension", if between 130-180 "Stage 2 Hypertension"
# 2. Recommend the patient a) visit the ER if blood pressure is above 180, or
#    b) if the patient smokes, recommend the patient stop.






print('-------------')
# Advanced Bonus Challenge:
# Where does our data go? At the end of every check up, we should store it in a
# file. Maybe try writing a CSV?

