'''
Given an integer array, output all the  unique pairs that sum up to a specific value k
Input:
[1, 3, 2, 2], 4
Output:
[[1, 3], [2, 2]]
'''

def array_pair_sum(arr, target):
    # stores the value of numbers already scanned
    seen = set()
    output = set()

    for num in arr:
        # set the pair to be the targer minus the pair and see if the pair is already in the seen set
        pair = target - num

        if pair in seen:
            output.add( (min(num, pair), max(num, pair)))
        else:
            seen.add(num)

    return seen, output


print(array_pair_sum([1, 3, 2, 2, 5, -1], 4))