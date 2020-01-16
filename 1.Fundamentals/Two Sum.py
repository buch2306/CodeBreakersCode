class Solution:

    def twoSum(self, nums, target):

        s = [] #declaring an empty list that will have indices
        
        for i in range(0,len(nums)): #iterating through the list, choosing pivot

            j = i+1 #incrementing the pivot and storing it in j
            
            for j in range(j, len(nums)): # checking against each element that comes after pivot
                
                if nums[i]+nums[j] ==target: # checking if the values sum up to target
                    s.append(i) #appending indices to the list
                    s.append(j)
                    return s # returning the list with indices