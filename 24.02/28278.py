import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    data = input()
    if data[0] == '1':
        x, y = data.split()
        x = int(x)
        y = int(y)
        stack.append(y)
    else:
        x = int(data[0])
        if x == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif x == 3:
            print(len(stack))
        elif x == 4:
            if not stack:
                print(1)
            else:
                print(0)
        elif x == 5:
            if stack:
                print(stack[0])
            else:
                print(-1)