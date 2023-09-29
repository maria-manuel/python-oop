# REMINDER: Start with a print, save and test after every change.

print('Hello oop world!')

print('Challenge 1 -------------')
# Challenge 1:
# Examine the following function code. Can you write an invocation that will
# cause it to print the phrase: "Don't Stop Believin"?

# def journey(verb, action='Do'):
#     print(action, 'Stop', verb + 'in')

def journey(verb, action='Do'):
    print(action, 'Stop', verb + 'in')

journey("Believe", "Don't")


print('Challenge 2 -------------')
# Challenge 2:
# Your goal for this challenge is to write code that prints the lyrics to a
# popular chorus 3 times, each lyric on a separate line, and each chorus
# labelled with "Chorus 1", "Chorus 2", "Chorus 3". The output should look a
# bit like this (except with "repeat" actually:
#         Chorus 1
#         Don't stop believin'
#         Hold on to the feelin'
#         Streetlight people
#         Chorus 2
#         (...chorus goes here...)
#         Chorus 3
#         (...chorus goes here...)
# chorus = [
#     "Don't stop believin'",
#     "Hold on to the feelin'",
#     "Streetlight people",
# ]

# # HINT: You should do this by creating a new for-loop that contains the chorus
# # for-loop. The outer for-loop should use the "range()" function to go through
# # the numbers 1-3. Examine this example code below:
# for lyric in chorus:
#     pass
# for number in range(3):
#     pass

chorus = [
    "Don't stop believin'",
    "Hold on to the feelin'",
    "Streetlight people",
]
for number in range(1, 4):
    print('Chorus', number)
    for lyric in chorus:
        print(lyric)



print('Challenge 3 -------------')
# Challenge 3
# The following code creates a dictionary "band_info1" that contains
# information on a band. To get practice setting keys in dictionaries, complete
# the code below band_info2 such that band_info1 and band_info2 are equivalent.
# You should not need to modify band_info1 at all.

# band_info1 = {
#     'label': 'Interscope Records',
#     'formed': 1989,
#     'disbanded': 1994,
#     'city': 'San Francisco',
#     'members': {
#         'drums': 'Wanda Day',
#         'guitar': 'Shaunna Hall',
#         'bass': 'Christa Hillhouse',
#         'vocals': 'Linda Perry',
#     },
#     'albums': [
#         'Bigger, Better, Faster, More!',
#         'Hello Mr. President',
#     ],
#     'videos': {
#         1992: 'Dear Mr. President',
#         1993: 'Spaceman',
#         1994: 'Superfly',
#     },
#     'soundtracks': [
#         "Wayne's World 2",
#         'Airheads',
#     ],
# }

# band_info2 = {}
# band_info2['city'] = 'San Francisco'
# band_info2['members'] = {}
# band_info2['members']['drums'] = 'Wanda Day'
# band_info2['albums'] = []
# band_info2['albums'].append('Bigger, Better, Faster, More!')
# # COMPLETE THIS...

# if band_info1 == band_info2:
#     print("Challenge 3 complete!")
# else:
#     print("Challenge 3 not yet done...")

band_info1 = {
    'label': 'Interscope Records',
    'formed': 1989,
    'disbanded': 1994,
    'city': 'San Francisco',
    'members': {
        'drums': 'Wanda Day',
        'guitar': 'Shaunna Hall',
        'bass': 'Christa Hillhouse',
        'vocals': 'Linda Perry',
    },
    'albums': [
        'Bigger, Better, Faster, More!',
        'Hello Mr. President',
    ],
    'videos': {
        1992: 'Dear Mr. President',
        1993: 'Spaceman',
        1994: 'Superfly',
    },
    'soundtracks': [
        "Wayne's World 2",
        'Airheads',
    ],
}

band_info2 = {}
band_info2['city'] = 'San Francisco'
band_info2['members'] = {}
band_info2['members']['drums'] = 'Wanda Day'
band_info2['albums'] = []
band_info2['albums'].append('Bigger, Better, Faster, More!')
# COMPLETE THIS...

if band_info1 == band_info2:
    print("Challenge 3 complete!")
else:
    print("Challenge 3 not yet done...")




print('Challenge 4 -------------')
# Challenge 4:
# Write a code that asks the user to enter a rock band. Then, use the
# dictionary to display the band's most famous song. HINT: Use "input" from
# previous activities.
# Optional: Make it into a while loop that keeps on asking, and "fails
# gracefully" if there is no band with that title

bands = {
    'Journey': "Don't Stop Believin'",
    'Bon Jovi': "Livin' On a Prayer",
    'Joy Division': 'Love Will Tear Us Apart',
    'Queen': 'Bohemian Rhapsody',
    '4 Non Blondes': "What's Up?",
    'Credence Clearwater Revival': "Fortunate Son",
}







print('-------------')
# Bonus Challenge:
# The Fibonacci Sequence are the numbers where every number after the first two
# is the sum of the two preceding ones. For example:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, etc.
# 1. Write a function that will calculate the nth Fibonacci number (where n is
# a parameter), and return that value.
# 2. Come up with a "test plan" for this function.
# 3. Use "assert" to test your code. Assert is for sanity checks in code.
#
# HINT: There are several distinct approaches to this. Get one working first
# before you think of others. One might use loops, another might use
# "recursion" (calling the same function within itself), and finally there is a
# way to approximate it using a formula.
# The formula for approximation is explained here:
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section1.2


