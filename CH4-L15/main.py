def quick_sort(nums, low, high):
  if low < high:
    middle = partition(nums, low, high)
    quick_sort(nums, low, middle - 1)
    quick_sort(nums, middle + 1, high)


def partition(nums: list, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
      if nums[j] < pivot:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[high], nums[i + 1] = nums[i + 1], nums[high]
    return i + 1
