qty = int(input())
arr = []
for i in range(qty):
    s = int(input())
    arr.append(s)
step = int(input())
for i in range(len(arr)):
    arr[i] = arr[i] ** step
for i in range(len(arr)):
    print(arr[i])
