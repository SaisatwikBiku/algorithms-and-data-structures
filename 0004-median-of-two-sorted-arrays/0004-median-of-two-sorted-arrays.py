class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition for nums1
            j = half - i            # Partition for nums2

            # Get the boundary values
            nums1LeftMax = nums1[i - 1] if i > 0 else float('-inf')
            nums1RightMin = nums1[i] if i < m else float('inf')
            nums2LeftMax = nums2[j - 1] if j > 0 else float('-inf')
            nums2RightMin = nums2[j] if j < n else float('inf')

            # Check if partitions are valid
            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
                # If total length is odd, return the middle element
                if total % 2 == 1:
                    return min(nums1RightMin, nums2RightMin)
                # If total length is even, return the average of two middle elements
                return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
            
            # Adjust binary search range
            elif nums1LeftMax > nums2RightMin:
                right = i - 1
            else:
                left = i + 1