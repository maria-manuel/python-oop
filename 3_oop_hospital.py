# REMINDER: Start with print, and save and test after every change!


# Welcome to General Hospital Oop! Now this activity involves transforming the
# code form activity 1 into the "object oriented programming" syntax.


print('Challenge 1 -------------')
# Challenge 1:
# 1. See this class definition, and instantiation? Read it and understand it.
# Can you identify all the different parts?
# 2. Modify it to also support a last name, instead of the "hard-coded" last
# name of Cleese.


class Patient:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = 'Cleese'
        self.is_checked_in = False


john = Patient('John')



print('Challenge 2 -------------')
# Challenge 2:
# - Add a new method to the Patient class called "print_info". It should
# consist of a series of prints to print out all 3 properties of the patient.
# - Create a "Patient" for yourself and a celebrity (or someone sitting next to
# you).
# - Invoke your new print_info() method on your newly created patients to
# ensure the information is getting printed out correctly.

# Hint #1: Adding the method must be done above to the Patient class.
# Hint #2: Consider making the output of the print_info() method look like the
# following:
#        ----- PATIENT -----
#        First name: Jane
#        Last name: Hacker
#        Checked-in status: False




print('Challenge 3 -------------')
# Challenge 3:
# - Add a new method to Patient called "check_in" that changes is_checked_in to
# be True.
# - Using print_info before and after an invocation of check_in(), ensure that
# your check_in() method works.






print('Challenge 4 -------------')
# Challenge 4:
# Write a new method to Patient called "nurse_check_up".
# It should then ask the following questions.
#     1. Does the patient smoke?
#     2. Does the patient drink?
#     3. Patient blood-pressure?
# Hint: Use input() and storing the result in separate properties of the
# patient object.





print('Challenge 5 -------------')
# Challenge 5:
# - Let's refactor the above method by creating "nicer" methods to ask for data
# from the user. We'll create two new methods: ask_for_bool, ask_for_int

# ask_for_bool: This method should ask the user a question given as a string
# argument, and then use input() to ask for "yes" or "no". If the use types in
# "yes" then your method should "return True". Otherwise, your method should
# "return False".

# ask_for_int: This method should convert the user's input into an int. This
# can be done using int(SOMETHING)   (replace "SOMETHING" with a variable name)

# Note: This one is challenging!





print('Challenge 6 -------------')
# Challenge 6:
# Create another method called "doctor_diagnose". It should allow a doctor to
# enter a "diagnosis" and a "recommendation" (two new properties for the
# Patient class). This diagnosis method should do the following:

# 1. Check that blood-pressure is below 120. If between 120-130 it should
# diagnose "Stage 1 Hypertension", if between 130-180 "Stage 2 Hypertension",
# above 180 "Hypertension Crisis"
# 2. Recommend the patient a) visit the ER if blood pressure is above 180 the
# or b) if the patient smokes, recommend the patient stop.

# Tips:
# - Modify the print_info to also show recommendation and diagnosis
# - Make sure the patient starts with a diagnosis and recommendation of None
# when initialized, but later gets it filled in by this method.
# - It should only work on patients who have already been checked in and
# visited a nurse.





print('-------------')
# Bonus Challenge 1:
# An important part of coding in any language is learning to solve errors
# in your code. We've written a program, called Debug Trainer, to help you
# practice this. Download it and run it three times on this file (3_oop_hospital.py)
# and see if you can figure out how to solve the bugs it creates.
#
# If you're on Linux, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/debug-trainer_1.1.0_amd64.AppImage
#
# If you're on a Mac, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/Debug.Trainer_1.1.0_x64.dmg
#
# If you're on Windows, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/Debug.Trainer_1.1.0_x64.msi


# Bonus Challenge 2:
# Spend some time improving your ask_for_bool and ask_for_int methods:
# - ask_for_bool should be "tolerant" of different answers, and accept anything
# like "y", "n", "YES  " etc
# - Both should keep on asking until the user enters a valid answer, letting
# the user know that what was typed is not valid
# - For "cleaner code", since your methods probably don't need the "self"
# parameter, research "static methods", and change them to be that

# Hint: To convert a method into a "static method", simply delete the "self"
# parameter, then add the line "@staticmethod" above the method (this @-sign
# thing is called a "decorator" and they "unlock" extra options for functions
# and methods)


# Advanced Bonus Challenge:
# - Create another (non-static) method called "save". It should take a filename
# as an argument. The Patient information should get saved to that file. This
# can be done with Python's built-in module called "pickle" (research this).
# - Make a static method called "load" that will restore a Patient object
# instance from a "pickled" file.
