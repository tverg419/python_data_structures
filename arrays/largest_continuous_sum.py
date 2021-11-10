'''
Given an array of integers(positive and negatives), find the largest continuous sum
'''

def largest_continuous_sum(arr):
    
    start = 0
    end = 1
    max_sum = current_max = arr[0]
     
    for num in arr[1:]:

        current_max = max(current_max + num, num)

        max_sum = max(current_max, max_sum)
    
    return max_sum

if __name__ == '__main__':

    print(largest_continuous_sum())