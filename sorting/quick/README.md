# [PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/21)
# Challenge Summary
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Quick Sort based on the pseudocode provided.

## Whiteboard Process

![](../quick/assets/Lomuto_animated.gif) 
<!-- Embedded whiteboard image -->





# Pseudo Code

``` python
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp



```



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
``` py

def quick_sort(lst, left, right):
    if left < right:

        # Partition the array by setting the position of the pivot value
        position = partition(lst, left, right)

        # Sort the left
        quick_sort(lst, left, position - 1)

        # Sort the right
        quick_sort(lst, position + 1, right)

def partition(lst, left, right):
#     // set a pivot value as a point of reference
    pivot = lst[right]
#     // create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    for i in range(left, right):
        if lst[i] <= pivot:
            low += 1
            swap(lst, i, low)

    #  // place the value of the pivot location in the middle.
#      // all numbers smaller than the pivot are on the left, larger on the right.
    swap(lst, right, low + 1)
#     // return the pivot index point
    return low + 1

def swap(lst, i, low):
    lst[i], lst[low] = lst[low], lst[i]




```



<hr/>
<p align="right">(<a href="#top">back to top</a>)</p>
<br/><br/>
<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>
<p align="right">22, 25 May </p>
