# Fractional Knapsack

def fractional_knapsack(values:list, weight:list, c:int)->float:
  N = len(values)
  items = [[weight[i],values[i]] for i in range(N)]
  #sort the items on value
  items.sort(reverse=True,key=lambda x:x[1]/x[0])
  total_value = 0.0
  current_w = 0
  for item in items:
    w,v = item[0],item[1]
    if current_w + w <= c:
      total_value += v
      current_w += w
    else:
      total_value += v*((c-current_w)/w)
      break
  return total_value
values = [60,100,120]
weights = [10,20,30,]
c = 50
fractional_knapsack(values,weights,c)