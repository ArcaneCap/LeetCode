'''
There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
'''

def finalValueAfterOperations(operations: list[str]) -> int:
    X = 0

    for op in operations:
        if op in ['++X', 'X++']:
            X +=1
        elif op in ['--X','X--']:
            X -=1

    return X


# Expected out : 1
print(finalValueAfterOperations(operations = ["--X","X++","X++"]))

# Expected out: 3
print(finalValueAfterOperations(operations = ["++X","++X","X++"]))

# Expected out: 0
print(finalValueAfterOperations(operations = ["X++","++X","--X","X--"]))