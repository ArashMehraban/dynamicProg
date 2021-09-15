# Coin change problem:
# You are given a target amount and infinite bag of coins with different
# denominations. Choose minimum number of coins to make the target amount:
# e.g. [1,2,5], taget amount = 11
# Solution:
# First recursively:
# We assume as we go through the coin denominations, we can take as many
# number of instances of that coin, but once we pass it, we no longer can go back
# to the old coin denomination (to help recursion).
#
# Therefore, recursively, since from the begining we do not know the optimal
# solution, at each denomination, we include as many coins as we need to make
# the target amount. Consider coins = [1,2] and amount = 4
#
#
#                       1
#                      / \
#       back-track--> 1   2
#                    /\   /\
#     back-track--> 1  2  2
#                  / \ ...
#   back-track--> 1   2 <--back-track
#                /\
#               0 
#
# So to make 4, we can choose 1, then 1, and then 1 and then 1 again. From the
# 4th 1, we back-track to the 3rd 1 and see we also had the option to choose 2,
# but 2 + so far three 1's = 5, so we do not choose it. From there, we back-track
# to the 2nd 1 and notice we also could choose 2 and 2 + two 1's make 4. In
# comparison, (four 1's) and (two 1's plus a 2), indicates we should choose
# (two 1's plus a 2) since it is 3 coins versus 4 coins with (four 1's). Finally,
# we notice that every time that we include a coin we decrease the taget amount
# by the coin amount: e.g. new amount = old amount - coin[i]: 4-1= 3 or 4-2 = 2
# This idea recursively is presented:
#
#   add 1 coin
#     |
#     |       coins arr             ith elem            move to next denomiation
#     |           |                     |                              |
# min(1 + count(coins, amount - coin[i],i)   ,   count(coins, amount, i+1) )
#     |_____if include a coin____________|       |____if exclude a coin__|
#
#
#  Boundary cases:
#  1) No coins while amount > 0 => return inf (cannot make amount with no coins)
#
#  2) if amount = 0 => return 0 (do not include any coins)
#
#
#  So we notice larger problems depend on the solution of sub-structure problems
#  Therefore, we use dynamic programming:
#  Consider coins = [1,2,5] and amount = 6. 
#  We make tabel of size mem[#coins +1][amount+1]: mem[3+1][6+1] = mem[4][7]
#  1st row an col of teh mem table corresponds to the boundary case:
#                                
#                                  amounts (j)
#             ____0_______1______2_______3________4_____ 5________6____
#    (i)    0 |___0___|__inf__|__inf__|__inf__|__inf__|__inf__|__inf__|
#   coins   1 |___0___|_______|_______|_______|_______|_______|_______|
#           2 |___0___|_______|_______|_______|_______|_______|_______|
#           3 |___0___|_______|_______|_______|_______|_______|_______|
#
# Next (sub problems):
# at mem[i][j] indicates the minimum number of coins (i) to make amount j:
# Also, each cell in:
#        mem[i][j] = min(       include       ,   exclude   )
# So for mem[1][1] = min(1 + mem[1][0 =(1-1)] ,  mem[1-1][1])
#        mem[1][1] = min(1 +       0 ,              inf     ) = 1
#  Similarly:
#        mem[i][j] = min(       include       ,   exclude   )
# So for mem[1][2] = min(1 + mem[1][1 =(2-1)] ,  mem[1-1][2])
#        mem[1][2] = min(       2             ,     inf     ) = 2
# and
#        mem[i][j] = min(       include       ,   exclude   )
# So for mem[1][3] = min(1 + mem[1][2 =(3-1)] ,  mem[1-1][3])
#        mem[1][3] = min(       3             ,     inf     ) = 3
#
#If we go row by row, we have:
#
#
#                                  amounts (j)
#             ____0_______1______2_______3________4_____ 5________6____
#    (i)    0 |___0___|__inf__|__inf__|__inf__|__inf__|__inf__|__inf__|
#   coins   1 |___0___|___1___|___2___|___3___|___4___|___5___|___6___|
#           2 |___0___|___1___|___1___|___2___|___2___|___3___|___3___|
#           3 |___0___|___1___|___1___|___2___|___2___|___1___|___2___|
#
# So:         min(        include    ,  exclude   )
# mem[i][j] = min(1 + mem[i][j-coin[i-1]], mem[i-1][j])
#
def coin_change(coins,amount):
    #Allocate [len(coins)+1][amount+1] memoization table
    mem = [[None]*(amount+1) for _ in range(len(coins)+1)]
    # Populate first row with no coins and amount > 0
    for i in range(amount +1):
        mem[0][i] = float('inf')

    # populate first column with when amount = 0
    for i in range(len(coins)+1):
        mem[i][0] = 0

    for i in range(1,len(coins)+1):  #<-- Start from 1
        for j in range(1,amount+1): #<-- Start from 1
            if coins[i-1] > j: # exclude if amount < ith coin denomination
                mem[i][j] = mem[i-1][j]
            else:  # min(include or exlude) if amount >= ith coin denomination
                mem[i][j] = min(1 + mem[i][j - coins[i-1]],mem[i-1][j])

    if mem[-1][-1] == float('inf'):
        return -1
    else:
        return mem[-1][-1] 
    
if __name__ == "__main__":
    coins=[1,2,5]
    amount = 6
    print(coin_change(coins,amount)) # 2
    coins=[2,5,10]
    amount = 6
    print(coin_change(coins,amount)) # 3
    coins=[5,10]
    amount = 6
    print(coin_change(coins,amount)) # -1
