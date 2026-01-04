def isValid(s: str) -> bool:
    mappings = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    stack = []

    for ch in s:
        if ch in mappings.keys():
            stack.append(mappings[ch])
        else:
            prev = stack.pop() if stack else "#"

            if prev != ch:
                return False

    return not stack

s = "([)]"
print(isValid(s))