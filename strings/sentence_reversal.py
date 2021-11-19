'''
Given a string of words, reverse all the words. You should remove all leading and 
trailing whitespace so only the words appear in the result

'''
def sentence_reversal(s):
    # Clean the string by removing any leading/trailing whitespace
    # have a for loop that runs through the entire string
    #   if we encounter a whitespace, that indicates a new word
    output = ''
    current = ''
    s = s.strip()

    for letter in s:
        if letter == ' ':
            output = current + " " + output
            current = ''
        else:
            current += letter
    output = current + " " + output

    return output

if __name__ == '__main__':
    data = input()
    print(sentence_reversal(data))