class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        count = 0
        maxlength = 0

        low = 0

        for high in range(1, len(nums)):

            if nums[high] - nums[low] == 1:
                count += 1
                low += 1

            else:
                maxlength = max(maxlength, count)
                count = 0
                low = high

        maxlength = max(maxlength, count)

        return maxlength + 1