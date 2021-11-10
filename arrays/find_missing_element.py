'''
Consider an array of non-negative integers. A second array is a randomixed version of the first with one element removed. Given these two arrays, find the missing element.
Input:
[1, 2, 3, 4, 5]
[3, 2, 1, 5]

Output:
4
'''

def find_missing_element(arr1, arr2):
    
    arr1.sort()
    arr2.sort()

    for i in range(max(len(arr1),len(arr2))):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return -1

print(find_missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))