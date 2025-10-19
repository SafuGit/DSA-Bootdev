def exponential_growth(n, factor, days):
  growth_list = [n]
  current = 0
  for i in range(0, days):
    current = growth_list[i] * factor
    growth_list.append(current)
  return growth_list

print(exponential_growth(10, 2, 4))