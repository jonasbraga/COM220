import copy
import time
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

def quickSort(array, start, end):
  if start >= end:
    return

  p = partition(array, start, end)
  quickSort(array, start, p-1)
  quickSort(array, p+1, end)

def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
          arr[j], arr[j+1] = arr[j+1], arr[j]

def fillNumbersArray(arrayLength = 10000):
  numbersList = []
  for i in range(arrayLength): 
    numbersList.append(random.randrange(1, 100000))
  return numbersList

def execQuickSort(numbersList):
  inicioQuickSort = time.time()
  quickSort(numbersList, 0, len(numbersList) - 1)
  fimQuickSort = time.time()
  elapsedTime = inicioQuickSort - fimQuickSort
  return elapsedTime

def execBubbleSort(numbersList):
  inicioBubbleSort = time.time()
  bubbleSort(numbersList)
  fimBubbleSort = time.time()
  elapsedTime = inicioBubbleSort - fimBubbleSort
  return elapsedTime

def main():
  print("\nAguarde enquanto o array é ordenado...\n")
  numbersListQuick = fillNumbersArray()
  numbersListBubble = copy.copy(numbersListQuick)
  print("Quick sort: {} s".format(execQuickSort(numbersListQuick)))
  print("Bubble sort: {} s".format(execBubbleSort(numbersListBubble)))
  
main()
