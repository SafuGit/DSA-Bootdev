def power_set(input):
  if len(input) == 0:
    return [[]]
  else:
    all_subsets = [[]]
    for elem in input:
      new_subsets = []
      for subset in all_subsets:
        subset_copy = subset
        subset_copy = new_subsets + [elem]
        new_subsets.append(subset_copy)
      all_subsets.append(new_subsets)
    return all_subsets
