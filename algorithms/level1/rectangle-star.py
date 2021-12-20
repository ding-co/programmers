n, m = map(int, input().strip().split(' '))
for i in range(m):
    for j in range(n):
        print("*", end = "")
    print()

# Other Solution
# print((("*" * n + "\n")* m).strip())

# https://programmers.co.kr/learn/courses/30/lessons/12969