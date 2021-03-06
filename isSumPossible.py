# DP problem (is sum possible):
# For  given list of values, l, and a given sum, s, can we make produce s from
# the values in s?
#
# In order to be efficienet we need to use dynamic programmign (dp). It is easier
# to start with recursive (fall back) functions (which typically have exponential
# timing such as 2^n if n = len(l)):
#
# Recursively:
# isSum(l,n,s): <-- n = len(l)
#   if s == 0  <-- if sum(s) is zero
#       return True
#   if s != 0 and n == 0:
#       return False   <-- cannot make a sum(s) with no elements
#   if s < l[n-1]:
#       return isSum(l,n-1,s) <-- exlude l[n-1] elem if larger than s
#   if s > l[n-1]:  <-- if l[n-1] < s, either exclude it OR include it
#       return isSum(l,n-1,s) || isSum(l,n-1,s-l[n-1])
#                (exclude it)         (inlude it)
#
#
# The above is 2^n time. So lets us a table for DP:
#
# Note: DP table starts fron 0 to s and 0 to n (#elems in l),so:
#       DP is a (len(l)+1)-by-(s+1) table (as apposed to len(l)-by-s)
#
#           j = 0      1     2   ...      s
#             _______________________________
# i = #elems 0|_____|_____|_____|_____|_____|
#            1|_____|_____|_____|_____|_____|
#            2|_____|_____|_____|_____|_____|
#            .|_____|_____|_____|_____|_____|
#            .|_____|_____|_____|_____|_____|
#
#
#
# The first col is all True because we can make s=0 for any number of elems
# by simply excluing all elems
#
#           j = 0       1     2   ...      s
#             _______________________________
# i = #elems 0|_True_|_____|_____|_____|_____|
#            1|_True_|_____|_____|_____|_____|
#            2|_True_|_____|_____|_____|_____|
#            .|_True_|_____|_____|_____|_____|
#            .|_True_|_____|_____|_____|_____|
#
#
# The first row after the zeroth elem is all False because we cannot make s
# if list l is empty
#
#           j = 0       1         2     ...      s
#             ________________________________________
# i = #elems 0|_True_|_False_|_False_|_False_|_False_|
#            1|_True_|_______|_______|_______|_______|
#            2|_True_|_______|_______|_______|_______|
#            .|_True_|_______|_______|_______|_______|
#            .|_True_|_______|_______|_______|_______|
#
#
# Then the rest of table is populated with the same logic as the above
# recursive function in code bleow:
#
# Note: j's are the smaller sums (s =1,2,..s)
#       i's are number of elements
#
# ANSWER (True ot False) is at bottom-right corner DP[len(l)][s]
#
#
def isSumPossible(l,s):
    #Allocate a (len(l)+1)-by-(s+1) list of None's
    dp = [[None]*(s+1) for _ in range(len(l)+1)]
    #dp = [[None for x in range(s + 1)] for x in range(len(l) + 1)]
    # Populate the zeroth col with True
    for i in range(len(l)+1):
        dp[i][0] = True
    #Populate the zeroth row (except the zeroth elem in that row) with False 
    for i in range(1,s+1):
        dp[0][i] = False
    # for every i and j (number of elem and s) apply the recursive function above
    for i in range(1,len(l)+1):
        for j in range(1,s+1):
            if j < l[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= l[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j - l[i-1]])

    return dp[len(l)][s]

# DP problem (Partition equal subset sums):
# For  given list of integer values, l, and a given sum, s, can we partition l into two
# subsets that have equal sum of values?
#
# Note 1: This is Knapsack problem 0/1 type problem.
# Note 2: This is in essense the isSumPossible() function with extra simple constrains:
#         Constrains:
#            1) If the sum(l) == Odd then the answer is false since sum/2 won't be integer
#            2) Given the array find its summation and use summation/2
#
#
def equalSubsetSum(l):
    s = sum(l)
    if s & 1:  # <--- sum(l) == Odd 
        return False
    else:
        return isSumPossible(l,s//2)

# DP problem (count the number of subsets that sum to s in given list l)
# Note: This problem is the same as isSumPossible() problem (so read its logic first)
#        Small changes in that problem gives this:
#        1) Fill the dp table with 0 for False and 1 for True
#        2) In the recurvsive call:
#   if s > l[n-1]:  <-- if l[n-1] < s, either exclude it OR include it
#       return isSum(l,n-1,s) || isSum(l,n-1,s-l[n-1])
#                (exclude it)         (inlude it)
#
#       we want to use + instead of ||. Why? becasue we want the number of
#       subsets in all conditions, when we include an item or exlude it. So:
#
def countSubsets(l,s):
    #Allocate a (len(l)+1)-by-(s+1) list of None's
    dp = [[None]*(s+1) for _ in range(len(l)+1)]
    #dp = [[None for x in range(s + 1)] for x in range(len(l) + 1)]
    # Populate the zeroth col with 1
    for i in range(len(l)+1):
        dp[i][0] = 1
    #Populate the zeroth row (except the zeroth elem in that row) with 0 
    for i in range(1,s+1):
        dp[0][i] = 0
    # for every i and j (number of elem and s) apply the recursive function above
    for i in range(1,len(l)+1):
        for j in range(1,s+1):
            if j < l[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= l[i-1]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j - l[i-1]])
                
    return dp[len(l)][s]


