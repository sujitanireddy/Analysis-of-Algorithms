#Reference -> https://neetcode.io/courses/advanced-algorithms/0
"""
The motivation behind this algorithm is for solving questions like - finding maximum subarray product or sum.
Example: https://neetcode.io/problems/maximum-subarray/question?list=neetcode150

The brute force way would be just go through all the possible subarray's using a double loop and keep track of the max sum, however
that solution is going to be O(n**2) time complexity and Kadnaes algorithm solves that in O(n) time.

The intuition behind the algorithm is very simple
- If all elements in the array are positive, the maximum sum subarray is the entire array.
- If we ever have a negative sum subarray, that's the case we want to avoid.

Example:
              [1,-3,7]
running sum =  1,-2  -> At this point is there a reason we should add -2 to 7? Because it's not going to yield us max sum anyway? So just ignore it
and start from 7. 

Another counter example is:
              [6, -2, 7]
running sum =. 6,  4, 11 -> here it's worth adding the -2 as it's giving us better max sum at the end.

So the core idea is if we encounter a -ve sum subarray, ignore it and start the sum from the new value.
"""

#Bruteforce 
#TC: O(n**2)
def bruteforce(nums:list) -> int:

    max_sum = float("-inf")

    for i in range(len(nums)):
        curr_sum = 0

        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum


#Kadanes Algorithm
#TC: O(n)
def kadanes(nums:list) -> int:

    curr_sum = 0
    max_sum = float("-inf")

    for num in nums:

        curr_sum = max(curr_sum, 0)
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum


#Sliding Window Kadanes -> When we are asked to return the positions of the array
#TC: O(n)
def kadanes_sliding_window(nums:list) -> int:

    L = 0
    maxL, maxR = 0, 0
    curr_sum = 0
    max_sum = float("-inf")

    for R in range(len(nums)):

        if curr_sum < 0:
            curr_sum = 0
            L = R

        curr_sum += nums[R]

        if curr_sum > max_sum:
            maxL, maxR = L, R
            max_sum = curr_sum

    return [maxL, maxR]

print(kadanes_sliding_window([6,-20,7]))



