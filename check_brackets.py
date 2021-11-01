# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            opening_brackets_stack.append(next)
            if ((are_matching(opening_brackets_stack[len(opening_brackets_stack) - 2], opening_brackets_stack[len(opening_brackets_stack)-1]))):
                opening_brackets_stack = opening_brackets_stack[:len(opening_brackets_stack) - 2]
    if opening_brackets_stack == []:
        return True
    else:
        return False

def main():
    print(find_mismatch(input()))


if __name__ == "__main__":
    main()