q = []
top = -1
while True:
    num = int(input())
    if not q or q[top] > num:
        q.append(num)
        top += 1
        continue


    if q[top] < num:
        print(q.pop())
        top -= 1
        if q[top] < num:
            print(num)
            print(q.pop())
            top -= 1
