class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
            nums.sort()
            best = nums[0] + nums[1] + nums[2]

            for i in range(len(nums)-2):
                left = i+1
                right = len(nums)-1

                while left < right:
                    s = nums[i]+nums[left]+nums[right]


                    if abs(s - target) < abs(best - target):
                        best = s

                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        return s

            return best
                                     