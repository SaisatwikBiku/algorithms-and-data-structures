class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {} #index, value

        for index, value in enumerate(nums):

            if target - value in hash_map:
                return index, hash_map[target-value]
            else:
                hash_map[value] = index   