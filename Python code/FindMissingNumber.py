def findmissing(nums):
  nums.sort()
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return i + 1
  return len(nums) + 1

nums = [1,2,4,3,6,7,8,9]
print(findmissing(nums))
    