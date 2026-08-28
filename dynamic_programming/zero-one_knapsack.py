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
#TC : O(2 ** n)
#SC : O(n)
def brute_force(profits, weights, capacity) -> int:

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



#Top Down Memoization
#TC : O(n * m)
#SC : O(n * m)
def top_down(profits, weights, capacity) -> int:

    cache = {}

    def recurse(i, cap):

        if i == len(profits):
            return 0

        if (i,cap) in cache:
            return cache[(i, cap)]

        cache[(i,cap)] = recurse(i+1,cap)

        if cap - weights[i] >= 0:
            p = profits[i] + recurse(i+1, cap - weights[i])
            cache[(i,cap)] = max(p, cache[(i,cap)])

        return cache[(i,cap)]

    return recurse(0,capacity)



#Bottom Up: DP solution
#Reference -> https://www.youtube.com/watch?v=8LusJS5-AGo & https://neetcode.io/courses/advanced-algorithms/18
#Reference image of your dry run to understand -> dynamic_programming/zero-one_knapsack.heic
#TC : O(n * m)
#SC : O(n * m)

"""
We build a table ranging from 0 - capacity as columns and the weights(items) as rows.

The reason we are looking above one row is that this is 0/1 knapsack (We can only choose the item ONCE!), so when we are in the include branch we already chose the item, so we have to compute what was the best with the 
capacity remaining, but surprise we already have it computed in the row above. Just use it. That is the core intuition.

We fill up the table from left to right and the answer is going to land at the bottom corner

Profit Weight   idx 0  1  2  3  4  5  6  7  8
  4       5      0 [0, 0, 0, 0, 0, 4, 4, 4, 4]
  4       2      1 [0, 0, 4, 0, 0, 0, 0, 0, 0]
  7       3      2 [0, 0, 0, 0, 0, 0, 0, 0, 0]
  1       1      3 [0, 0, 0, 0, 0, 0, 0, 0, 0]

The answer simply drops down to - Do we skip or do we have enough capacity to include? 
"""

def bottom_up(profits, weights, capacity):

    #build the matrix
    ROWS = len(weights) #weights
    COLS = capacity + 1 #capacity ranging from 0 - capacity
    matrix = [[0] * COLS for i in range(ROWS)]

    #initialize the first column
    for c in range(COLS):
        if c >= weights[0]:
            matrix[0][c] = profits[0]

    #Dp logic
    for r in range(1, ROWS):
        for c in range(1, COLS):

            skip = matrix[r-1][c] #if the item is being skipped the best answer will lie without choosing item on the above row

            include = 0

            if c >= weights[r]: #do we have enough capacity to include the weight? 
                include = profits[r] + matrix[r-1][c - weights[r]] #if more capacity is remaining then lookup what was the best profit at that remaining capacity

            matrix[r][c] = max(skip, include)

    return matrix[ROWS-1][COLS-1]


#Bottom Up: DP solution with space optimization. Using only two array's through out instead of the whole matrix.
#TC: O(n*m)
#SC: O(m)
def bottom_up_space_optimized(profits, weights, capacity):

    #build the matrix
    ROWS = len(weights) #weights
    COLS = capacity + 1 #capacity ranging from 0 - capacity
    matrix = [[0] * COLS for i in range(2)]

    #initialize the first column
    for c in range(COLS):
        if c >= weights[0]:
            matrix[0][c] = profits[0]

    #Dp logic
    for i in range(1, ROWS):
        for c in range(1, COLS):

            skip = matrix[0][c] #if the item is being skipped the best answer will lie without choosing item on the above row

            include = 0

            if c >= weights[i]: #do we have enough capacity to include the weight? 
                include = profits[i] + matrix[0][c - weights[i]] #if more capacity is remaining then lookup what was the best profit at that remaining capacity

            matrix[1][c] = max(skip, include)

        matrix[0] = matrix[1].copy()

    return matrix[1][COLS-1]

print(bottom_up_space_optimized(profits=[4,4,7,1], weights=[5,2,3,1], capacity = 8))


"""
Approach	                     TC	     SC
Brute Force	                   O(2ⁿ)	O(n)
Top-Down Memoization	       O(n·m)	O(n·m)
Bottom-Up (full table)	       O(n·m)	O(n·m)
Bottom-Up (space optimized)	   O(n·m)	O(m)
"""