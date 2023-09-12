'''
You are given an m x n integer grid accounts where accounts[i][j] 
is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
'''

def maximumWealth(accounts: list[list[int]]) -> int:
    return max(sum(account) for account in accounts)

# Exp. out: 6
print(maximumWealth(accounts = [[1,2,3],[3,2,1]]))

# Exp. out: 10
print(maximumWealth(accounts = [[1,5],[7,3],[3,5]]))

# Exp. out: 17
print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))