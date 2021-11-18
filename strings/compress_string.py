def compress(s):
    # Create a dict that holds the number of occurences of each letter
    output = ''
    current = s[0]
    count = 0

    for letter in s:
        if letter != current:
            output += current
            output += str(count)
            current = letter
            count = 1
        else:
            count += 1

    output += current
    output += str(count)

    return output

if __name__ == "__main__":
    data = input('Enter a String:\n')
    print(compress(data))