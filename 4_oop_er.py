# REMINDER: Start with print, and save and test after every change!

# Challenge 0: For this activity, we start with a Patient class pre-created.
# Look over the code. It's okay not to understand every single line, but try to
# understand at least broadly what each method does.


class Patient:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.is_checked_in = False
        self.does_drink = None
        self.does_smoke = None
        self.recommendation = None
        self.diagnosis = None
        self.extra_notes = None

    def print_info(self):
        print('-----PATIENT', self.first_name, self.last_name, '----')
        print('Is checked in:', self.is_checked_in)
        print('Drinks?', self.does_drink)
        print('Smokes?', self.does_smoke)
        print('Blood pressure?', self.blood_pressure)
        print('Diagnosis:', self.diagnosis)
        print('Recommendation:', self.recommendation)

    def check_in(self):
        self.is_checked_in = True

    def nurse_check_up(self):
        smoke_string = input('Does the patient smoke? ')
        drink_string = input('Does the patient drink? ')
        blood_pressure_string = input('Patient blood-pressure? ')
        if smoke_string == 'yes':
            self.does_smoke = True
        else:
            self.does_smoke = False
        if drink_string == 'yes':
            self.does_drink = True
        else:
            self.does_drink = False
        self.blood_pressure = int(blood_pressure_string)

    def doctor_diagnose(self):
        if not self.blood_pressure:
            print('Patient must visit nurse first')
            return

        if self.blood_pressure > 180:
            self.diagnosis = 'Hypertension Crisis'
            self.recommendation = 'Immediate treatment in ER'
        elif self.blood_pressure > 140:
            self.diagnosis = 'Stage 2 Hypertension'
        elif self.blood_pressure > 130:
            self.diagnosis = 'Stage 1 Hypertension'

        self.extra_notes = input('Extra physician notes? ')


print('Challenge 1 -------------')
# Challenge 1:
# Debugging challenge: Examine the class above. When you uncomment the
# following lines, an error occurs. Instead of saying "Patient must visit nurse
# first", it causes a Python error.  Why is that? Can you fix it?
# HINT: This requires adding another line of code to the __init__ in the
# original class, to make sure that a certain property gets a default value.

#eric = Patient('Eric', 'Idle')
#eric.doctor_diagnose()


print('Challenge 2 -------------')
# Challenge 2:
# Time to get practice with the concept of extension and "subclasses"!
# Here's the challenge: The General Oop Hospital has an Emergency Room, and
# they want patients there processed differently.
# 1. Create a new class called: EmergencyPatient
# 2. EmergencyPatient should inherit from Patient





print('Challenge 3 -------------')
# Challenge 3:
# Note: This one is tricky!
# - Create a new method within the EmergencyPatient class called "triage"
# - This method should ask the user a series of questions
# - Using a series of if statements (and possibly "else", "return" or "elif"),
# and check if those are equal to "yes" to set an appropriate "triage_level"

# In Pseudocode, you should do have the triage function do the following:
# - Requires life saving intervention?
#       - yes means triage_level = 1, and triage ends
# - Is high risk: confused, lethargic, severe distress?
#       - yes means triage_level = 2, and triage ends
# - How many resources needed (none, some, or many):
#       - "none" means triage_level = 5, and triage ends
#       - "one" means triage_level = 4, and triage ends
#       - "many" means triage_level = 3, and triage ends


print('Challenge 4 -------------')
# Challenge 4:
# So far so good, but the print_info() method of EmergencyPatient isn't showing
# the new triage_level property. Override print_info() so that it prints out
# triage_level.

# Hint: Use super().print_info() at the top of your method to re-use the base
# class's print_info() method, so you don't have to duplicate anything.





print('Challenge 5 -------------')
# Challenge 5:
# - The hospital needs all emergency patients to start with is_checked_in set
# to True by default, since ER patients are automatically checked-in.
# - Can you override __init__ method in the EmergencyPatient class that makes
# is_checked_in start as True for EmergencyPatients?
# Hint: Use super().__init__(first_name, last_name)





print('-------------')
# Bonus Challenge 1:
# An important part of coding in any language is learning to solve errors
# in your code. We've written a program, called Debug Trainer, to help you
# practice this. Download it and run it three times on this file (4_oop_er.py)
# and see if you can figure out how to solve the bugs it creates.
#
# If you're on Linux, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/debug-trainer_1.1.0_amd64.AppImage
#
# If you're on a Mac, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/Debug.Trainer_1.1.0_x64.dmg
#
# If you're on Windows, download it at this link: https://github.com/kickstartcoding/debug_trainer_app/releases/download/debug-trainer-v1.1.0/Debug.Trainer_1.1.0_x64.msi


# Bonus Challenge 2:
# Look up the following less common concepts, and see if you can explain them
# in your own words.
# 1. Singleton pattern
# 2. Factory pattern
# 3. Object pool
# 4. Mixin

# Advanced Bonus Challenge:
# Look up how to do multiple inheritance in Python. Refactor the
# EmergencyPatient into 3 total classes:
# 1. Emergency "mixin"
# 2. Patient "base class"
# 3. EmergencyPatient that derives from both Emergency and Patient.
#
# The EmergencyPatient class should have the triage method, but nothing else.
#
# Why do you think this pattern is useful?
