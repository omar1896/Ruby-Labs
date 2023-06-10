#! python3
# print ("sds")
from ast import List


def twoSum( nums, target):
        for num in nums:
            rand=target-num
            if rand in nums:
                if num==rand:
                    num_redundency=nums.count(rand)
                    if num_redundency>1:
                        last = len(nums) - nums[::-1].index(num) - 1
                        print(last)
                        return [nums.index(num),last]
                elif  nums.index(num) != nums.index(rand):
                    nums.index(rand)
                    return [nums.index(num),nums.index(rand)]
            else:
                 continue     
                        
                     
                            
                          


                               
                          
li=[3,3]
n=6
x=twoSum(li,n)
print (x)