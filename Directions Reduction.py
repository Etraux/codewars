def dirReduc(arr):
    opposites = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH':'NORTH', 'WEST': 'EAST'}
    stack = []
    for direction in arr:
        if stack and opposites[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)
    return stack