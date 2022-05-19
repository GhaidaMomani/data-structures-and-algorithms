
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
    merge function takes 3 arguments: left, right, array.
    left and right are the left and right halves of the array.
    arr is the array that is being sorted.
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
    
