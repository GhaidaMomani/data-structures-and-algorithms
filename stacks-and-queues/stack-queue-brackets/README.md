
# Data Structures and Algorithms

## Code 401 - Advanced Software Development
<!-- This is the reading notes repository where I keep my favorite articles with their sources.
       
       Hope you'll benefit from my reads, Enjoy!
-->




By [Ghaida Al Momani] (https://github.com/GhaidaMomani).

>>>>>Welcome to Code 401.
<br/>
<hr/>
<br/>



# stack_queue_brackets

Multi-Bracket Validation is a challenge to verify that an inputed string has balanced brackets. It will return a boolean representing whether or not the brackets in the string are balanced. There are three types of brackets:

Round Brackets: ()
Square Brackets: []
Curly Brackets: {}

## [PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/11)



## Approach & Efficiency

**validate_brackets function**
This functions validates the brackets to check if there is an even number of them first 
The first loop has the complexity of O(n) for time and O(n) for space 
The next loop does the same work but for the closing brackets which make the function of O(n) time efficiency. 





## Whiteboard 

![](../assets/brackets.jpg)






# API
[Code](../stack-queue-brackets/stack_queue_brackets/stack_queue_brackets.py)




# solution 

```python


def validate_brackets(string):
    """
    This method takes a string arguments to check if the brackets are balanced in pairs.
    """
    brackets = []
    open_brackets = []
    bracket_dict = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    if string.count('{') == string.count('}') and string.count('(') == string.count(')') and string.count('[') == string.count(']'):

        for char in string:
            if char in ['(', ')', '[', ']', '{', '}']:
                brackets.append(char)

            if len(brackets) == 0:
                return True

        if brackets[0] in [')', '}', ']']:
            return False

        for bracket in brackets:
            if bracket in ['(', '[', '{']:
                open_brackets.append(bracket)

            elif open_brackets:
                if bracket_dict[bracket] == open_brackets[len(open_brackets)-1]:
                    open_brackets.pop()
                else:
                    return False
            else:
                return False
    else:
        return False

    return True




```




<hr/>
 <br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>

<p align="right">22, 4 APR </p>