import random

class RandomizedSet(object):

    def __init__(self):
        self.values_dict = {}
        self.values_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.values_dict:
            return False
        else:
            self.values_dict[val] = len(self.values_list)
            self.values_list.append(val)

            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.values_dict:
            return False
        else:
            index = self.values_dict[val]
            last_value = self.values_list[-1]

            self.values_dict[last_value] = index
            self.values_list[index] = last_value

            self.values_list.pop()
            del self.values_dict[val]

            return True

    def getRandom(self):
        """
        :rtype: int
        """

        value = random.choice(self.values_list)

        return value



        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()