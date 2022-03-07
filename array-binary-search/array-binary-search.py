
import math 



# def binary_search(arr, key):
#     while len(arr) > 0:
#         try:
#             middle = len(arr)//2

#             if arr[middle] == key:
#                 return middle
#             if arr[middle] > key:
#                 binary_search( arr[:middle], key)
#             if arr[middle] < key:
#                 binary_search(arr[middle:], key)
#         except IndexError:
#             return -1

#     return -1



def BinarySearch(array, key): # key is what we want to find the index for 
  array.sort() 
  low = 0
  high = len(array)
  while len(array) > 0:
    middle = math.floor((low+high) // 2)
    if array[middle] == key:
      return middle
    if array[middle] < key:
      low= middle
    if array[middle] > key:
      high= middle
    if middle == 0 or middle == len(array) - 1:
      return -1
  return -1

