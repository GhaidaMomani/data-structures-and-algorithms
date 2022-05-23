# Hash Map
# [PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/19)


## Features
 Write a function that accepts a lengthy string parameter.
 Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write at least three test assertions for each method that you define.

Ensure your tests are passing before you submit your solution.

## Approach & Efficiency

Repeated_word takes in an initial string, to get a list of words we must split the string based on spaces. Now, before we do this I wanted to ensure common special grammer characters were removed and replaced with a space. This was done using regex, O(n) on the initial string. Next we take a O(1) space string and make it to a list. here we create a dictionary to keep track of some values. Then O(N) as we loop through the list of words, increasing the counter for that word, key, in dictionary by 1. When a word reacheds a count of 2, the loop breaks and returns the output word. This whole operation is O(N) time complexity with a space of O(N) based on the length of the initial string.