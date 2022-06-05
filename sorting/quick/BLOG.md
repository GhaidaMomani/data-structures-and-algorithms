# Quick Sort
The algorithm was developed by a British computer scientist Tony Hoare in 1959. The name "Quick Sort" comes from the fact that, quick sort is capable of sorting a list of data elements significantly faster (twice or thrice faster) than any of the common sorting algorithms. It is one of the most efficient sorting algorithms and is based on the splitting of an array (partition) into smaller ones and swapping (exchange) based on the comparison with 'pivot' element selected. Due to this, quick sort is also called as "Partition Exchange" sort. Like Merge sort, Quick sort also falls into the category of divide and conquer approach of problem-solving methodology.

# Quicksort works in the following way
Before diving into any algorithm, its very much necessary for us to understand what are the real world applications of it. Quick sort provides a fast and methodical approach to sort any lists of things. Following are some of the applications where quick sort is used.

Commercial computing: Used in various government and private organizations for the purpose of sorting various data like sorting of accounts/profiles by name or any given ID, sorting transactions by time or locations, sorting files by name or date of creation etc.
Numerical computations: Most of the efficiently developed algorithms use priority queues and inturn sorting to achieve accuracy in all the calculations.
Information search: Sorting algorithms aid in better search of information and what faster way exists than to achieve sorting using quick sort.
Basically, quick sort is used everywhere for faster results and in the cases where there are space constraints.

# Explanation

Technically, quick sort follows the below steps:
Step 1 − choose teh last element as pivot which is hte 'array right'
Step 2 − traverse over the elements to comparing it to the last element the pivot 
Step 3 − Do the swap function 
Step 4 − Apply quick sort on right partition recursively

Step 1:

Make any element as pivot: Decide any value to be the pivot from the list. For convenience of code, we often select the rightmost index as pivot or select any at random and swap with rightmost. Suppose for two values “Low” and “High” corresponding to the first index and last index respectively.

In our case low is 0 and high is 5.
Values at low and high are 50 and 32 and value at pivot is 32.
Partition the array on the basis of pivot: Call for partitioning which rearranges the array in such a way that pivot (32) comes to its actual position (of the sorted array). And to the left of the pivot, the array has all the elements less than it, and to the right greater than it.
In the partition function, we start from the first element and compare it with the pivot. Since 50 is greater than 32, we don’t make any change and move on to the next element 23.
Compare again with the pivot. Since 23 is less than 32, we swap 50 and 23. The array becomes ``` 23, 50, 9, 18, 61, 32 ```
We move on to the next element 9 which is again less than pivot (32) thus swapping it with 50 makes our array as 23, ```9, 50, 18, 61, 32.```
Similarly, for next element 18 which is less than 32, the array becomes 23, 9, 18, 50, 61, 32. Now 61 is greater than pivot (32), hence no changes.
Lastly, we swap our pivot with 50 so that it comes to the correct position.
Thus the pivot (32) comes at its actual position and all elements to its left are lesser, and all elements to the right are greater than itself.

Step 2: The main array after the first step becomes
```
23, 9, 18, 32, 61, 50
```
Step 3: Now the list is divided into two parts:

Sublist before pivot element
Sublist after pivot element
Step 4: Repeat the steps for the left and right sublists recursively. The final array thus becomes
```
9, 18, 23, 32, 50, 61.
```
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
# going through the process
Consider the following array: 50, 23, 9, 18, 61, 32. We need to sort this array in the most efficient manner without using extra place (inplace sorting).

Solution
Step 1:

Make any element as pivot: Decide any value to be the pivot from the list. For convenience of code, we often select the rightmost index as pivot or select any at random and swap with rightmost. Suppose for two values “Low” and “High” corresponding to the first index and last index respectively.
In our case low is 0 and high is 5.
Values at low and high are 50 and 32 and value at pivot is 32.
Partition the array on the basis of pivot: Call for partitioning which rearranges the array in such a way that pivot (32) comes to its actual position (of the sorted array). And to the left of the pivot, the array has all the elements less than it, and to the right greater than it.
In the partition function, we start from the first element and compare it with the pivot. Since 50 is greater than 32, we don’t make any change and move on to the next element 23.
Compare again with the pivot. Since 23 is less than 32, we swap 50 and 23. The array becomes 23, 50, 9, 18, 61, 32
We move on to the next element 9 which is again less than pivot (32) thus swapping it with 50 makes our array as 23, 9, 50, 18, 61, 32.
Similarly, for next element 18 which is less than 32, the array becomes 23, 9, 18, 50, 61, 32. Now 61 is greater than pivot (32), hence no changes.
Lastly, we swap our pivot with 50 so that it comes to the correct position.
Thus the pivot (32) comes at its actual position and all elements to its left are lesser, and all elements to the right are greater than itself.

Step 2: The main array after the first step becomes

23, 9, 18, 32, 61, 50
Step 3: Now the list is divided into two parts:

Sublist before pivot element
Sublist after pivot element
Step 4: Repeat the steps for the left and right sublists recursively. The final array thus becomes
9, 18, 23, 32, 50, 61.

The following diagram depicts the workflow of the Quick Sort algorithm which was described above.


## Approach & Efficiency
Space complexity Big O(logn)
Time complexity Big O(n^2)