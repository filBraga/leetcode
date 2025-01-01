# Sorting - O(nlogn)
def hasDuplicate(self, nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return True
    return False

# Set - O(n)
def hasDuplicateAlternative(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False