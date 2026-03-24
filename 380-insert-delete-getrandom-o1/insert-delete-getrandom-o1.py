class RandomizedSet(object):

    def __init__(self):
        self.values = []
        self.values_mapping = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.values_mapping:
            return False
        
        length = len(self.values)
        self.values.append(val)
        self.values_mapping[val] = length

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.values:
            return False

        val_index = self.values_mapping[val]

        last_value = self.values[-1]
        self.values[val_index] = self.values[-1]
        self.values.pop()

        self.values_mapping[last_value] = val_index
        del self.values_mapping[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.values)
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# [1,3] {1:0, 3:1} ,,,,,, remove(2), val_index = 1, last_index = 2