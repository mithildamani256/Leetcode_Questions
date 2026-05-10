class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)

            

#  go over each index, check its neighbours if they exist, if value is greater , then look at preceeding neighbour to see no of candies, and assign + 1 




        
# {1,4,3,6}
# 1 -> assign it 1 
# 4 -> assign it 2
#  3 -> assign it 1
#  6 -> assign it 2

# {1,2,2}
# 1 -> assign it 1
# 2 -> assign it 2 
#  2 -> assign it 1

# {3,1,0}
# 3 -> assign it 2
# 1 -> assign it 3
#  0 -> assign it 1