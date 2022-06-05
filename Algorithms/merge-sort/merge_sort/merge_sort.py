
def Mergesort(list):

    array_length = len(list)
    if array_length > 1:
        mid = array_length // 2
        left = list[0:mid]
        right = list[mid:]
        Mergesort(left)
        Mergesort(right)
        merge(left, right, list)
    return list
        
def merge(left,right,list):
    """
        Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer. 
        Merge sort repeatedly breaks down a list into several sublists
        until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list.
    """
    
    count1 = 0
    count2 = 0
    count3 = 0
    while count1 < len(left) and count2 < len(right):
        if left[count1] <= right[count2]:
            list[count3] = left[count1]
            count1 += 1
        else:
            list[count3] = right[count2]
            count2 += 1
        count3 += 1
    while count1 < len(left):
        list[count3] = left[count1]
        count1 += 1
        count3 += 1
    while count2 < len(right):
        list[count3] = right[count2]
        count2 += 1
        count3 += 1   
    



# merge function take two intervals
# one from start to mid
# second from mid+1, to end
# and merge them in sorted order
# def merge(Arr, start, mid, end) :

#         # create a temp array
#         temp[] = [0] * (end - start + 1)

#         # crawlers for both intervals and for temp
#         i, j, k = start, mid+1, 0

#         # traverse both lists and in each iteration add smaller of both elements in temp 
#         while(i <= mid and j <= end) :
#             if(Arr[i] <= Arr[j]) :
#                 temp[k] = Arr[i]
#                 k += 1; i += 1
#             else :
#                 temp[k] = Arr[j]
#                 k += 1; j += 1

#         # add elements left in the first interval 
#         while(i <= mid) :
#             temp[k] = Arr[i]
#             k += 1; i += 1

#         # add elements left in the second interval 
#         while(j <= end) :
#             temp[k] = Arr[j]
#             k += 1; j += 1

#         # copy temp to original interval
#         for i in range (start, end+1) :
#             Arr[i] = temp[i - start]