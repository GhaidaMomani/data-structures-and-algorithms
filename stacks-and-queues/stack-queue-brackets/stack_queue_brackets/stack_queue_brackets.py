
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
