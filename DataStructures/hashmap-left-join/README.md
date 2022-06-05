# Left Join for HashMaps

Implement a simplified LEFT JOIN for 2 Hashmaps.

[PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/24)

---
## Challenge 
- [x] Write a function that LEFT JOINs two hashmaps into a single data structure.
- [x] The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- [x] The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- [x] Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- [x] LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of `None` should be appended to the result row.
- [x] The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
- [x] Avoid utilizing any of the library methods available to your language.



# Example
INPUT
![](../hashmap-left-join/assets/input.png)

OUTPUT

```
[
   ["font", "enamored", "averse"],
   ["wrath", "anger", "delight"],
   ["diligent", "employed", "idle"],
   ["outfit", "garb", NULL],
   ["guide", "usher","follow"]
]

```
---

## Whiteboard

![](../hashmap-left-join/assets/hashmap_lefjoin.jpg)


---
## Approach & Efficiency


O(n) time given the length of the left hashmap
O(n) space based on the number of keys in left hashmap.

---

## Solution
```py
   def left_join(hashmap1, hashmap2):
    """Takes in two hash maps and left joins them. 
    The first parameter will look the the second parameter for matching keys and get those values, 
    if no match is found null will be return for that row in the the table. 
    Result will be a returned combination of both.
    """
    output = []

    for key in hashmap1:
        row = []
        row.append(key)
        row.append(hashmap1[key])

        try:
            if hashmap2[key]:
                row.append(hashmap2[key])
        except:
            row.append(None)

        output.append(row)
    return output
``` 


