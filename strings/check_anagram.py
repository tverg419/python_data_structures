'''
Given two strings check to see if they are anagrams.
Anagram: two words written using the same exact letters
Ex: "bat" "tab"
Note: ignore spaces and capitalizations
'''

def check_anagram(s1, s2):

    # clean strings
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # create a dictionary for s1 that contains letters as keys and counts as values
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # remove values as they appear in s2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False
    # loop through count dict to see if there are any non zero values
    for letter in count:
        if count[letter] != 0:
            return False
    return True

string1 = "112"
string2 = "211"

print(check_anagram('go go go','gggooo'))
print(check_anagram('abc','cba'))
print(check_anagram('hi man', 'hi       man'))
print(check_anagram('aabbcc','aabbc'))
print(check_anagram('123','132'))
