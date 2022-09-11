a = input().split()
m = int(a[0])
n = int(a[1])

h = 0

storage = list()
storage = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        h+=1
    if i in B:
        h-=1

print(h)
