'''
Given a string, check if all of the characters in the string are unique.
Return true if all characters are unique, else return false
'''

def unique_characters(s):
    
    seen = []

    for letter in s:
        if letter in seen:
            return False
        else:
            seen.append(letter)
    return True

if __name__ == '__main__':
    data = input('Enter a String: \n')
    print(unique_characters(data))