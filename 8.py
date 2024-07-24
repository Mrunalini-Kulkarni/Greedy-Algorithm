# Shop in a Candy Store

def candy_store(candies:list[int],k:int)->tuple[int,int]:
  N = len(candies)
  candies.sort()
  #compute min price
  min_p = 0
  buy = 0
  free = N-1
  while buy<=free:
    min_p += candies[buy]
    buy += 1
    free -= k
  #compute max price
  max_p = 0
  buy = N-1
  free = 0
  while buy>=free:
    max_p += candies[buy]
    buy -= 1
    free += 1
  return min_p,max_p
candies = [3,2,1,4]
k = 2
candy_store(candies,k)