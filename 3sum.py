from typing import List


class Solution:
    def three_sum(self, nums):
        nums.sort()  # Sort the numbers first
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip the same element to avoid duplicates
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip the same element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip the same element
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets

nums = [-1,0,1,2,-1,-4]
nums_list = Solution().three_sum(nums)
print(nums_list)
