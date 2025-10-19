def merge_sort(nums: list):
  if (len(nums) < 2):
    return nums
  first_half, second_half = nums[:len(nums) // 2], nums[len(nums) // 2:]
  sorted_first_half = merge_sort(first_half)
  sorted_second_half = merge_sort(second_half)
  return merge(sorted_first_half, sorted_second_half)


def merge(first: list, second: list):
    final, j, i = [], 0, 0
    while i < len(first) and j < len(second):
      if first[i] <= second[j]:
        final.append(first[i])
        i += 1
      else:
        final.append(second[j])
        j +=1
    while i < len(first):
      final.append(first[i])
      i +=1
    while j < len(second):
      final.append(second[j])
      j +=1
    
    return final
