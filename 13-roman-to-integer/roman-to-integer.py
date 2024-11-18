class Solution(object):
    def romanToInt(self, s):

        dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "IX" : 9, "IV" : 4, "XC" : 90, "XL" : 40, "CD" : 400, "CM" : 900}

        i = 0
        ans = 0

        while i < len(s):
            if i != len(s) - 1:
                if s[i] + s[i+1] in dict:
                    ans += dict[s[i] + s[i+1]]
                    i += 2
                else:
                    ans += dict[s[i]]
                    i += 1
            else:
                ans += dict[s[i]]
                i += 1 

        return ans

        # roman_vals = []

        # for val in s:
        #     if(val == 'I'):
        #         roman_vals.append(1)
        #     elif(val == 'V'):
        #         roman_vals.append(5)
        #     elif(val == 'X'):
        #         roman_vals.append(10)
        #     elif(val == 'L'):
        #         roman_vals.append(50) 
        #     elif(val == 'C'):
        #         roman_vals.append(100) 
        #     elif(val == 'D'):
        #         roman_vals.append(500)  
        #     else:
        #         roman_vals.append(1000)
        
        # total_value = 0
        # counter = False
    
        # for i in range(len(roman_vals)):
        
        #     if(counter == True):
        #         counter = False;
        #         continue;
            
        #     if(roman_vals[i] == 1):
        #         if(i+1 < len(roman_vals) and (roman_vals[i+1] == 10 or roman_vals[i+1] == 5)):
        #             total_value += roman_vals[i+1] - roman_vals[i]
        #             counter= True
        #         else:
        #             total_value += 1
            
        #     elif(roman_vals[i] == 10):
        #         if(i+1 < len(roman_vals) and (roman_vals[i+1] == 50 or roman_vals[i+1] == 100)):
        #             total_value += roman_vals[i+1] - roman_vals[i]
        #             counter= True 
        #         else:
        #             total_value += 10
                
        #     elif(roman_vals[i] == 100):
        #         if(i+1 < len(roman_vals) and (roman_vals[i+1] == 500 or roman_vals[i+1] == 1000)):
        #             total_value += roman_vals[i+1] - roman_vals[i]
        #             counter= True
        #         else:
        #             total_value += 100
                
        #     else:
        #         total_value += roman_vals[i]

        # return total_value


