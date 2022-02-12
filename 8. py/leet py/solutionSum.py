class Solution:
    def twoSum(self, nums , target):
        self.nums = nums
        self.target = target
        
        for x in enumerate(nums):
            for y in enumerate(nums):
                
                if (x[1] + y[1] == target) and( x[0] != y[0]):
                    
                    return [x[0], y[0]]


ts = Solution()


list_ = [2,7,5,11, 15]
sum_ = 9

idx = ts.twoSum(list_, sum_)


print(f'the index is : {idx}')