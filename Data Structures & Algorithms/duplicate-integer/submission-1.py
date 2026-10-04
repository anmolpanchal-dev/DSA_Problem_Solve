class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        if len(nums) != len(freq):
            return True

        return False