# Pattern Recognition using RegEx

import re  # Where re is the RegEx Module

# Function to see if string contains a single letter (Simple Pattern)
def findLetter(str1):
    found = re.search(r'P', str1)  # this creates a re.Match object
    # r'P' where any instance of 'P' is enough to satisfy the match
    if(found):
        print("P is in " + str1)
    else:
        print("P is NOT in " + str1)

# Function to allow for passing target as a parameter
def findPattern(pattern, str1):
    found = re.search(pattern, str1)  # this creates a re.Match object
    if(found):
        print(pattern + " is in " + str1)
    else:
        print(pattern + " is NOT in " + str1)

# Example where we are testing the formatting for a SSN
def isSSN(str):
    found = re.search(r'\d\d\d-\d\d-\d\d\d\d', str) # '\d' denotes a digit, where '-' denotes itself
    if found:
        print(str, 'contains a social security number.')
    else:
        print(str, 'does NOT contain a social security number.')

# Introducing boundaries '\b', and '$' for matching the start and end of the string respectively
def findBoundaryCondition(str):
    found1 = re.search(r'\bthe', str)   # this checks to see if
    found2 = re.search(r'ing\b', str)
    found3 = re.search(r'\bhat\b', str)
    if found1:
        print(str, 'has "the" at the start of a word.')
    if found2:
        print(str, 'has "ing" at the end of a word.')
    if found3:
        print(str, 'has the word "hat" in it.')

# Introducing Repetition in various forms

# ^ starting at the beginning of the string,
# \w+ look for one or more word characters
# ,? followed by an optional comma (zero or one commas)
# \s* zero or more spaces
# [A-Z] and a capital letter
# $ which must be at the end of the string.
def lastNameFirstInitial(str):
    found = re.search(r'^\w+,?\s*[A-Z]$', str)
    if found:
        print(str, 'contains the pattern.')
    else:
        print(str, 'does NOT contain the pattern.')

# Function very similar to above, but introduces grouping denoted by '()'
def validName(str):
    found = re.search(r'^(\w+)(,?\s*[A-Z])?$', str)
    if found:
        print('Pattern match results: \n')
        print('whole match:      |', found.group(0), '|', sep='')
        print('first set of ():  |', found.group(1), '|', sep='')
        print('second set of (): |', found.group(2), '|', sep='')
    else:
        print(str, 'does not contain the pattern.')

# Introducing re.findall, returns all objects pertaining to the pattern instead of just the first one
def findAllPattern(message):
    result = re.findall(r'([A-Z]-?\d)', message)
    if result:
        for item in result:
            print(item)
    else:
        print('findall() did not find any matches to the pattern.')



### MAIN ###
str1 = "Pineapple"
findLetter(str1)

pattern1 = r'P.n' # r'P.n' = where P is followed by any character followed by n
findPattern(pattern1, str1)

pattern2 = r'P[aeiou]n' # r'P[aeiou]n' = where 'P' is followed by any of the -
                        # - characters within the "[]", followed by an 'n'            
findPattern(pattern2, str1)

pattern3 = r'P[^aeiou]n' # r'P[aeiou]n' = where 'P' is followed by NONE of the -
                         # - characters within the "[^]", followed by an 'n'            
findPattern(pattern3, str1)

isSSN('301-22-0156')     # Checking to see if valid formatting of SSN
isSSN('301-555-1212')
isSSN('SSN is 562-99-6713')

findBoundaryCondition("cat in a hat")      # checking if 'hat' is in the string
findBoundaryCondition("the cat in a car")  # does the string starts with 'the'
findBoundaryCondition("cat is dancing")    # does the string end with 'ing'

# see function for implementation 
lastNameFirstInitial('Smith, J')    # Is this a last name followed by a first initial
lastNameFirstInitial('M Cano')
lastNameFirstInitial('nguyen C')

validName('Smith, J')   # same as above but with grouping functionality
validName('Madonna')
validName('Morgan D')

message = 'Insert tabs B3, D-7, and C6 into slot A9.' 
# Will extract any occurrence of [A-Z] attached to a [1-9], with an optional "-"
findAllPattern(message)
