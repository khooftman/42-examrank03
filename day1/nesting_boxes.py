def nesting_boxes(tags: str) -> bool:
    stack = []
    
    for char in tags:
        if char == '{': stack.append('}')
        elif char == '(': stack.append(')')
        elif char == '[': stack.append(']')
        elif char in '}])':

            if not stack or stack.pop() != char:
                return False
            
    return len(stack) == 0
