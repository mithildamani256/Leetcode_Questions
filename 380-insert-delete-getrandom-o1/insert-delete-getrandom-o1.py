class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.set = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.dict:
            return False
        
        length_set = len(self.set)
        self.dict[val] = length_set

        self.set.append(val)
        
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.dict:
            return False
        
        index_val = self.dict[val]
        last_set_element = self.set[-1]

        self.set[index_val] = last_set_element
        self.set.pop()

        self.dict[last_set_element] = index_val
        del self.dict[val]

        return True
        
#  list = [3,4,1,2]
#  dict = {3:0, 4:1, 2:3, 1:2}

# 5 so for that 
#  step 1 -> find index of 5 in dict (2), the last element in list (1)
#  step 2 -> at index 2, put 1. and then delete last index from list and update 1 in dict to habve2 and delete the key 5. 
        

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()