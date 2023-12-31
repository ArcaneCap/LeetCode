'''
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    most_candies = []

    for i in candies:
        if i + extraCandies >= max(candies):
            most_candies.append(True)
        else:
            most_candies.append(False)
    
    return most_candies


# Expected out: [true,true,true,false,true] 
print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))

# Expected out: [true,false,false,false,false]
print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))

# Expected out: [true,false,true]
print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))