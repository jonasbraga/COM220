import random 


def partition(array, start, end):
  pivot = array[start]
  low = start + 1
  high = end
  while True:
    while low <= high and array[high] >= pivot:
      high = high - 1
    
    while low <= high and array[low] <= pivot:
      low = low + 1
    
    if low <= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  
  array[start], array[high] = array[high], array[start]
  return high

def quick_sort(array, start, end):
  if start >= end:
    return

  p = partition(array, start, end)
  quick_sort(array, start, p-1)
  quick_sort(array, p+1, end)

numbersList = []

for i in range(10000): 
  numbersList.append(random.randrange(1, 10000))

print(numbersList)
quick_sort(numbersList, 0, len(numbersList) - 1)
print(numbersList)
