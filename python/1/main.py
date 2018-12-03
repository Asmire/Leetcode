# 3 lines Brute Force
def twoSum(self, nums, target):
    for i in range(len(nums)):
        if ((target - nums[i]) in nums[i+1:]):
            return i,nums[i+1:].index(target-nums[i])+i+1

# enumerate
def twoSum(self, nums, target):
    for i,elements in enumerate(nums):
        if (target - element) in dic:
            return [dic[target - element],i]
        dic[element] = i
#O(n)
def twoSum(self, nums, target):
    store = dict()
    for i in range(len(nums)):
        search  = target - nums[i]
        if search in store:
            return [store[search],i]
        else:
            store[nums[i]] = i
    return 0
                  
