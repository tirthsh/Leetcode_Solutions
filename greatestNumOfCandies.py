# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                candies[i] = True
            else:
                candies[i].append(False)

        return candies