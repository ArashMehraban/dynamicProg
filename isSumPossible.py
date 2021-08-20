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

if __name__ == "__main__":
    l=[3,34,4,12,5,2]
    s = 9
    print(isSumPossible(l,s))
    #True