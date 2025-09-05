def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:
        parts = op.split()
        if parts[0] == "1":  # push
            x = int(parts[1])
            stack.append(x)
            if not max_stack:
                max_stack.append(x)
            else:
                max_stack.append(max(x, max_stack[-1]))
        elif parts[0] == "2":  # pop
            if stack:
                stack.pop()
                max_stack.pop()
        else:  # parts[0] == "3"
            if max_stack:
                result.append(max_stack[-1])
    
    return result


if __name__ == "__main__":
    n = int(input().strip())  # number of operations
    operations = [input().strip() for _ in range(n)]
    
    ans = getMax(operations)
    for val in ans:
        print(val)