# DP Problem (Minimum Subset Sum difference)
# Given an array l, partition l into two subsets such that the difference of the
# sums of each subset is minimum?
#
# Note: This is a Knapsack 0/1 type problem. It is a variaion of equalSubsetSum()
#       and isSumPossible() problems. equalSubsetSum() is the best case senario where
#       diff = 0. 
#       Things to consider:
#       1) s1 = sum(elems in subset 1)
#          s2 = sum(elems in subset 2)
#       2) if an elem is used in coputation of s1, then it is not used in s2, so:
#
#                 s1                     sum-s1 = s2
#          |-------------------------|-----------------|
#          <--------------------sum-------------------->
#
#        So, diff = abs((sum -s1) -s1) = sum - 2*s1
#        Therefore, we need to minimize sum - 2*s1 then.
#        So, imagine s1 <= s1. We ask under what condition s1 = s2? Ans: When
#        s2 (and s1) is equal to sum/2 (logic of equalSubsetSum() function):
#        Therefore: s1 < sum/2 and
#
#          0              sum/2           sum
#          |---------------------|---------------------|
#                        s1<------
#
#          so if we can find the best value for s1 and minimize diff = sum 2*s1,
#          we have the answer. Note that some values of sum may not be acheivable
#          and will be skipped.
#          So find all the poissible values of subset sum. That comes from the
#          logic of isSumPossible() problem.
#          That yields table below. Flase ones are the sums that cannot be made
#
#           j = 0       1         2     ...      s
#             ________________________________________
# i = #elems 0|_True_|_False_|_False_|_False_|_False_|
#            1|_True_|_______|_______|_______|_______|
#            2|_True_|___..__|__..___|__..___|__..___|
#            .|_True_|___..__|__..___|__..___|__..___|
#            .|_True_|_False_|_True__|_False_|_True__|
#
#          In the table above we are only interested in the last row becase
#          the last row values indicate all elements of array l are used.
#          In addition, we iterate through the last row (dp[len(l)][:]) up to sum/2.
#          (for i = 0 to sum/2 (not sum because we assumed s1 <= s2 = sum/2))
#          I) initialize: diff = sys.maxsize (python 3) or sys.maxint (python 2) 
#          II) While iteratating through the last row; 
#              first  <--- i     (which is s1)
#              second <--- sum-i (which is s2)
#          III) if dp[len(l)][i] is True (i,e that sum is possible to form)
#                    and
#                  diff > abs(first - second)
#               then (update minimum possible difference)
#                   diff = abd(first - second)
#
def MinSumDiff(l):
    s = sum(l)
    #Allocate a (len(l)+1)-by-(s+1) list of None's
    dp = [[None]*(s+1) for _ in range(len(l)+1)]
    # Populate the zeroth col with True
    for i in range(len(l)+1):
        dp[i][0] = True
    #Populate the zeroth row (except the zeroth elem in that row) with False 
    for i in range(1,s+1):
        dp[0][i] = False
    # for every i and j (number of elem and s) apply the recursive function above
    for i in range(1,len(l)+1):
        for j in range(1,s+1):
            if j < l[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= l[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j - l[i-1]])
    import sys
    diff = sys.maxsize
    for i in range(s//2+1):
        first = i
        second = s - i
        if dp[len(l)][i] == True and diff > abs(first - second):
            diff = abs(first - second)
    return diff


if __name__ == "__main__":
    l=[3,34,4,12,5,2]
    s = 9
    print(isSumPossible(l,s))
    #True
    print('-----------------')
    l = [12,5,7,4,4]
    print(equalSubsetSum(l))
    #True
    print('-----------------')
    print(countSubsets(l,12))
    #2
    l = [12,5,7,4,4,1]
    print('-----------------')
    print(MinSumDiff(l))
    #1
    
    

