#0/1 Knapsack Algorithm (Dynamic Programming)
#Reference -> https://neetcode.io/courses/advanced-algorithms/18

"""
Q: Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that can be contained in the backpack. 
The i-th item's profit is profit[i] and it's weight is weight[i]. 
Assume you can only add each item to the bag at most one time.

Sol:      0 1 2 3                                         
profit=  [4,4,7,1]        
weights= [5,2,3,1]
capacity = 8

1st branch recurrence relation (choosing the weight at i): f(i) = f(i+1, (capacity - weights[i]) (profit + profit[i]))
2nd branch recurrence relation (not choosing): f(i) = f(i+1, capacity, profit)

base cases:
- before choosing: validate if the capacity will be greater than 0 if choosing else return back
                                                    
"""

#Brute Force
def max_profit(profits, weights, capacity) -> int:

    def recurse(i, profit, cap):

        if i >= len(profits):
            return profit

        res_choosing = 0 #default value if the first branch never executed in our recursive call

        #choose the value at i if we have enough capacity
        if cap - weights[i] >= 0:
            res_choosing = recurse(i+1, profit + profits[i], cap - weights[i])

        #dont choose value at i
        res_not_choosing = recurse(i+1, profit, cap)
    
        return max(res_choosing, res_not_choosing)

    return recurse(0,0,capacity)

print(max_profit(profits=[4,4,7,1], weights=[5,2,3,1], capacity = 8))