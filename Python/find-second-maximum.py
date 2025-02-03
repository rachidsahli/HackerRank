n = int(input())
arr = map(int, input().split())

unique = list(set(arr))
unique.sort()

print(unique[-2])