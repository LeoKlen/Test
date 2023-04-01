qty = int(input())
b = set()
for i in range(qty):
    s = input()
    b = b | set(s.split())
print(*b, sep='\n')
