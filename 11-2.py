from functools import cache

@cache
def calc(x, c):
	if c == 0:
		return 1
	if x == 0:
		return calc(1, c - 1)
	elif len(str(x)) % 2 == 0:
		return calc(int(str(x)[:len(str(x)) // 2]), c - 1) + calc(int(str(x)[len(str(x)) // 2:]), c - 1)
	else:
		return calc(x * 2024, c - 1)

s = list(map(int, input().split()))

print(sum(map(lambda x: calc(x, 75), s)))
