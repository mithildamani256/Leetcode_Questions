class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # max_val = 0
        # count = 0
         
        # for i in range(len(citations)):
        #     value = citations[i]
        #     for j in range(len(citations)):
        #         if(citations[j] >= value):
        #             count = count + 1
            
        #     if(min(count,value) > max_val):
        #         max_val = min(count,value)
            
        #     count = 0
        

        # return max_val

        dict = {}

        citations.sort()

        for i in citations:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            

            for j in dict:
                if j < i:
                    dict[j] += 1

        print(dict)
        max_v = 0

        for key in dict.keys():
            if max_v < min(key, dict[key]):
                max_v = min(key, dict[key])

        return max_v

            