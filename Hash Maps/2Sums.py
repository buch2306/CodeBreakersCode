class Solution:

    def twoSum(self, nums, target):
        t = {}
        potentialsum = 0
        for c,k in enumerate (nums):
            potentialsum = target - k
            if potentialsum in t:
                return [t[potentialsum],c]
            else: 
                t[k] =c
        
        
    
